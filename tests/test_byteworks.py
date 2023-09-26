import byteworks

def approx(a, b, eps = 0.00001):
    return abs(a-b) <= eps

def test_float2bits():
    exp = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
            0, 1, 0]
    bits = byteworks.float_to_bits(3.14159265)
    assert exp == bits

def test_bits2float():
    bts = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
            0, 1, 0]
    fval = byteworks.bits_to_float(bts)
    assert approx(fval, 3.14159265)
