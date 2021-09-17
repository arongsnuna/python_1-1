# 사용자로부터 도형 데이터 파일에서부터 입력 받기
#   입력 받은 데이터를 이용해서 리스트 구성
#      파일 열기
#      파일에 데이터가 있으면
#          첫 번째 데이터는 모양 --> 리스트에 추가
#          모양을 확인하고 몇 개 데이터를 추가로 받을 지 결정하고 입력 받기
#          데이터 개수에 따라서 입력을 받으면서 튜플을 생성
#          생성된 튜플을 리스트에 추가
#      반복
#      파일 닫기
# 면적 계산
#    리스트의 요소를 한 개씩 확인하면서 면적을 계산
#    모양을 확인
#       모양에 따라서 다른 면적 계산 함수를 호출
import math

def createShapeTuple(num, lines):
    t1 = ()
    for i in range(num):
        n = int(getLineFromList(lines))
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

# (x1, y1, x2, y2)
def calcRectanglePerimeter(t):
    return 2 * ((t[2] - t[0]) + (t[1] - t[3]))

# (x1, y1, x2, y2, x3, y3)
def calcTrianglePerimeter(t):
    return (t[4] - t[2]) + (t[1] - t[5]) + math.sqrt((t[0] - t[2]) ** 2 + (t[1] - t[3]) ** 2)

# x, y, r
def calcCircleCircumference(t):
    return 2 * math.pi * t[2]

lineNum = 0
def getLineFromList(lines):
    global lineNum
    if lineNum >= len(lines):
        return ""
    str = lines[lineNum]
    if str[-1] == '\n':
      str = str[:-1]
    lineNum += 1
    return str

shapeList = []
f = open("MP10data.txt")
lines = f.readlines()
print(lines)
f.close()

shapeStr = getLineFromList(lines)

while shapeStr:
    shapeList.append(shapeStr)
    t = ()
    if shapeStr == "사각형":
        t = createShapeTuple(4, lines)
    elif shapeStr == "삼각형":
        t = createShapeTuple(6, lines)
    elif shapeStr == "원":
        t = createShapeTuple(3, lines)
    else:
        print("도형의 모양은 사각형, 삼각형, 원 중에 한 가지만 가능합니다.")
    shapeList.append(t)
    shapeStr = getLineFromList(lines)   
print(shapeList)  

for i in range(0, len(shapeList), 2):
    print(shapeList[i])
    if shapeList[i] == "사각형":
        print("면적", calcRectangleArea(shapeList[i + 1]))
        print("둘레", calcRectanglePerimeter(shapeList[i + 1]))
    elif shapeList[i] == "삼각형":
        print("면적", calcTriangleArea(shapeList[i + 1]))
        print("둘레", calcTrianglePerimeter(shapeList[i + 1]))
    elif shapeList[i] == "원":
        print("면적", calcCircleArea(shapeList[i + 1]))
        print("둘레", calcCircleCircumference(shapeList[i + 1]))
