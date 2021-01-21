import time


# no flush
for i in range(10):
    print(i, end=' ')
    time.sleep(0.5)

# has flush
for i in range(10):
    print(i, end=' ', flush=True)
    time.sleep(0.5)
