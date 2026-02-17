class account:
    total = 15000
    def __init__(self,name,id,deposit):
        self.name = name
        self.id = id
        self.deposit = deposit
    def std_name(self,name,id):
        print(f"student name :-{self.name} \nstudent id :-{self.id}")
    @classmethod
    def std_balance(cls,deposit):
        print(f"remaining balance is {cls.total - deposit}")
r1 = account('suraj',456,5500)
print(r1.std_name('suraj',456))
print(r1.std_balance(5500))
        