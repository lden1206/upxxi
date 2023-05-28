num1 = input('num = ')
num2 = num1.replace('[','')
num3 = num2.replace(']','')
num4 = num3.split(',')
num = list(map(int, num4))
target = int(input('target = '))
op = []
for c in num:
    x = target - c
    if x == c:
        if num.count(x) < 2:
            continue
        else:
            op.append(num.index(c))
            num.remove(c)
            op.append(num.index(x) + 1)
            break
    if x in num:
        op.append(num.index(c))
        op.append(num.index(x))
        break
print(op)