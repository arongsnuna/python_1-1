d = float(input("쇼핑몰까지의 거리를 입력하세요: "))
price = float(input("컴퓨터의 가격을 입력하세요: "))
          
total = str(price + d/10*1400*2 + d/40*8590*2)

print("거리가 " ,d, " km이고, 컴퓨터 가격이 " ,price, " 원일 때 전체비용 = " ,total, " 원 입니다")

