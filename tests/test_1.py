import pytest


class TestSuiteInt:

    @pytest.mark.parametrize("value", [-1, 0, 1])
    def test_positive_value(self, value):
        """Positive int values"""
        assert isinstance(value, int)

    @pytest.mark.parametrize("value", [1.1, '1.1',
                                       [1.1], {1: "1.1"},
                                       (1.1), {1}
                                       ])
    def test_negative_value(self, value):
        """Negative int values"""
        assert not isinstance(value, int)

    @pytest.mark.parametrize('value', [[1.1, 1], {1: "1.1"},
                                       (1.1, 1), {1, 1}
                                       ])
    def test_negative_transform(self, value):
        """Negative cast to int"""
        with pytest.raises(TypeError):
            result = int(value)


class TestSuiteDict:

    @pytest.mark.parametrize("value", [{"dict": 1}, dict([("dict", 1)]),
                                       dict.fromkeys(['dict', 1]),
                                       {a: a ** 2 for a in range(7)}
                                       ])
    def test_positive_create(self, value):
        """Positive vocabulary building methods"""
        assert isinstance(value, dict)

    def test_non_existent_elem(self):
        """Negative retrieval of an element
        from a dictionary"""
        d = {1: True}
        with pytest.raises(KeyError):
            result = d[3]

    def test_existent_elem(self):
        """Positive retrieval of an element
        from a dictionary"""
        d = {1: True}
        result = d[1]
        assert result
