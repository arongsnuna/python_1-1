# 사용자로부터 도형 데이터 5개를 입력 받기
#   입력 받은 데이터를 이용해서 리스트 구성
#      첫 번째 데이터는 모양 --> 리스트에 추가
#      모양을 확인하고 몇 개 데이터를 추가로 받을 지 결정하고 입력 받기
#      데이터 개수에 따라서 입력을 받으면서 튜플을 생성
#      생성된 튜플을 리스트에 추가
# 면적 계산
#    리스트의 요소를 한 개씩 확인하면서 면적을 계산
#    모양을 확인
#       모양에 따라서 다른 면적 계산 함수를 호출
import math

rectangleList = ( "x1 좌표를", "y1 좌표를", "x2 좌표를", "y2 좌표를" )
triangleList = ( "x1 좌표를", "y1 좌표를", "x2 좌표를", "y2 좌표를", "x3 좌표를", "y3 좌표를" )
circleList = ( "x 좌표를", "y 좌표를", "반지름을" )

def createShapeTuple(num, lst):
    t1 = ()
    for i in range(num):
        n = int(input(lst[i] + " 입력하세요: "))
        t1 = t1 + (n,)
    return t1

# (x1, y1, x2, y2)
def calcRectangleArea(t):
    return (t[2] - t[0]) * (t[1] - t[3])

# (x1, y1, x2, y2, x3, y3)
# (x3 - x2, y1 - y3)
def calcTriangleArea(t):
    return (t[4] - t[2]) * (t[1] - t[5]) / 2

# x, y, r
def calcCircleArea(t):
    return t[2] * t[2] * math.pi
    
shapeList = []
for i in range(5):
    shapeStr = input("도형 모양을 입력하세요: ")
    shapeList.append(shapeStr)
    t = ()
    if shapeStr == "사각형":
        t = createShapeTuple(4, rectangleList)
    elif shapeStr == "삼각형":
        t = createShapeTuple(6, triangleList)
    elif shapeStr == "원":
        t = createShapeTuple(3, circleList)
    else:
        print("도형의 모양은 사각형, 삼각형, 원 중에 한 가지만 가능합니다.")
    shapeList.append(t)
#print(shapeList)
for i in range(0, len(shapeList), 2):
    print(shapeList[i])
    if shapeList[i] == "사각형":
        print("면적", calcRectangleArea(shapeList[i + 1]))
    elif shapeList[i] == "삼각형":
        print("면적", calcTriangleArea(shapeList[i + 1]))
    elif shapeList[i] == "원":
        print("면적", calcCircleArea(shapeList[i + 1]))

