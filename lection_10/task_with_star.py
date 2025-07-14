# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test(request):
    marker = request.node.get_closest_marker("id_check")
    if marker:
        print(f"id_check: {', '.join(map(str, marker.args))}")
    else:
        print("Маркер id_check не найден")
    assert True
