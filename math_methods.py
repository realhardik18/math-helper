def lin_in_2_var(a):#code contributed by dbamogh
    a1, a2 = a.split(',')
    a1 = a1.replace('+', ',')
    a1 = a1.replace('-', ',-')
    a1 = a1.replace(' ', '')
    a1 = a1.replace('x','')
    a1 = a1.replace('y', '')
    a1 = a1.split(',')
    a2 = a2.replace('+', ',')
    a2 = a2.replace('-', ',-')
    a2 = a2.replace(' ', '')
    a2 = a2.replace('x', '')
    a2 = a2.replace('y', '')
    a2 = a2.split(',')
    if a1[0] == '':
        a1[0] ='1'
    if a1[0] == '-':
        a1[0] = '-1'
    if a1[1] == '':
        a1[1] ='1'
    if a1[1] == '-':
        a1[1] = '-1'
    if a1[2] == '':
        a1[2] ='1'
    if a1[2] == '-':
        a1[2] = '-1'
    if a2[0] == '':
        a2[0] ='1'
    if a2[0] == '-':
        a2[0] = '-1'
    if a2[1] == '':
        a2[1] ='1'
    if a2[1] == '-':
        a2[1] = '-1'
    if a2[2] == '':
        a2[2] ='1'
    if a2[2] == '-':
        a2[2] = '-1'
    if int(a1[0]) / int(a2[0]) == int(a1[1]) / int(a2[1]) == int(a1[2] / int(a2[2])):
        print('there are infinite solutions since its a co-incedent line')
    if int(a1[0]) / int(a2[0]) == int(a1[1]) / int(a2[1]) != int(a1[2] / int(a2[2])):
        print('there are no solutions since the lines are parralel')
    t1 = a1[0]
    t2 = a1[1]
    t3 = a1[2]
    a1 = int(t1)
    b1 = int(t2)
    c1 = int(t3)
    t4 = a2[0]
    t5 = a2[1]
    t6 = a2[2]
    a2 = int(t4)
    b2 = int(t5)
    c2 = int(t6)
    xhalf1 = (b1*c2)-(b2*c1)
    xhalf2 = (a1*b2)-(a2*b1)
    x = xhalf1 / xhalf2
    yhalf1 = (c1*a2)-(c2*a1)
    yhalf2 = (a1*b2)-(a2*b1)
    y = yhalf1 / yhalf2
    y = int(y)
    x = int(x)
    result=f"the value of x is {str(x)} and the value of y is {str(y)}"
    return result

def add(vals):
    val_split=vals.split()
    return sum(val_split)