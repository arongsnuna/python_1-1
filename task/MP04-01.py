year=int(input("년도를 입력하세요: "))

if year%400==0 :
    print(year,"년은 윤년입니다")
elif year%4==0:
    if year%100==0:
        print(year,"년은 윤년이 아닙니다")
    else:
        print(year,"년은 윤년입니다")
else:
    print(year,"년은 윤년이 아닙니다")
    
        
        
