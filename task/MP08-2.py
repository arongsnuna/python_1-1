# 두 번째 풀이 방법 재귀호출 사용

def remains0(num):
    if num % 7 == 0:
        return True
    return False

#print(remains0(7))
#print(remains0(35))
#print(remains0(36))
#print(remains0(6))

def remains1(num):
    if num % 2 == 1 and num % 3 == 1 and num %4 == 1 and num % 5 == 1 and num % 6 == 1:
        return True
    return False

#print(remains1(301))
#print(remains1(300))
#print(remains1(299))

def findNum(num):
    while not (remains0(num) and remains1(num)):
        num += 1
    return num

#print(findNum(301))
#print(findNum(100))
#print(findNum(302))

def findNthLowestNum(a, m, n):
    b = findNum(n)
    if a >= m:
        return b
    else:
        return findNthLowestNum(a + 1, m, b + 1)
        
m = int(input("1보다 큰 정수를 입력하세요:"))
n = findNthLowestNum(1, m, 1)
print(n)
