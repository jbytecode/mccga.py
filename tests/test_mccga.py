import optimizer
import utility 

def test_sample():
    probs = [1.0, 1.0, 0.0, 0.0]
    bits = optimizer.sample(probs)
    assert bits[0] == 1
    assert bits[1] == 1
    assert bits[2] == 0
    assert bits[3] == 0

def test_update():
    probs = [0.5, 0.5, 0.5, 0.5]
    winner = [1, 1, 0, 0]
    loser  = [0, 0, 1, 1]
    mutrate = 0.01
    optimizer.update(probs, winner, loser, mutrate)
    assert probs[0] == 0.5 + mutrate 
    assert probs[1] == 0.5 + mutrate 
    assert probs[2] == 0.5 - mutrate 
    assert probs[3] == 0.5 - mutrate 

def test_mccga_for_f():
    myeps = 0.00001
    f = utility.f
    result = optimizer.mccga(f, [-100.0, -100.0], [100.0, 100.0], 0.001, 100000)
    assert len(result) == 2
    assert utility.approx(result[0], 3.14159265, eps = myeps)
    assert utility.approx(result[1], 2.71828, eps=myeps)
    
def test_mccga_for_g():
    myeps = 0.00001
    g = utility.g
    result = optimizer.mccga(g, [-1000.0, -1000.0, -1000.0], [1000.0, 1000.0, 1000.0], 0.001, 1000000)
    assert len(result) == 3
    assert utility.approx(result[0], 7.0, eps = myeps)
    assert utility.approx(result[1], 77.0, eps=myeps)
    assert utility.approx(result[2], 777.0, eps=myeps)