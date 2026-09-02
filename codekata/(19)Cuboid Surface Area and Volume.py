l, b, h = map(int, input().split())
total_surface=2*(l*b+b*h+h*l)
volume=l*b*h
print(total_surface,volume)