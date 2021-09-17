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

def createShapeTuple(f, num):
    t1 = ()
    for i in range(num):
        n = int(f.readline())
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

def calcDistance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)    

# (x2 - x1) * 2 + (y1 - y2) * 2 
def calcRectanglePerimeter(t):
    return (t[2] - t[0]) * 2 + (t[1] - t[3]) * 2
    
# (y1 - y3) + (x3 - x2) + calcDistance(x1, y1, x2, y2)    
def calcTrianglePerimeter(t):
    return (t[1] - t[5]) + (t[4] - t[2]) + calcDistance(t[0], t[1], t[2], t[3])

def calcCirclePerimeter(t):
    return 2 * math.pi * t[2]

def readFileData(filename, shapeList):
    with open(filename, "r") as f:
        shapeStr = f.readline() # 첫 번째 줄 읽기
        shapeStr = shapeStr.strip() # 줄바꿈 문자 제거
        while shapeStr:
            shapeList.append(shapeStr)  # 도형 모양 추가
            t = ()
            if shapeStr == "사각형":
                t = createShapeTuple(f, 4)
            elif shapeStr == "삼각형":
                t = createShapeTuple(f, 6)
            elif shapeStr == "원":
                t = createShapeTuple(f, 3)
            else:
                print("도형의 모양은 사각형, 삼각형, 원 중에 한 가지만 가능합니다.")
            shapeList.append(t)
            shapeStr = f.readline()
            shapeStr = shapeStr.strip() # 줄바꿈 문자 제거
    return shapeList    

shapeList = []

shapeList = readFileData("MP10data.txt", shapeList)
#print(shapeList)

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
        print("둘레", calcCirclePerimeter(shapeList[i + 1]))

