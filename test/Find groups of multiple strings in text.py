'''import re

f=open(r'C:\Users\16033\Desktop\somefile.txt')
b=f.read()
b=b.lower()
pat='[a-zA-Z]+'
w= re.findall(pat,b)
print(w)
c={}
print(b)
for i in w:
    if i not in c:
            c[i]=1
    else:
            c[i]+=1
print(c)

d=max(c.values())
print(d)
for n in c.keys():
    if c[n]==d:
        print('%s是出现最多次数的单词，次数是%d次' % (n,d))
f.close()

'''
a = int(input("请输入一个整数："))
b = ""
d = a
q = 1
while q:
    if a == 1:
        break
    for i in xrange(2, a + 1):
        if a == i:
            q = 0
            break

        if a % i == 0:
            b += '%s * ' % i
            a = a / i
            break

print("%s = %s%s" % (d, b, a))





