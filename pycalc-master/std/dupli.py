sdfadsfdassads

sdfsdasfsaf

sdfsafdsfs

SDFsfsdfsd

sdfasfsadf

def _as_list(func: Callable) -> Callable[[Callable, Iterable], list]:
    def decorator(a: Callable, b: Iterable) -> list:
        return list(func(a, b))

    return decorator
