from unittest import result


def urav(a, b, c):
    a = a
    b = b
    c = c
    discr = b**2-4*a*c

    if a==0 and b==0:
        return result

    if discr < 0:
        return result
    elif discr == 0:
        result = -b/2*a
        return result
    else:
        x1 = (-b+discr**0.5)/(2*a)
        x2 = (-b-discr**0.5)/(2*a)
        return x1, x2

urav(1, 2, 3)