import typing as t
from functools import singledispatch, partial

if t.TYPE_CHECKING:
    from mypy_extensions import VarArg, KwArg

from lxml.etree import Element
import lxml.html as html
from lxml.builder import E as raw_builder

import markupsafe


__all__ = ["_", "render"]


T = t.TypeVar("T")

# Like `className` or `htmlFor` in React.
RESERVED_PAIRS = [
    ["class_name", "class"],
    ["html_for", "for"],
]


Child = t.Union[Element, str]


class Builder:
    """HTML5-aware builder class for Python."""

    def __getattr__(
        self, attr: str
    ) -> t.Callable[[VarArg(Child), KwArg(t.Any)], Element]:
        """Get an attribute."""
        return partial(self.__build, attr)

    def __build(self, tag_name: str, *children: Child, **props: t.Any) -> Element:
        """Build an element."""
        for from_attr, to_attr in RESERVED_PAIRS:
            swap(from_attr, to_attr, props)

        safe_children = list(map(safe, children))

        tag = getattr(raw_builder, tag_name)
        return tag(*safe_children, **props)


def render(ele: Element) -> str:
    raw: bytes = html.tostring(ele)
    return raw.decode("utf-8")


_ = Builder()


@singledispatch
def safe(var: T) -> T:
    """Mark a value as safe."""
    return var


@safe.register
def __safe_string(var: str) -> str:
    """Escape a string."""
    return str(markupsafe.escape(var))


def swap(from_attr: str, to_attr: str, values: t.Dict[str, str]) -> None:
    """Swap values in a dictionary."""
    contained_value = values.pop(from_attr, None)
    if contained_value is not None:
        values[to_attr] = contained_value
