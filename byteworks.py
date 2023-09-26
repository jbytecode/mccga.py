import ctypes 

def float_to_bits(f: float) -> list:
    cf = ctypes.c_float(f)
    cu = ctypes.c_uint32.from_address(ctypes.addressof(cf))
    bts = [(cu.value >> i) & 1 for i in range(32)]
    return bts

def bits_to_float(b: list) -> float: 
    uval = 0
    for i in range(32):
        uval = uval + b[i] * (2 ** i)
    cu = ctypes.c_uint32(uval)
    cf = ctypes.c_float.from_address(ctypes.addressof(cu))
    return cf.value


