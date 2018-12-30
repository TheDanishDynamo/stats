import random
h = t = 0
for i in range(1,1000001):
    if random.choice(['heads','tails']) == 'heads':
        h = h + 1
    else:
        t = t + 1
print ('h', str(round((h / 1000000.0) * 100.0, 3)) + '%')
print ('t', str(round((t / 1000000.0) * 100.0, 3)) + '%')
