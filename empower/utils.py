from ._class import Root


def assert_root_subclass(cls):
    assert issubclass(cls, Root), f"{cls} is not sublass of `Root`"
