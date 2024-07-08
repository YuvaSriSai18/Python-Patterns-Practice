import random
bet = int(input("Your bet from 1 to 10 : "))
lucky_draw = random.randint(1,10)
account = 0
if(bet == lucky_draw):
    account = account + 900 - 100
else:
    account = account - 100
print(account)
print(lucky_draw)