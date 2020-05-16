def factorial_num(num):
    multi = 1
    if num == 1:
        return 1
    elif num < 0:
        return "Factorial of a negative number is undefined"
    else:
        for elem in range(1,num+1,1):
            multi *= elem
        return multi
print(factorial_num(0))