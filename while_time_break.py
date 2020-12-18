import time 

start_time = time.time()

while True:
    now = time.time()
    if now - start_time > 10:
        print("Break!!")
        break
    else:
        print(now)