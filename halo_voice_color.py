# generated by mBlock5 for HaloCode
# codes make you happy
import halo, time
halo.speech_recognition.set_recognition_url(halo.speech_recognition.SERVER_MICROSOFT, "http://msapi.passport3.makeblock.com/ms/bing_speech/interactive")
halo.speech_recognition.set_token(halo.speech_recognition.SERVER_MICROSOFT,token = "3tlpvvsk407")

halo.led.show_all(25, 25, 255)
while not halo.wifi.is_connected():
    # 修改 wifi名称 为家里wifi的名字
    # 修改 密码 为家里wifi的密码
    # 前后双引号要保留！
    halo.wifi.start(ssid = "linksys" or "ASUS", password = "creative", mode = halo.wifi.WLAN_MODE_STA)
halo.led.show_all(90, 90, 225)

while True:
    if halo.button.is_pressed():
        halo.led.show_all(10, 0, 10)
        halo.speech_recognition.start(halo.speech_recognition.SERVER_MICROSOFT, halo.speech_recognition.LAN_CHINESE, 3)
        result = halo.speech_recognition.get_result_code()
        if "红色" in result:
            halo.led.show_all(255, 0, 0)
        elif "黄色" in result:
            halo.led.show_all(255, 255, 0)
        elif "白色" in result:
            halo.led.show_all(255, 255, 255)
        elif "绿色" in result:
            halo.led.show_all(0, 255, 0)
        elif "蓝色" in result:
            halo.led.show_all(0, 0, 255)
        elif "粉色" in result:
            halo.led.show_all(255,0, 255)
        elif "关机" in result:
            halo.led.show_all(0,0, 0)
        elif "音量测试" in result:
            p=100/12
            while True:
                mic_value = halo.microphone.get_loudness("maximum")
                led = mic_value//p
                for i in range(led):
                    halo.led.show_single(i+1,46,0,173)
                time.sleep(0.1)
                halo.led.off_all()
        elif "彩虹" in result:
            halo.led.show_animation(rainbow)
        else:
            halo.led.show_all(10,10,10 )
