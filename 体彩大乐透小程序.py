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
print('��ɫ��������ǣ�',end = '')
fun(1,35,5)     #��1��33�����������ȡ6��
print('��ɫ��������ǣ�',end = '')
fun(1,12,2)     #��1��16�����������ȡ1��
print('��ʴ���͸��ֱ��������')