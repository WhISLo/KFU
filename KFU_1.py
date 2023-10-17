list_sum = []
list_dif = []
list_div = []
list_mult = []
while True:
    int1 = int(input())
    int2 = int(input())
    oper = input()
    str1 = ''

    if oper == '+':
        str1 += (str(int1) + oper + str(int2) + '=' + str(int1+int2))
        print(int1, oper, int2, '=', int1+int2,sep='')
        list_sum.append(str1) 
    if oper == '-':
        str1 += (str(int1)+oper+str(int2)+'='+str(int1-int2))
        print(int1, oper, int2, '=', int1-int2, sep='')
        list_dif.append(str1)
    if oper == '/':
        str1 += (str(int1)+oper+str(int2)+'='+str(int1/int2))
        print(int1,oper,int2,'=',int1/int2,sep='')
        list_div.append(str1)
    if oper == '*':
        str1 += (str(int1)+oper+str(int2)+'='+str(int1*int2))
        print(int1,oper,int2,'=',int1*int2,sep='')
        list_mult.append(str1)
    print('+',list_sum)
    print('-',list_dif)
    print('/',list_div)
    print('*',list_mult)
