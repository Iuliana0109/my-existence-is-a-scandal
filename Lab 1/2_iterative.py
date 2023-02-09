#iterative method
import time

def fib(n):
  n1 = 0
  n2 = 1
  for _ in range(0 , n):
    n1 = n2
    n2 = n1 + n2
  return n1

start1 = time.time()
fib(1)
end1 = time.time()

start2 = time.time()
fib(5)
end2 = time.time()

start3 = time.time()
fib(10)
end3 = time.time()

start4 = time.time()
fib(15)
end4 = time.time()

start5 = time.time()
fib(20)
end5 = time.time()

start6 = time.time()
fib(25)
end6 = time.time()

start7 = time.time()
fib(30)
end7 = time.time()

start8 = time.time()
fib(35)
end8 = time.time()

start9 = time.time()
fib(40)
end9 = time.time()

start10 = time.time()
fib(45)
end10 = time.time()

start11 = time.time()
fib(50)
end11 = time.time()

x = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y = [end1 - start1, end2 - start2, end3 - start3, end4 - start4, end5 - start5, end6 - start6, end7 - start7, end8 - start8
     , end9 - start9, end10 - start10, end11 - start11]
plt.plot(x, y, marker='o')
plt.title('Iterative implementation')
plt.show()