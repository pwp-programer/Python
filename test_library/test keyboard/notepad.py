from time import sleep

import keyboard as board

for i in range(1, 6):
    sleep(1)
    print(i)
    i += 1

for i in range(1000, 1, -7):
    board.write(str(f"{i} - 7 = {i - 7}"),
                delay=0.000000000000000000000000000000000000000000000000000000000000000005)
    board.send("Enter")
