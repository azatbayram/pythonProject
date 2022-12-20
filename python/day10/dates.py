import datetime

x=datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

y=datetime.datetime(2022, 5, 17)
print(y.year)
print(y.strftime("%B"))
 