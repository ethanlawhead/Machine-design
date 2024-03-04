import math
d = .085
D = 1-d-.05


alpha = 0.5
m = 0.145
g = 11.75*(10**6)
e = 28.5*(10**6)
A = 201000
z = 0.15
ns = 2
lnot = 4
sf = 1.2
f = 20
y = 2
k = f/y

sut = A/(d**m)
c = D/d
kb = ((4*c)+2)/((4*c)-3)
print(d,"in")
print("c",c)
print(kb)

tou = kb* ((8*(1+z)*f*D)/(math.pi*(d**3)))
print(tou)

ssy = 0.45*sut
print(ssy)

na = ((d)*g)/(8*k*(c**3))
print("na",na)

locrit = 2.63*(D/alpha)
print(locrit)

nt = na + 2
ls = d * nt
ns =ssy/tou
if ns >= 1.2:
    print('ns good')
else: 
    print('ns bad')
if ls > 1.5:
    print("ls bad")
else:
    print("ls good")
lnot = ls + (1+z)*y
print("lo",lnot)

fom = -((math.pi**2)*(d**2)*nt*D)/4
print("fom",fom)