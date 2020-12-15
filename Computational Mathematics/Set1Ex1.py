import math as m

#define the function as given in the instactions
fa= lambda x: m.exp(x)-2*x*m.cos(x)-3 #x[0,2]
fb= lambda x: pow(x,2)-m.sin(x)+m.exp(x)-2 #x[0,1]
dfa= lambda x: m.exp(x)-2*m.cos(x)+2*x*m.sin(x)
dfb= lambda x: 2*x-m.cos(x)+m.exp(x)

i_ba=0; i_nra=0

#bisection method for fa
x1=0; x2=2
while (abs(x2-x1)>0.0005):
    i_ba=i_ba+1
    x3=(x1+x2)/2
    if fa(x1)*fa(x3)<0:
        x2=x3
    elif fa(x1)*fa(x3)>0:
        x1=x3
    else:
        break
print('bisection fa: %.4f' %x3,'\n iterations:',i_ba)

#Newton-Raphson method for fa
x1=0; e_a=1
while (e_a>0.0005):
    i_nra=i_nra+1
    x2=x1-(fa(x1)/dfa(x1))
    e_a=abs(fa(x1)/dfa(x1))
    x1=x2
print('Newton-Raphson fa: %.4f' %x2,'\n iterations:',i_nra)


i_bb=0; i_nrb=0

#bisection method for fb
x1=0; x2=1
while (abs(x2-x1)>0.0005):
    i_bb=i_bb+1
    x3=(x1+x2)/2
    if fb(x1)*fb(x3)<0:
        x2=x3
    elif fb(x1)*fb(x3)>0:
        x1=x3
    else:
        break
print('bisection fb: %.5f' %x3,'\n iterations:',i_bb)

#Newton-Raphson method for fb
x1=0.5; e_a=1
while (e_a>0.0005):
    i_nrb=i_nrb+1
    x2=x1-(fb(x1)/dfb(x1))
    e_a=abs(fb(x1)/dfb(x1))
    x1=x2
print('Newton-Raphson fb: %.5f' %x2,'\n iterations:',i_nrb)
