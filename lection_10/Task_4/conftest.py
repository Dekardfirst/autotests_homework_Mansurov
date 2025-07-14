import pytest
import time

@pytest.fixture(scope='class')
def class_time(request):
    """
    Фикстура для измерения времени выполнения класса с тестами
    """
    start_time = time.time()
    print(f"\nНачало выполнения класса: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
    yield
    end_time = time.time()
    print(f"\nОкончание выполнения класса: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
    total_time = end_time - start_time
    print(f"\nОбщее время выполнения класса: {total_time:4f} секунд")

@pytest.fixture()
def test_time(request):
    """
    Фикстура для измерения времени выполнения теста
    """
    start_time = time.time()
    print(f"\nНачало выполнения теста: {request.node.name} - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
    yield
    end_time = time.time()
    print(f"\nОкончание выполнения теста: {request.node.name} - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
    total_time = end_time - start_time
    print(f"\nВремя выполнения теста {request.node.name}: {total_time:4f} секунд")