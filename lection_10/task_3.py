# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize("params, result",[((10, 0), ZeroDivisionError),
                                           pytest.param((100, 10), 10, marks=pytest.mark.smoke),
                                           pytest.param((-100, -10), 10, marks=pytest.mark.skip('Ошибка в приемочных тестах, не будет правиться в эту веху. Согласовано тут: ссылка')),
                                           ((100, -10), -10),
                                           ((1000000, 1000), 1000)])
def test_all_divisions(params, result):
    if result == ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            all_division(*params)
    else:
        assert all_division(*params) == result