def power(x, y):
    
    if y == 0 or x == 1:
        return 1
    if x == 0:
        return 0

    if y >= 1:
        return x*power(x, y-1)

    y = abs(y)
    return 1/(y*power(x, y-1))


if __name__ == '__main__':
    print(power(-6, 5))