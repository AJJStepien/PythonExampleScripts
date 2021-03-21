exampleList=['psy','dziki','kuny','jeże']
def printlist (list):
    amount=len(list)
    for i in range(amount):
        if i==amount-1:
            print('i',end=' ')
            print(list[i])
            break
        print(list[i], end=', ')
    print()
        
printlist(exampleList)
secondlist=[1,2,3,4,5,6,7,8]
printlist(secondlist)