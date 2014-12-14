
def power(a,b):
    return pow(a,b)
def add(a,b):
    return a+b
def mult(a,b):
    return a*b
def sub(a,b):
    return a-b
def calc(x):    
    a=input('enter first number')
    b=input('enter second number')
    options ={1:power(a,b), 2:add(a,b) ,3 : mult(a,b) ,4: sub(a,b) }
    return options[x]

print calc(1)

