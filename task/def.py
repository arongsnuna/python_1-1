
def isLeapYear(year):
    if year%400==0 :
        return True 
    
    elif year%4==0:
       if year%100==0:
           return False
        
       else:
           return True
        
    else:
        return False



def getDayOfYear(year,month,day):
    dayOfYear=(month-1)*31+day
    if month<1 and month>12:
        return 0
    elif month>=3 and month<=12 :
        if year<=0:
            return 0
        elif year%400==0:
            A= dayOfYear - ((4*month+23)//10)+1
            return A
        elif year%4==0:
            if year%100==0:
                A= dayOfYear - ((4*month+23)//10)
                return A
            else:
                A=dayOfyear-((4*month+23)//10)+1
                return A
        else:
            A= dayOfYear - ((4*month+23)//10)
            return A
    else:
        print(dayOfYear)
        return
    
    
    
      
    
    
