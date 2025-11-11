class Calculator:
def_init_(self,a, b):
self.a = a
self.b = b 
def get_sum(self):
    return self.a - self.b
def get_difference(self):
    return self.a - self.b
def get_quotient(self):
    return self.a / self.b

#iniaties the calculator
myCalc = Calculator(2,4)

#applies the method get_product
print(myCalc.get_product())
