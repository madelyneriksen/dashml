"""Types defined for DashML."""

import typing as t

if t.TYPE_CHECKING:
    from mypy_extensions import VarArg, KwArg  # pragma: no cover
else:
    # Stub out for normal execution.
    VarArg = lambda x: t.List[x]
    KwArg = lambda x: t.Dict[str, x]

from lxml.etree import _Element as Element


__all__ = ["Child", "Prop", "BuilderCallable", "Element"]


Child = t.Union[Element, str, int, float, None]
Prop = t.Union[str, int, float, bool, None]

BuilderCallable = t.Callable[[VarArg(Child), KwArg(Prop)], Element]
