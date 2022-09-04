import random

#修改accessToken(单人模式),多人模式此处accessToken不生效
accessToken = "tZM/+uPznH/j1NJPbDX****************************G2kjxfYjqsaw/M9AiZ2Glqg=="

# 选择模式 单人：single；多人：multi
# 多人模式 在accessToken.py 填写 accessToken
mode = "single"

#通知方式 推送加:pushplus、自建推送:diy、不用推送:None
notice="diy"
notice_token="ea6811587*************3868"

#问卷公共ID
__questionnaireVo_id__ = "1001642561233886004860000000001"

#提交的打卡数据
data = {
    "questionnairePublishEntityId": "1001662220806125006650000000001",
    "answerInfoList": [
        {
            "subjectId": "1001642561233888004860000000001",
            "subjectType": "multiSelect",
            "multiSelect": {
                "optionAnswerList": [
                    {
                        "beSelectValue": "NotThing",
                        "fillContent": ""
                    }
                ]
            }
        },
        {
            "subjectId": "1001642561233899004860000000001",
            "subjectType": "location",
            "location": {
                "deviationDistance": 705,
                "locationRangeId": "1001640250597565000250000000001",
                "address": "下陆区义诚学生公寓",
                "city": "黄石市",
                "province": "湖北省",
                "area": "下陆区",
                "latitude": 30.210418836805555,
                "longitude": 115.01871799045139,
                "street": "团城山街道"
            }
        },
        {
            "subjectId": "1001644805536031021720000000001",
            "subjectType": "simpleFill",
            "simpleFill": {
                "inputContent": "36",
                "imgList": []
            }
        },
        {
            "subjectId": "1001644805551540021560000000001",
            "subjectType": "simpleFill",
            "simpleFill": {
                "inputContent": "36",
                "imgList": []
            }
        },
        {
            "subjectId": "1001644805564033021720000000001",
            "subjectType": "simpleFill",
            "simpleFill": {
                "inputContent": "36",
                "imgList": []
            }
        }
    ]
}

for i in data["answerInfoList"]:
    try:
        if i["subjectType"] == "simpleFill":
            i["simpleFill"]["inputContent"] = str(random.randint(362, 370) / 10)

        if i["subjectType"] == "multiSelect":
            i["multiSelect"]["optionAnswerList"][0]["beSelectValue"] = "NotThing"

        if i["subjectType"] == "location":
            i["location"]["deviationDistance"] = int(i["location"]["deviationDistance"]) + random.randint(1,
                                                                                                          50)  # 偏差距离 米
            i["location"]["latitude"] = float(i["location"]["latitude"]) + random.randint(100, 999) / 10 ** 15  # 纬度
            i["location"]["longitude"] = float(i["location"]["longitude"]) + random.randint(100, 999) / 10 ** 15  # 经度
    except Exception as e:
        print("混淆问卷答案存在错误\n", e)
