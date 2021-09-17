# 입력 받기
# 2 이상의 정수인지 확인
# 2 이상이면 반환
# 아니면 입력 받기로 되돌아가서 반복
def readNumber():
    n = int(input("2이상의 정수를 입력하세요: "))
    while n < 2:
        print("2 이상의 정수를 입력하세요")
        n = int(input("2이상의 정수를 입력하세요: "))
    return n

# count = 2
# 2 ~ num - 1까지 반복 --> i (2부터 n까지 1씩 증가되는 정수)
#     num % i == 0인지 확인
#         나눠지면 count를 1 증가
def getCountsOfDivisors(num):
    count = 2
    for i in range(2, num):
        if num % i == 0:
            count += 1    
    return count

# 약수가 2개이면 소수, 3 개 이상이면 소수가 아님
def isPrime(num):
    return getCountsOfDivisors(num) == 2    

# 사용자로부 입력을 받아야 함 (2이상의 정수를 입력 받기)
#      readNumber()
# 2-n까지 반복 --> i (2부터 n까지 1씩 증가되는 정수)
#     약수의 개수 구하기 (getCountsOfDivisors(i))
#     소수인지 확인 (isPrime(i))
#     출력 (정수, 약수 개수, 소수인지 아닌지)
n = readNumber()
for i in range(2, n + 1):
    count = 2
    for j in range(2, i):
        if i % j == 0:
            count += 1    
    #prime = isPrime(i)
    print("정수:", i, " 약수 개수: ", count, " 소수:", isPrime(i))
