import random
def fun(a,b,c):
    number = []
    new_number = list(range(a,b+1))
    while c > 0:
        i = len(new_number)
        count=random.randint(0,i-1)
        number.append(new_number[count])
        new_number.remove(new_number[count])
        c -= 1
    number.sort()
    print(number)
print('红色随机号码是：',end = '')
fun(1,35,5)     #从1到33号码中随机抽取6个
print('蓝色随机号码是：',end = '')
fun(1,12,2)     #从1到16号码中随机抽取1个
print('体彩大乐透简直蠢到爆了')
