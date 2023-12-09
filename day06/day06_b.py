import math

# time = 71530
# dist = 940200

time = 49787980
dist = 298118510661181

# dist = (time - t)*t
# dist = -t^2 + t*time
# 0 = -1 tt + time t - dist
a = -1
b = time
c = -dist

D = b*b-4*a*c


x1 = math.ceil ((-b + math.sqrt(D))/(2*a))
x2 = math.floor ((-b - math.sqrt(D))/(2*a))


print(D)
print(x1)
print(x2)

print(x2 - x1 + 1)