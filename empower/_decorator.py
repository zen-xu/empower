from .utils import assert_root_subclass


def impl(target_cls):
    """
    with `impl` decorator you can empower your class without create
    a subclass
    """

    assert_root_subclass(target_cls)

    def wrapped(impl_cls):
        assert_root_subclass(target_cls)
        target_cls.__bases__ = (impl_cls, *target_cls.__bases__)

        if target_cls.__doc__ is None:
            target_cls.__doc__ = ""
        doc = f"<Impl: {impl_cls.__name__}>: {impl_cls.__doc__}"
        target_cls.__doc__ += f"\n{doc}"

    return wrapped
