import os
from tkinter import *
import pyautogui as pag
import time
import threading

record_pos = (195, 285)          # row의 위치
gyogicwon_pos = (720,614)        # 교직원 버튼 위치
Issue_button_pos = (922,699)     # 발급버튼 위치
Issue_program_pos = (265,12)     # 발급프로그램_창 위치
complete_button_pos = (681,555)  # 완료버튼 위치


def issue():
    pag.click(Issue_program_pos)           # 발급프로그램 클릭하여 활성화
    time.sleep(2)
    while True:
        pag.click(record_pos, clicks=2)    # 레코드 더블클릭
        time.sleep(2)
        pag.click(Issue_button_pos)        # 발급버튼 클릭
        time.sleep(40)                     # 발급중 대기
        i = 0
        while i < 10:
            i += 1
            alert = pag.locateCenterOnScreen('check1.png')    # Alert 경고문(알림창) 처리 구간
            pag.click(alert)
            alert1 = pag.locateCenterOnScreen('check2.png')  # Alert 이미지는 '확인' 버튼을 캡쳐하는데, 중앙 정사각형 모양으로 잡아야 함.
            pag.click(alert1)
            alert2 = pag.locateCenterOnScreen('check3.png')
            pag.click(alert2)
            alert3 = pag.locateCenterOnScreen('check4.png')
            pag.click(alert3)
            alert4 = pag.locateCenterOnScreen('check5.png')
            pag.click(alert4)
            alert5 = pag.locateCenterOnScreen('check6.png')
            pag.click(alert5)
            alter6 = pag.locateCenterOnScreen('check7.png')
            pag.click(alter6)
            alter7 = pag.locateCenterOnScreen('check8.png')
            pag.click(alter7)
        time.sleep(2)


def kill_t():
    pid = os.getpid()
    os.kill(pid, 2)


t1 = threading.Thread(target=issue)

window = Tk()
window.title("발급자동화 매크로_학생 by KOO")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=400)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150, 207, text="안뇽이를 클릭하면 발급 시작, 인덕이를 클릭하면 프로그램 종료",
    width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

anyong2_img = PhotoImage(file="anyong2.png")
anyong2_button = Button(image=anyong2_img, highlightthickness=0, command=t1.start)
anyong2_button.grid(row=1, column=0)

induck_img = PhotoImage(file="induck2.png")
induck_button = Button(image=induck_img, highlightthickness=0, command=threading.Thread(target=kill_t).start)
induck_button.grid(row=1, column=3)

window.mainloop()

# how to compile py.exe : pyinstaller -w -F 'fileName.py'