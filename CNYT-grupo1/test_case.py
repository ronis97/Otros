import complejos as c
def test_suma():
    assert c.suma([-3,2],[4,1]) ==  [1,3], 'Debe ser 1 + 3i'
def test_resta():
    assert c.resta([-3,2],[4,1]) == [-7,1], 'Debe ser -7 + i'
def test_producto():
    assert c.multiplicar([-7,3],[-2,3]) == [5,-27], 'Debe ser 5-27i' 
def test_division():
    #print(c.dividir([-7,3],[1,1]))
    assert c.dividir([-7,3],[1,1]) == [-2.0,5.0], 'Debe ser -2 +5i'
def test_conjugado():
    assert c.conjugado([-4,5]) == [-4,-5], 'Debe ser -4-5i'
def test_modulo():
    assert c.modulo([1,1]) == 1.4142135623730951, 'Debe ser 1.4142'
def test_fase():
    assert c.fase_complejo([0,1]) == 1.5707963267948966 ,'Debe ser pi/2'
def test_pasar_a_polar():
    assert c.pasar_a_polar([1,1]) == [1.4142135623730951, 0.7853981633974483], 'Debe ser sqrt(2),pi/4'
 

if __name__ == "__main__":
    test_suma()
    test_producto()
    test_division()
    test_conjugado()
    test_modulo()
    test_fase()
    test_pasar_a_polar()
    print("Prueba exitosa")
