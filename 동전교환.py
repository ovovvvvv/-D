money=int(input("교환할 금액:"))

c500=money//500
money%=500

c100=money//100
money%=100

c50=money//50
money%=50

c10=money//10
money%=10

print("500원: %d개"%c500)
print("100원: %d개"%c100)
print("50원: %d개"%c50)
print("10원: %d개"%c10)
print("잔돈:%d원"%money)