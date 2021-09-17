year=int(input("년도를 입력하세요: "))
month=int(input("월을 입력하세요: "))
day=int(input("일을 입력하세요: "))


dayOfYear=(month-1)*31+day


if month>=3 and month<=12 :
    if year%400==0 :
        A= dayOfYear - ((4*month+23)//10)+1
        print("통일: ",A)
        
    elif year%4==0 :
        if year%100==0 :
            A= dayOfYear - ((4*month+23)//10)
            print("통일: ",A)
        else:
            A= dayOfYear - ((4*month+23)//10) +1
            print("통일: ",A)
    else:
        A= dayOfYear - ((4*month+23)//10)
        print("통일: ",A)
else:
    print("통일: ",dayOfYear)
        
    


