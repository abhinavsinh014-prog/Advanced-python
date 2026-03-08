# adding values by using list function
tupel = (117,49,254,914,157,83,82)
a,b = 14,15
print(a+b)
typlr = list(tupel)
typlr.append(160)
print(typlr,type(typlr))
tupel = tuple(typlr)
print(tupel,type(tupel))
tupel = len(typlr)
print(tupel,type(tupel))