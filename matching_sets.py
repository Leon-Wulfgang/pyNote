# The first line contains a single integer, .
# The second line contains space-separated integers describing the respective values of set .
# The third line contains space-separated integers describing the respective values of set .
# Output Format
# Print a single integer denoting the minimum number of operations required to make set equal to set ;
# if no number of operations will ever make the two sets equal, print instead.

n = 3
x = [1, 2, 1, 2, 3, 3]
y = [-1, 4, 4, -1, 3, 3]


sumx = sum(x)
sumy = sum(y)


if sumx != sumy:
    print -1
    exit()

# determine if they have the same sum
print sumx, sumy

# remove elements exist in both
ynew = []
for e in y:
    if e in x:
        x.remove(e)
    else:
        ynew.append(e)
y = ynew
print x
print y

x.sort()
y.sort()

x = x[0:len(x)/2]
y = y[0:len(y)/2]

print x
print y
c = 0
for i in range(0, len(x)):
    c += x[i] - y[i]

print c
exit()

z = []
for i in range(0, len(x)):
    z.append(x[i] - y[i])

print z

i = 0
c = 0
while i < len(x):
    # xi > yi, xi-- x-i++
    if x[i] > y[i]:
        x[i] -= 1
        x[len(x)-1 - i] += 1
        c += 1

    # xi < yi, xi++ x-i--
    elif x[i] < y[i]:
        x[i] += 1
        x[len(x)-1 - i] -= 1
        c += 1

    # xi == yi increment i
    else:
        i += 1

print x
print y
print c