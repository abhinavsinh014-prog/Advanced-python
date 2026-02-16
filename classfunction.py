# class operators:
#     def sum(self,a,b):
#         return a+b
#     def subs(self,a,b):
#         return a-b
#     def multiple(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
# op =operators()
# print('Sum',op.sum(4,5))
# print('Substract',op.subs(4,5))
# print('mulriple',op.multiple(4,5))
# print('divison',op.div(4,5))

# class test:
#     x = 5
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def show(self):
#         print(self.a,self.b)
#     @staticmethod
#     def static():
#         print('hello')
#     @classmethod
#     def classes(cls):
#         print(cls.x)
# t1 = test(4,9)
# t2 = test(5,3)
# t1.show()
# test.static()
# test.classes()
# # print(t1.a*t1.b)
# # print(t2.a+t2.b)

class employee:
    def __init__(self,name=None,enrid=None,salary=None):
        self.name = name
        self.enrid = enrid
        self.salary = salary
    def setname(self,name):
        self.name = name
    def setenrid(self,enrid):
        self.enrid = enrid
    def setsalary(self,salary):
        self.salary = salary
    def fulldetail(self):
        return ("{enrid}. {name},{salary}")
e1 = employee('oggy',6,156)
e2 = employee()
print(e2.setname('jack'))
print(e2.setenrid(5))
print(e2.setsalary(158))
print(e2.fulldetail)