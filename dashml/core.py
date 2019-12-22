import typing as t
from functools import singledispatch, partial

if t.TYPE_CHECKING:
    from mypy_extensions import VarArg, KwArg  # pragma: no cover
else:
    # Stub out for normal execution.
    VarArg = lambda x: t.List[x]
    KwArg = lambda x: t.Dict[str, x]

from lxml.etree import Element
import lxml.html as html
from lxml.builder import E as raw_builder

import markupsafe


__all__ = ["_", "render"]


T = t.TypeVar("T")


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
        swap_attributes(props)
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
    return str(markupsafe.escape(var))  # pragma: no cover


# Like `className` or `htmlFor` in React.
RESERVED_PAIRS = {
    "class_name": "class",
    "html_for": "for",
}


def swap_attributes(attrs: t.Dict[str, str]) -> None:
    """Swap attribute values passed in as kwargs.

    This changes snake_case to use dashes for HTML, as well as doing swaps for
    class_name and html_for.
    """
    for key, value in attrs.items():
        if key.startswith("data_") or key.startswith("aria_"):
            attrs[key.replace("_", "-")] = attrs.pop(key)
        elif key in RESERVED_PAIRS:
            attrs[RESERVED_PAIRS[key]] = attrs.pop(key)
