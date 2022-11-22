select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

## 메인 코드 부분 ##
# eval 함수 사용
select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

if select == 1 :
    expression = input(" *** 수식을 입력하세요 : ")
    print(expression + " 결과는 " + str(eval(expression)) + "입니다.")
elif select == 2 :
    number1 = int(input("첫번째 숫자를 입력하세요 : "))
    number2 = int(input("두번째 숫자를 입력하세요 : "))
    sum = 0

    for i in range(number1, number2 + 1) :
        sum += i

    print(str(number1) + "..." + str(number2) + "는 " + str(sum) + "입니다.")

