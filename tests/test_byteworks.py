import byteworks
import utility 

def test_float2bits():
    exp = [
        1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 
        0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 
        0, 0, 0, 0, 0, 0, 1, 0]
    bits = byteworks.float_to_bits(3.14159265)
    assert exp == bits

def test_bits2float():
    bts = [
        1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 
        0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 
        0, 0, 0, 0, 0, 0, 1, 0]
    fval = byteworks.bits_to_float(bts)
    assert utility.approx(fval, 3.14159265)

def test_bits2floats():
    bts = [
            1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 
            1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 
            1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 
            1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 
            0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 
            0, 0, 0, 0, 0, 0, 0, 1, 0
        ]
    fvals = byteworks.bits_to_floats(bts)
    assert len(fvals) == 2
    assert utility.approx(fvals[0], 3.14159265)
    assert fvals[0] == fvals[1]


def test_floats2bits():
    a = 4.5
    b = 20.9
    c = 2.71828
    fs = [a, b, c]
    bits = byteworks.floats_to_bits(fs)
    
    assert len(bits) == 32 * len(fs)

    finv = byteworks.bits_to_floats(bits)

    assert len(finv) == len(fs)
    assert utility.approx(finv[0], a)
    assert utility.approx(finv[1], b)
    assert utility.approx(finv[2], c)

