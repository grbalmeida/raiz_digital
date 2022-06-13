from raiz_digital import raiz_digital

def test_deve_retornar_numero_se_menor_que_10():
    assert raiz_digital(1) == 1
    assert raiz_digital(2) == 2
    assert raiz_digital(3) == 3
    assert raiz_digital(4) == 4
    assert raiz_digital(5) == 5
    assert raiz_digital(6) == 6
    assert raiz_digital(7) == 7
    assert raiz_digital(8) == 8
    assert raiz_digital(9) == 9

def test_deve_retornar_raiz_digital_igual_a_1():
    assert raiz_digital(451) == 1
    assert raiz_digital(91) == 1
    assert raiz_digital(19) == 1
    assert raiz_digital(22222) == 1
    assert raiz_digital(442) == 1

def test_deve_retornar_raiz_digital_igual_a_2():
    assert raiz_digital(443) == 2
    assert raiz_digital(551) == 2
    assert raiz_digital(1037) == 2

def test_deve_retornar_raiz_digital_igual_a_3():
    assert raiz_digital(975) == 3

def test_deve_retornar_raiz_digital_igual_a_9():
    assert raiz_digital(18) == 9
    assert raiz_digital(36) == 9
    assert raiz_digital(243) == 9
    assert raiz_digital(7587) == 9

def test_deve_retornar_raiz_digital_igual_a_6_para_24():
    assert raiz_digital(24) == 6

def test_deve_retornar_raiz_digital_igual_a_8_para_143():
    assert raiz_digital(143) == 8

def test_deve_retornar_raiz_digital_igual_a_9_para_51111():
    assert raiz_digital(51111) == 9

def test_deve_retornar_raiz_digital_igual_a_2_para_87482():
    assert raiz_digital(87482) == 2