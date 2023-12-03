
number_of_soldiers=int(input("How many soliders are there: "))
def sit(number_of_soliders):
    a=0
    b=0
    while b<number_of_soliders:
         a+=1
         b=2**a
    else:
        b=2**(a-1)
    l=2*(number_of_soliders-b)+1
    answer=f'If there are {number_of_soliders} soliders, you should sit on the {l} sit not to be killed.'
    return answer
print(sit(number_of_soldiers))
