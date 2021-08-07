# -*- codiyng: UTF-8 -*-
# Filename : time_use
# author by : yanbing

# 以下实例使用 time 模块来实现秒表功能：


import time

print('按下回车开始计时，按下 Ctrl + C 停止计时。')
while True:

    input(" ")  # 如果是 python 2.x 版本请使用 raw_input()
    start_time = time.time()
    print('开始')
    try:
        while True:
            print('计时: ', round(time.time() - start_time, 0), '秒', end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        end_time = time.time()
        print('总共的时间为:', round(end_time - start_time, 2), 'secs')
        break
