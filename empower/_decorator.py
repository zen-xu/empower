def impl(target_cls):
    """
    with `impl` decorator you can empower your class without create
    a subclass
    """

    def wrapped(impl_cls):
        for name, method in impl_cls.__dict__.items():
            if name.startswith("_"):
                continue
            setattr(target_cls, name, method)

        if target_cls.__doc__ is None:
            target_cls.__doc__ = ""
        doc = f"<Impl: {impl_cls.__name__}>: {impl_cls.__doc__}"
        target_cls.__doc__ += f"\n{doc}"

    return wrapped
