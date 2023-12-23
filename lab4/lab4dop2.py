from ctypes import *
#Made by Kailexi with love to C++

def c_plus_plus_is_better(number):
    # I LOVE THE MANTISSA EXPONENT IMPLENTATION
    #also limits aproximation is of log(1+x) == x is cool i guess
    #1 / 2^23 (M + 2^23 * E) + u  - 127
    #where u - offset
    #IEEE 754 bit manipulatuion funny haha
    #Mr + 2^23 * Eg = 3/2*2**23(127-u) + 1/2 (My + 2^23 * Ey)

    halfs = number * 0.5
    y = c_float(number)

    i = cast(byref(y), POINTER(c_int32)).contents.value  # I'm John Carmak so evil bit manipulation

    #so why works is actually because of adress casting, however this shit doesn't work if it's not an
    #unsigned integer, but let's ignore it for now
    #
    i = c_int32(0x5f3759df - (i >> 1))  # what the fuck
    #bit shifting exponents with signed address bit
    #bit shifting division as well

    #0x5f3759df = 3/2*2**23(127-u) + 1/2 funny address
    y = cast(byref(i), POINTER(c_float)).contents.value

    y = y * (1.5 - (halfs * y * y))
    # newton iterarion funny deriviative haha why works it works because f(x) = 1/y^2 - x
    # if if f(x) = 0;  y = 1/sqrt(x)
    #newton genius i'm not that smart

    return y


print(c_plus_plus_is_better(5.23))
