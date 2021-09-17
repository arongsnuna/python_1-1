#arongsowner


#함수안에서 할일
#1. 양 끝단에 있는 공백제거
#2. 공백문자 찾아내기
#3. 처음부터 공백문자의 위치까지 문자열 자르기 (=첫 단어)
#4. 첫 단어를 제외한 문자열에서 양 끝단에 있는 공백제거
#5. 두번째 공백문자 찾아내기
#6. 공백문자가 없다면 두 단어로 구성된 문자열임으로 첫 단어만을 반환
#7-1. 공백문자가 있다면 세 개 이상의 단어로 구성된 문자열임으로
#7-2. 첫번째 공백문자의 위치부터 두번째 공백문자의 위치까지 문자열 자르기 (=두번째 단어)
#7-3. 첫단어와 두번째단어를 제외한 문자열에서 양 끝단에 있는 공백제거
#7-4. 세번째 공백문자 찾아내기
#7-5-1. 공백문자가 없다면 세단어로 구성된 문자열임으로 첫단어와 세번째 단어를 반환
#7-5-2. 이때 세번째 단어는 두번째 공백문자부터 끝까지이다
#7-6-1. 공백문자가 있다면 네 개 이상의 단어로 구성된 문자열임으로
#7-6-2. 첫단어와 세번째 단어를 반환
#7-6-3. 이때 세번째 단어는 두번째 공백문자부터 세번째 공백문자까지이다.


#8. 문자열 입력받기
#9. 양끝단에 있는 공백제거
#10. 한단어로 구성되어있으면 두단어로 입력해야한다고 출력
#11. 두단어 이상의 문자열로 구성되어있으면 함수호출
#12. 결과값과 결과값의 길이 출력


def firstThirdWord(str):
    newSen= str.strip()
    num=newSen.find(' ')
    newSen2=newSen[num+1:].strip()
    num2=newSen2.find(' ')
    if num2 == -1 :
        result=newSen[:num]
        return result
    else:
        newSen3=newSen2[num2+1:].strip()
        num3=newSen3.find(' ')
        if num3 == -1:
            result=newSen[:num]+' '+newSen3
            return result
        else :
            result=newSen[:num]+' '+newSen3[:num3]
            return result
                           

sen = str(input("문자열을 입력하세요: "))
newSen= sen.strip()
num=newSen.find(' ')
if num == -1 :
    print("최소한 두 개 이상의 단어로 구성된 문자열을 입력해야 합니다.")
else:
    a=firstThirdWord(newSen)
    print( a,len(a),sep=', ')
    

    
                 
    
        
