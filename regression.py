#
def intercept(x, y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    xx = [a*a for a in x]
    xy = []
    i = 0;
    while i < n:
        xy.append(x[i]*y[i])
        i += 1
    sxy = sum(xy)
    sxx = sum(xx)
    numerator = (sy*sxx)-(sx*sxy)
    denominator = (n*sxx)-(sx*sx)
    answer = numerator/denominator
    return answer

def slope(x, y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    xx = [a*a for a in x]
    xy = []
    i = 0;
    while i < n:
        xy.append(x[i]*y[i])
        i += 1
    sxy = sum(xy)
    sxx = sum(xx)
    numerator = (n*sxy)-(sx*sy)
    denominator = (n*sxx)-(sx*sx)
    answer = numerator/denominator
    return answer

x = [26.6, 17.85, 20.3, 16.8, 20.8, 16.7, 19.1, 18.9, 16.0, 15.8]
y = [28.9, 19.2, 26.4, 13.7, 20.2, 18.8, 25.0, 21.0, 16.8, 15.3]

a = intercept(x, y)
b = slope(x, y)
print(a)
print(b)
print(a+b*25)
print(sum(y)/len(y))
