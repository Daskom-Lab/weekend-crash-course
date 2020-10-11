c=[];b=0
while 1:
    d=input()
    b+=d.count(" ")
    if d:c+=d,
    else:break
if('\n'.join(c).count("\n")-1)**2!=b:print("non-",end='')
print("symmetrical")