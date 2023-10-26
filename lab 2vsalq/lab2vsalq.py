a=[0]*int(input('Elementlerin sayi: '))
k=1
for i in range(len(a)):
    a[i]=int(input())
print('A:',a)
for x in a:
    if x > 9:
        print(x)
        k=k*x
print(k)
