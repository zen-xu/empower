import pytest
from empower import Root, utils


class NormalClass:
    pass


class RootSubClass(Root):
    pass


def test_assert_root_subclass():
    with pytest.raises(AssertionError):
        # will raise
        utils.assert_root_subclass(NormalClass)

    # will not raise
    utils.assert_root_subclass(RootSubClass)
