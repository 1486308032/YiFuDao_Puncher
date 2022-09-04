import requests

import accessToken
import config

"""
questionnairePublishEntityId 每日变化 问卷发布一级id
id 固定不变 问卷问题三级id
questionnaireEntityId 固定不变 问卷二级id

"""
__message__ = ""
__head__ = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 "
                  "Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "accessToken": config.accessToken,
    "userAuthType": "MS"
}
__questionnaireVo_id__ = config.__questionnaireVo_id__


def getQuestionId():
    url = "https://yfd.ly-sky.com/ly-pd-mb/form/api/healthCheckIn/client/student/indexVo"
    r = requests.get(url, headers=__head__).json()
    # print("1\n", r)
    if r["code"] == 200:
        print(r["data"]["title"])
        return r["data"]["questionnairePublishEntityId"]
    else:
        print("cookies失效")
        exit(0)


def getDetailWithAnswer(question_publish_id):
    url = "https://yfd.ly-sky.com/ly-pd-mb/form/api/questionnairePublish/{}/getDetailWithAnswer".format(
        question_publish_id)
    r = requests.get(url, headers=__head__).json()
    # print("2\n", r)
    if r["code"] == 200:
        if r["data"]["questionnairePublishFillVo"]["hadFill"]:
            print("今日已经打卡")
            exit(0)
        print(r["data"]["questionnairePublishFillVo"]["title"],
              r["data"]["questionnairePublishFillVo"]["createUserName"])
        return r["data"]["questionnaireWithSubjectVo"]
    else:
        print("cookies失效")
        exit(0)


def postData(question_publish_id):
    global __message__
    url = "https://yfd.ly-sky.com/ly-pd-mb/form/api/answerSheet/saveNormal"
    config.data["questionnairePublishEntityId"] = question_publish_id
    r = requests.post(url=url, headers=__head__, json=config.data).json()

    print(r)
    print(config.data)
    if r["code"] != 200:
        # postMessage("打卡失败")
        __message__ += "打卡失败"
    else:
        # postMessage("打卡成功")
        __message__ += "打卡成功"

        return 0


def start():
    question_publish_id = getQuestionId()

    subject_vo = getDetailWithAnswer(question_publish_id)
    if __questionnaireVo_id__ == subject_vo["questionnaireVo"]["id"]:
        print("问卷id相同，继续运行")
    else:
        print("问卷id不同，终止运行")
        return 0

    for i in subject_vo["subjectList"]:
        print(i["subjectTitle"])

    postData(question_publish_id)


def postMessage(msg="test123"):
    if config.notice == "pushplus":
        url = "http://www.pushplus.plus/send"
        data = {
            "token": config.notice_token,
            "title": "奕辅导签到情况",
            "content": msg,
            "template" : "txt"
        }
        r = requests.post(url=url, data=data)
        print(r.text)
    elif config.notice == "None":
        print(__message__)
    else:
        url = 'http://bt.bkpi.cn:5700/send_private_msg'
        # msg = json.dumps(msg, indent=4, ensure_ascii=False)
        data = {
            "user_id": "1486308032",
            "message": str(msg)
        }
        data_group = {
            "qq": "638679743",
            "msg": str(msg)
        }
        r = requests.post(url=url, data=data)
        print(r.text)


if __name__ == '__main__':
    if config.mode == "single":
        start()
    elif config.mode == "multi":
        for name, key in accessToken.data.items():
            __head__["accessToken"] = key
            print(name, ":")
            try:
                __message__ += "{}:".format(name)
                start()
            except:
                __message__ += "{}".format("遇到意外")
            finally:
                __message__ += "{}".format("\n")
    postMessage(__message__)
    # postData()
