import json
import os
from contextlib import suppress
from json import JSONDecodeError
from pathlib import Path

import allure
import pytest

from data.logs import MsgLog
from data.project_info import ProjectInfo


def log_step_to_allure():
    test_steps = []
    _msg_logs = MsgLog.msg_log

    # Find index step in list
    # get description from index
    steps_index = [
        index for index, value in enumerate(_msg_logs)
        if ("step" or "steps" or "Should see") in value.lower()
    ]

    for i in range(len(steps_index)):
        if i == (len(steps_index) - 1):
            test_steps.append(_msg_logs[steps_index[i]:])
            break
        test_steps.append(_msg_logs[steps_index[i]: steps_index[i + 1]])

    # Log test to allure reports
    for steps in test_steps:
        step = steps.pop(0)

        with allure.step(step):
            for verify in steps:
                with allure.step(verify):
                    pass

    del _msg_logs[:]


def modified_allure_report():

    allure_dir = Path(ProjectInfo.allure_dir)
    failed_steps = MsgLog.verify_log_failed

    result_files = list(allure_dir.glob("*-result.json"))
    result_files.sort(key=os.path.getctime)

    for file in result_files:
        with file.open("r", encoding="utf8") as _rf:
            with suppress(JSONDecodeError):
                json_obj = json.load(_rf)

                if json_obj["status"] == "failed":
                    json_obj["statusDetails"] = dict(message="\n".join(MsgLog.status_details[0]))
                    MsgLog.status_details.pop(0)

                end_index = failed_steps.index("end test")
                for item, err_msg in failed_steps[:end_index]:

                    for allure_step in json_obj.get("steps", []):
                        for verify_step in allure_step.get("steps", []):
                            if verify_step["name"] == item:
                                verify_step["status"] = "failed"
                                verify_step["statusDetails"] = dict(message=err_msg)

                                if json_obj.get("attachments"):
                                    verify_step["attachments"] = json_obj["attachments"][0]["type"] != "image/png" or [json_obj["attachments"].pop(0)]
                                allure_step["status"] = "failed"

                del failed_steps[:end_index + 1]

            # Write the modified json object
            with file.open("w") as _f:
                json.dump(json_obj, _f)
