# +, -, *, /, ** - vozvedenije v stepen'
# unarnqj minus, okruglenije, Pi

a = 5
b = 10
c = a + b
print("c = " + str(c))

d = a - b
print("d = " + str(d))

e = a * b
print("e = " + str(e))

f = a / b
print("f = " + str(f))

g = a ** b
print("g = " + str(g))
# delenije po modulju - %, vozvrashajetsja ostatok
h = 100 % 43
print("h = " + str(h))
# unarnqj minus,
i = 10
i = -i
i = -i
print("i = " + str(i))

# ROUND - okruglenije
x = 7.65
print("x = " + str(round(x)))
# okruglenije v men'shuju storonu
# importirujem modul' math
import math
print("x = " + str(math.floor(x)))
# okruglenije v bol'shuju storonu
y = 7.15
import math
print("y = " + str(math.ceil(y)))
