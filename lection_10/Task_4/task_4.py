# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest

class TestMathOperations:

    @pytest.mark.usefixtures("class_time")
    def test_addition(self):
        assert 2 + 2 == 4

    def test_multiplication(self):
        assert 3 * 5 == 15

    @pytest.mark.usefixtures("test_time")
    def test_type_check(self, test_time):
        assert isinstance(10, int)

    def test_division(self):
        assert 100 / 10 == 10