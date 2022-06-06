
from colorama import Fore
import string
import random
import time 
amounts = 0

letters = string.ascii_letters
print(f"{Fore.RED}")
while amounts<100:
    print ( ''.join(random.choice(letters) for i in range(15)) )
    amounts+=1
    time.sleep(0.1)
print(f"{Fore.GREEN}")
print ( ''.join(random.choice(letters) for i in range(15)) )
time.sleep(0.5)
print(f"{Fore.WHITE}")
print("Found Wallet!")
