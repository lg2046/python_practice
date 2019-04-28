from queue import PriorityQueue

q = PriorityQueue()

q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

print(q.get())  # (1, 'eat')
print(q.get())  # (2, 'code')
print(q.get())  # (3, 'sleep')
