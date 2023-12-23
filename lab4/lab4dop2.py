from ctypes import c_float, c_int32, cast, byref, POINTER


def c_plus_plus_is_better(number):


    threehalfs = 1.5
    x2 = number * 0.5
    y = c_float(number)


    i = cast(byref(y), POINTER(c_int32)).contents.value # I'm John Carmak so evil bit manipulation

    i = c_int32(0x5f3759df - (i >> 1)) # what the fuck
    y = cast(byref(i), POINTER(c_float)).contents.value

    y = y * (1.5 - (x2 * y * y)) # newton iterarion funny deriviative haha why works

    return y


print(c_plus_plus_is_better(5.23))



