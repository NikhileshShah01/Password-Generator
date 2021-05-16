import random
smaller="abcdefghijklmnopqrstuvwxyz"
captial="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
symbols="-+*&%$!@_."
combine=smaller+captial+numbers+symbols
length=15
password="".join(random.sample(combine,length))
print(password)
