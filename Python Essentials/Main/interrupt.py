from time import sleep
 
seconds = 0
 
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Bye")
        break
