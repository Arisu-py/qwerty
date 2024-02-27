x, y, k, h = map(int, input().split())
x1, y1, k1, h1 = map(int, input().split())
if y > y1 or x > x1:
    y, y1 = y1, y
    x, x1 = x1, x
    h = h1
    k = k1
if (x + k - x1 > 0 and y1 <= y + h) or (y + h - y1 > 0 and x1 <= x + k):
    print("YES")
else:
    print("NO")
