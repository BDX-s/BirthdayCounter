from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

h = int(now.strftime("%H"))
m = int(now.strftime("%M"))
s = int(now.strftime("%S"))

ht = h * 6133
mt = ht * m
st = mt * s

