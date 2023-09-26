import ctypes


def float_to_bits(f: float) -> list[int]:
    cf = ctypes.c_float(f)
    cu = ctypes.c_uint32.from_address(ctypes.addressof(cf))
    bts = [(cu.value >> i) & 1 for i in range(32)]
    return bts


def bits_to_float(b: list[int]) -> float:
    uval = 0

    for i in range(32):
        uval = uval + b[i] * (2**i)

    cu = ctypes.c_uint32(uval)
    cf = ctypes.c_float.from_address(ctypes.addressof(cu))
    return cf.value


def floats_to_bits(fs: list[float]) -> list[int]:
    bitlist = []

    for f in fs:
        bitlist = bitlist + float_to_bits(f)

    return bitlist


def bits_to_floats(b: list[int]) -> list[float]:
    bitsize = len(b)
    floatssize = int(bitsize / 32)
    floatvector = [0.0] * floatssize
    index = 0
    findex = 0

    while index + 32 <= bitsize:
        part = b[index : (index + 32)]
        floatvector[findex] = bits_to_float(part)
        index = index + 32
        findex += 1

    return floatvector
