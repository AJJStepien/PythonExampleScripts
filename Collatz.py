num=int(input("Podaj nieujemną i niezerową dla problemu Collatza: "))

step = 0
while num != 1:
    if num % 2 == 0:
        num = int(num/2)
    else:
        num = int(3 * num + 1)
    step += 1
    print(step,".  " ,num, sep="")