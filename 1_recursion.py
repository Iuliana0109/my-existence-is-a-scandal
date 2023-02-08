#recursive method

import time
import matplotlib.pyplot as plt
start = time.time()

def fib(n):
  if n==0:
    return 0;
  elif n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

fib(1)
end1 = time.time()

fib(5)
end2 = time.time()

fib(10)
end3 = time.time()

fib(15)
end4 = time.time()

fib(20)
end5 = time.time()

fib(25)
end6 = time.time()

fib(30)
end7 = time.time()

fib(35)
end8 = time.time()

fib(40)
end9 = time.time()

fib(45)
end10 = time.time()

fib(50)
end11 = time.time()

x = [1, 5, 10, 15, 20, 25, 35, 40, 45, 50]
y = [end1 - start, end2 - start, end3 - start, end4 - start, end5 - start, end6 - start, end7 - start, end8 - start
     , end9 - start, end10 - start]
plt.plot(x, y, marker='o')
plt.title('Recursive implementation')
plt.show()