class operators:
    def sum(self,a,b):
        return a+b
    def subs(self,a,b):
        return a-b
    def multiple(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
op =operators()
print('Sum',op.sum(4,5))
print('Substract',op.subs(4,5))
print('mulriple',op.multiple(4,5))
print('divison',op.div(4,5))

class test:
    def __init__(self):
        self.a =5
        self.b = 6
t1 = test()
t2 = test()
print(t1.a,t1.b)
print(t1.a+t2.b)