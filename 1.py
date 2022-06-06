def connect(v1, v2):
    assert isinstance(v1, str)
    assert isinstance(v2, str)

    return v1 + ' ' + v2

print(connect('a', 1))
