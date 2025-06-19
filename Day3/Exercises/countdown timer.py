import time

countdown = int(input("Set a time in seconds: "))

for i in range(countdown, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("BEEP BEEP BEEP")