import typing as t
from functools import singledispatch, partial

from lxml.etree import Element
import lxml.html as html
from lxml.builder import E as raw_builder

import markupsafe


__all__ = ["_", "render"]


T = t.TypeVar("T")


@singledispatch
def safe(var: T) -> T:
    """Mark a value as safe."""
    return var


@safe.register(str)
def _(var: str) -> str:
    """Escape a string."""
    return str(markupsafe.escape(var))


def swap(from_attr: str, to_attr: str, values: t.Dict[str, str]) -> None:
    """Swap values in a dictionary."""
    contained_value = values.pop(from_attr, None)
    if contained_value is not None:
        values[to_attr] = contained_value
    return values


# Like `className` or `htmlFor` in React.
RESERVED_PAIRS = [
    ["class_name", "class"],
    ["html_for", "for"],
]


class Builder:
    """HTML5-aware builder class for Python."""

    def __call__(self, tag: str, *children, **props) -> Element:
        """Direct access based on strings."""
        return self.__build(tag, *children, **props)

    def __getattr__(self, attr: str):
        """Get an attribute."""
        return partial(self.__build, attr)

    def __build(self, tag: str, *children, **props):
        """Build an element."""
        for from_attr, to_attr in RESERVED_PAIRS:
            swap(from_attr, to_attr, props)
        children = list(map(safe, children))
        tag = getattr(raw_builder, tag)
        return tag(*children, **props)


def render(ele: Element) -> str:
    return html.tostring(ele).decode("utf-8")


_ = Builder()
