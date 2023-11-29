#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number &lt; 0:
    last_num = number % -10
elif number &gt;= 0:
    last_num = number % 10
if last_num &gt; 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
else:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
