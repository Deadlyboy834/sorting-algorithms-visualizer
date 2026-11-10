from functools import wraps
from typing import ParamSpec, TypeVar, Generic, Callable

P = ParamSpec("P")
R = TypeVar("R")

class RepresentationCallable(Generic[P, R]):
    def __init__(
            self,
            func: Callable[P, R],
            repr_str: str | None = None
    ) -> None:
        self.func: Callable[P, R] = func
        self.repr_str = repr_str or f"<Function: {func.__name__}"
        wraps(func)(self)

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        return self.func(*args, **kwargs)

    def __repr__(self) -> str:
        return self.repr_str

def with_repr(repr_str: str) -> Callable[[Callable[P, R]], RepresentationCallable[P, R]]:
    def decorator(func: Callable[P, R]) -> RepresentationCallable[P, R]:
        return RepresentationCallable[P, R](func, repr_str)

    return decorator