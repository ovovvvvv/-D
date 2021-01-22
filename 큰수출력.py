num1=int(input("첫 번째 숫자:"))
num2=int(input("두 번째 숫자:"))
num3=int(input("세 번째 숫자:"))

if (num1>=num2)and(num1>=num3):
    large=num1
elif (num2>=num1) and (num2>=num3):
    large=num2
else:
    large=num3

print("가장 큰 수는 %d입니다."%(large))
