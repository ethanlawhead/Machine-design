import math
P = 300

b = 1
l = 1.25
to = 0.125
ti = 0.25
ei = 10000000
eo =30000000
alphi = 0
alfo = 0
x = l/2
delt = 0
h =0.005

w =math.sqrt((200000/h)*((1/(eo*to))+(2/(ei*ti))))
print(w)

answer = ((P*w)/(4*b*math.sinh((w*l)/2)))*math.cosh(w*x) + (((P*w)/(4*b*math.cosh((w*l)/2)))*(((2*eo*to) -(ei*ti))/((2*eo*to)+(ei*ti))))*math.sinh(w*x)
print(answer)
