# DEVISE AN EXPERIMENT TO VERIFY THAT GET ITEM AND SET ARE O(1) FOR DICTIONARIES

import timeit
import random

for i in range(10000,1000001,20000):
    t = timeit.Timer("x[choice]",
                     "from __main__ import x, choice")
    x = {j:None for j in range(i)}
    choice = random.choice(list(x.keys()))
    d_time = t.timeit(number=1000)
    print("Get operation", d_time, "milliseconds")

for i in range(10000,1000001,20000):
    t = timeit.Timer("x[choice] = 5",
                     "from __main__ import x, choice")
    x = {j:None for j in range(i)}
    choice = random.choice(list(x.keys()))
    d_time = t.timeit(number=1000)
    print("Set operation", d_time, "milliseconds")