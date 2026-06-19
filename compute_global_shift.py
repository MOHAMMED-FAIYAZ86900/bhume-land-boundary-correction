# compute_global_shift.py

shifts = [
(-0.00010719, 0.00005062),
(-0.00005793, 0.00007898),
(-0.00014479, 0.00008848),
( 0.00002682, 0.00016609),
(-0.00002778, 0.00016135),
( 0.00000529, 0.00011587),
]

dx = sum(x for x,y in shifts)/len(shifts)
dy = sum(y for x,y in shifts)/len(shifts)

print(dx)
print(dy)