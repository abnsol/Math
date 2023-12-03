def lucky_num(n):
    lucky_list = list(range(1, n + 1))  
    for j in lucky_list:
         follower=0
         a=len(lucky_list)
         if j==1:follower+=j
         else: follower+=j-1
         while follower<a:
             if j==1:             
                del lucky_list[follower]
                a-=1
                follower+=j
             else:
                del lucky_list[follower]
                a-=1
                follower+=j-1
    return lucky_list
print(lucky_num(1000))
