from src.c11.tiy_11_1 import city_functions


def test_city_country():
    formatted_name = city_functions('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'
