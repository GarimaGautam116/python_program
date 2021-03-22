n=input('Enter the number')

ln=len(a)
s=0
i=0
while i<ln:
    s += a[i]**ln
    i += 1
if int(a)== s:
    print('number is armstrong')
else:
    print('not armstrong')
