import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

a = float(input("Please input a positive number: "))

x = 0.0
epsilon = 0.1
numGuesses = 1
memsave = []

if a < 1:
    epsilon = 0.001
    min = a
    max = 1.0
    mem = [0, 0, 0]
    while abs(x ** 2 - a) >= epsilon:
        x = min + (max - min) / 2
        memsave.append([min, x, max])
        numGuesses += 1
        if (x ** 2 > a):
            max = x
        else:
            min = x
        if mem == [min, x, max]:
            break
        else:
            mem = [min, x, max]
else:
    min = 1.0
    max = a
    mem = [0, 0, 0]
    while abs(x ** 2 - a) >= epsilon:
        x = min + (max - min) / 2
        memsave.append([min, x, max])
        numGuesses += 1
        if (x ** 2 > a):
            max = x
        else:
            min = x
        if mem == [min, x, max]:
            break
        else:
            mem = [min, x, max]


fig = plt.figure(figsize=(10,6))
plt.xlim(0, numGuesses-2)
if a > 1:
    plt.ylim(1, a)
    #plt.yscale("log")
else:
    plt.ylim(a,1)
plt.xlabel('iteration',fontsize=20)
plt.ylabel('bounds',fontsize=20)
plt.title('finding the square root of ' + str(a),fontsize=20)

df = pd.DataFrame(np.array(memsave), columns=['min', 'x', 'max'])

def animate(i):
    data = df.iloc[:int(i+1)] #select data range
    plt.plot(data['min'], 'ro-', data['max'], 'bo-', data['x'], 'go-')
    plt.legend(('min', 'max', 'x'), loc='upper right')
    if i==numGuesses-2:
        plt.text(i+0.01*i, x, str(round(x,2)))

ani = matplotlib.animation.FuncAnimation(fig, animate, frames=numGuesses-1, repeat=False)
#animate(numGuesses-2)        
plt.show()