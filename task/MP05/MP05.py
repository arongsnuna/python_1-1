# 1. import random, turtle
# 2. win, turtle 생성 (거북이 2개 생성)
# 3. 거북이를 배치 (화면에 배치)
# 4. 카드 이미지 등록
# 5. random number 생성
# 6. 거북이로 카드 이미지로 보이도록 함
# 7. 숫자 비교
# 8. 누가 이겼는지 혹은 비겼는지 화면에 출력

# 1
import random
import turtle

# 2
win = turtle.Screen()
tLeft = turtle.Turtle()
tRight = turtle.Turtle()

# 3
tLeft.penup()
tLeft.goto(-200, 0)
tLeft.pendown()
tRight.penup()
tRight.goto(200, 0)
tRight.pendown()

# 4
win.addshape("ace_of_spades.gif")
win.addshape("jack_of_spades.gif")
win.addshape("queen_of_spades.gif")
win.addshape("king_of_spades.gif")
win.addshape("2_of_spades.gif")
win.addshape("3_of_spades.gif")
win.addshape("4_of_spades.gif")
win.addshape("5_of_spades.gif")
win.addshape("6_of_spades.gif")
win.addshape("7_of_spades.gif")
win.addshape("8_of_spades.gif")
win.addshape("9_of_spades.gif")
win.addshape("10_of_spades.gif")

# 5
leftNum = random.randint(1, 13)
rightNum = random.randint(1, 13)

# 6
print(leftNum)
filename = ""
if leftNum >= 2 and leftNum <= 10:
    filename = str(leftNum) + "_of_spades.gif"
elif leftNum == 1:
    filename = "ace_of_spades.gif"
elif leftNum == 11:
    filename = "jack_of_spades.gif"
elif leftNum == 12:
    filename = "queen_of_spades.gif"
#elif leftNum == 13:
else:
    filename = "king_of_spades.gif"
tLeft.shape(filename)
    
print(rightNum)
if rightNum >= 2 and rightNum <= 10:
    tRight.shape(str(rightNum) + "_of_spades.gif")
elif rightNum == 1:
    tRight.shape("ace_of_spades.gif")
elif rightNum == 11:
    tRight.shape("jack_of_spades.gif")
elif rightNum == 12:
    tRight.shape("queen_of_spades.gif")
elif rightNum == 13:
    tRight.shape("king_of_spades.gif")

# 7, 8
if leftNum > rightNum:
    print("왼쪽이 이겼습니다")
elif rightNum > leftNum:
    print("오른쪽이 이겼습니다")
else:
    print("양쪽이 비겼습니다")
