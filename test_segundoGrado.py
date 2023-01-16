from segundoGrado import raices, Sin_raices
from pytest import raises


def test_raice():
    # if not (raices(1, -4, 0) == (0,4)):
    #     raices Exception
    
    assert (raices(1, -4, 0) == (4.0,0.0))
    assert (raices(1, 0, 0) == (0.0,0.0))
    with raises(Sin_raices):
        raices(0,0,0)