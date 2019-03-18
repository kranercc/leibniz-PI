import time
pi = 4
iterations = 0

startTime = time.time()
frequencyOfTheDisplay = 5

history = []

def calculate(times=1):
    global pi,iterations
    den = iterations * 2 +3
    if iterations % 2 == 0:
        pi -= ( 4 / den)
    else:
        pi +=(4 / den)
    iterations+=1
    return pi

while True:
    value = calculate()
    endTime = time.time() - startTime
    if endTime > frequencyOfTheDisplay:
        print("%.30f" % value)
        history.append(value)
        if len(history) == 2:
            compare = history[1] - history[0]
            print("\n\nAfter 5 secounds it's a differtion of %.30f\n\n" % compare)
            history = []
        startTime = time.time()