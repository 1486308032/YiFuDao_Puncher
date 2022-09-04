# 奕辅导每日打卡
### 文件说明
`YiFuDao_Puncher.py`为打卡主程序  

`config.py`为配置文件  
* 【选择模式】单人：single；多人：multi
* 【accessToken】该变量用于单人模式填写`accessToken`，多人模式可忽略
* 【通知方式】填写`notice_token`用于发送运行结果 

`accessToken.py`用于多人模式填写`accessToken`，单人模式可忽略


### 使用方法（简易） & 单人模式
1. 抓取`accessToken`
![image](https://user-images.githubusercontent.com/50775291/188295787-c79cba73-c6eb-4fab-83a0-10495e4d807c.png)
* 打开奕辅导
* 使用fiddler锁定小程序进程（上图红色）
* 选择小程序的任意请求，在响应头中找到`accessToken`
![image](https://user-images.githubusercontent.com/50775291/188295461-73512179-0372-4be9-adc6-5a401a0f8ad8.png)
* 修改`config.py`中的`accessToken`值  

2.运行`YiFuDao_Puncher.py`即可打卡

### 无需服务器，使用actions运行
0. 了解**使用方法（简易） & 单人模式**
1. fork本项目
![image](https://user-images.githubusercontent.com/50775291/188301110-1bb7359c-eeb8-4474-80d3-540b51c2aeee.png)
2. 修改`config.py`配置文件，多人模式在`accessToken.py`填写`accessToken`
3. 进入actions，选择具体的`Workflows`并手动运行一次，此后会定时运行打卡程序
![image](https://user-images.githubusercontent.com/50775291/188301316-76be9bfc-385b-4432-afc0-2ca59e6f18e9.png)
4.修改打卡时间
* 修改`.github/workflows/work.yml`中的`- cron:  '5 16 * * *`，意思为16:05时运行程序，此处为UTC+0时间，换算成北京时间即为UTC+8 00:05时运行程序

### 推送方式
##### pushplus:
1. 注册账号，并关注微信公众号 www.pushplus.plus
2. 在`config.py`填写`notice_token`, `notice`设置为`"pushplus"`
![image](https://user-images.githubusercontent.com/50775291/188299451-b826d61b-f0ae-4b1f-adac-99e8e344d381.png)
![推送结果](https://user-images.githubusercontent.com/50775291/188299503-52c76ac6-022f-4ba6-8489-976af3f8919e.png)


### 注意！
* `__questionnaireVo_id_`为打卡问卷的ID，一般不会变化。当发布者修改了问卷，此ID将会变动，需要自己抓包并修改ID
* `question_publish_id`每天动态获取，每个人不同
* `accessToken`有时效性，一段时间后会失效，需重新抓取
