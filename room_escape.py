import sys
from bangtal import *



scene1 = Scene("룸1", "RoomEscape//배경-1.png")





# 탁자 생성
table = Object("RoomEscape//table(2).png")  # 탁자 이미지 필요
table.locate(scene1, -20, 50)  # 탁자를 검정 벽 쪽으로 이동
table.setScale(0.4)  # 크기 조정
table.show()

#컴퓨터 생성
computer = Object("RoomEscape//computer(5).png")  # 노트북 이미지 필요
computer.locate(scene1, 70, 370)  # 노트북을 탁자 위로 위치 조정
computer.setScale(0.07)  # 크기 조정
computer.show()

keypad1 = Object("RoomEscape//키패드.png")
keypad1.locate(scene1, 300, 60)
keypad1.show()



light = Object("RoomEscape//light(2).png")  # 조명 이미지 경로
light.locate(scene1, 300, 60)  # 천장 위치에 조명 배치
light.setScale(0.7)  # 조명의 크기를 조정
light.show()



sofa = Object("RoomEscape//sofa.png")
sofa.locate(scene1,1010,60)
sofa.setScale(0.5)
sofa.show()

door1 = Object("RoomEscape//문-오른쪽-닫힘.png")
door1.locate(scene1, 800, 270)
door1.show()



key = Object("RoomEscape//열쇠.png")
key.setScale(0.2)
key.locate(scene1, 600, 150)
key.show()


flowerpot = Object("RoomEscape//화분.png")
flowerpot.locate(scene1, 550, 150)
flowerpot.show()



scene2 = Scene("룸2", "RoomEscape//배경-2.png")

door2 = Object("RoomEscape//문-왼쪽-열림.png")
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object("RoomEscape//문-오른쪽-닫힘.png")
door3.locate(scene2, 910, 270)
door3.show()

keypad = Object("RoomEscape//키패드.png")
keypad.locate(scene2, 885, 420)
keypad.show()

switch = Object("RoomEscape//스위치.png")
switch.locate(scene2, 880, 440)
switch.show()

password = Object("RoomEscape//암호.png")
password.locate(scene2, 400, 100)

board = Object("RoomEscape//board.png")
board.setText("한글 ABCD\n1234")
board.locate(scene1, 900, 600)
board.show()

door1.closed = True
def onMouseAction_door1(x, y, action):
    global door1, key, scene2
    if door1.closed == True:
        if key.inHand():
            door1.setImage("RoomEscape//문-오른쪽-열림.png")
            door1.closed = False
        else:
            showMessage("열쇠가 필요해~~~")
    else:
        scene2.enter()
door1.onMouseAction = onMouseAction_door1

def onMouseAction_key(x, y, action):
    global key
    key.pick()
key.onMouseAction = onMouseAction_key

flowerpot.moved = False
def onMouseAction_flowerpot(x, y, action):
    global flowerpot
    if flowerpot.moved == False:
        if action == MouseAction.DRAG_LEFT:
            flowerpot.locate(scene1, 450, 150)
            flowerpot.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot.locate(scene1, 650, 150)
            flowerpot.moved = True
flowerpot.onMouseAction = onMouseAction_flowerpot

def onMouseAction_door2(x, y, action):
    global scene1
    scene1.enter()
door2.onMouseAction = onMouseAction_door2

door3.closed = True
door3.unlocked = False
def onMouseAction_door3(x, y, action):
    global door3
    if door3.unlocked == False:
        showMessage("문이 잠겨있다.")
    elif door3.closed == True:
        door3.setImage("RoomEscape//문-오른쪽-열림.png")
        door3.closed = False
    else:
        endGame()
door3.onMouseAction = onMouseAction_door3

def onKeypad_door3():
    global door3
    showMessage("철커덕")
    door3.unlocked = True
door3.onKeypad = onKeypad_door3

def onMouseAction_keypad(x, y, action):
    showKeypad("BANGTAL", door3)
keypad.onMouseAction = onMouseAction_keypad



switch.lighted = True
def onMouseAction_switch(x, y, action):
    global switch, password, scene2
    switch.lighted = not switch.lighted
    if switch.lighted == True:
        scene2.setLight(1.)
        password.hide()
    else:
        scene2.setLight(.2)
        password.show()
switch.onMouseAction = onMouseAction_switch
def onMouseAction_computer(x, y, action):
    showMessage("힌트 : '난 요즘 컴퓨터로 계속 작업하는데\n빛이 너무 강해서 그런가 눈이 너무 아파서\n소파에서 가끔씩 쉬면서 해'\n조명쪽으로 가서 빛 조절좀 해줄래?")
    
computer.onMouseAction = onMouseAction_computer

def onMouseAction_light(x,y,action):
    showMessage("방금 힌트를 봤을거야\n 거기에 나온 문장들을 잘보면 지금 이 방에 있는 물건들이 문장 속에 있을거야\n그 단어들을 잘 조합해서 다음의 퀴즈를 풀어줘")
light.onMouseAction = onMouseAction_light

def onMouseAction_keypad1(x, y, action):
    showKeypad("CLS",door1)
keypad1.onMouseAction = onMouseAction_keypad1


# showMessage("먼저 탁자위에 있는 컴퓨터로 가봐!\n열쇠를 얻기 위한 힌트가 주어질거야")
startGame(scene1)
