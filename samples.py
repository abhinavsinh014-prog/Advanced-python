class account:
    total = 15000
    def __init__(self,name,id,deposit):
        self.name = name
        self.id = id
        self.deposit = deposit

    @classmethod
    def std_balance(cls,deposit):
        print(cls-int(deposit))
r1 = account('suraj',456,5500)
print(r1.std_balance(5500))
        