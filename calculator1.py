#Calculator v1
#peremennaja what
what = input("What do we do? (+ or -): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if what == "+":
    c = a + b
    print("Result: " + str(c))
elif what == "-":
    c = a - b
    print("Result: " + str(c))
else:
    print("Wrong operation!")
