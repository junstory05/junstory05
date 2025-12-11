import ctypes
import os
import time
t = 60

ctypes.windll.user32.MessageBoxW(0, "그러게 왜 실행했냐 낄낄", "title", 16)
ctypes.windll.user32.MessageBoxW(0, "이 컴퓨터는 60초 뒤에 종료된다.", "title", 16)
os.system('shutdown -s -t 60')
for i in range(60):
    print(t)
    t -= 1
    time.sleep(1)