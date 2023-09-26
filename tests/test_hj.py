import hookejeeves
import utility 


def test_hj_for_f():
    f = utility.f
    result = hookejeeves.hj(f, [0.0, 0.0], 100000, 500, 0.000001)
    assert len(result) == 2
    assert utility.approx(result[0], 3.14159265)
    assert utility.approx(result[1], 2.71828)
    
def test_hj_for_g():
    g = utility.g
    result = hookejeeves.hj(g, [0.0, 0.0, 0.0], 100000, 500, 0.000001)
    assert len(result) == 3
    assert utility.approx(result[0], 7.0)
    assert utility.approx(result[1], 77.0)
    assert utility.approx(result[2], 777.0)
