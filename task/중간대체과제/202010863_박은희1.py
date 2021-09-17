#arongsowner

#함수 안에서 할일
#1. 불쾌지수를 계산하는 공식을 작성해 함수를 정의
#2. 불쾌지수를 반환

#3. 함수 밖에서 사용자로부터 온도와 상대습도를 입력받기
#4. 함수를 호출
#5. 결과값과 기준값을 비교해 알맞은 불쾌지수의 정도 도출


def discomfortIndex(T,H) :
    DI = 0.81*T+0.01*H*(0.99*T-14.3)+46.3
    return DI

T=int(input("온도를 입력하세요: "))
H=int(input("상대습도를 입력하세요: "))

if discomfortIndex(T,H)<70:
    print("쾌적함")
elif discomfortIndex(T,H)>=70 and discomfortIndex(T,H)<80:
    print("일부 사람들이 불쾌감을 느낄 수 있음")
elif discomfortIndex(T,H)>=80 and discomfortIndex(T,H)<=83 :
    print("50% 정도의 사람들이 불쾌감을 느낌")
else:
    print("대부분의 사람들이 불쾌감을 느낌")
    



