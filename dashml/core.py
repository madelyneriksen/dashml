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


__all__ = ["_", "render", "unsafe_from_string"]


T = t.TypeVar("T")


Child = t.Union[Element, str, None]
Prop = t.Union[str, int, bool, None]


class Builder:
    """DashML Markup Builder.

    Allows the creation of lxml.html elements via overriding __getattr__.

    >>> _.p("Hello world!")
    """

    def __getattr__(
        self, attr: str
    ) -> t.Callable[[VarArg(Child), KwArg(t.Any)], Element]:
        """Get an attribute."""
        return partial(self.__build, attr)

    def __build(self, tag_name: str, *children: Child, **props: Prop) -> Element:
        """Build an element.

        Arguments:
            tag_name: (str) The name of the HTML tag to build.
            children: (Child) A list of strings, Elements, or None
        Returns:
            element: (Element) An lxml Element.
        """
        swap_attributes(props)
        safe_children: t.List[Child] = [safe(x) for x in children if x is not None]

        tag: t.Callable[[VarArg(Child), KwArg(Prop)], Element] = getattr(
            raw_builder, tag_name
        )
        return tag(*safe_children, **props)


def render(ele: Element) -> str:
    """Render an Element to a string.

    Arguments:
        ele (Element): The element to render.
    Returns:
        (str) Rendered utf-8 string of the element.
    """
    raw: bytes = html.tostring(ele)
    return raw.decode("utf-8")


_ = Builder()


@singledispatch
def safe(var: Child) -> Child:
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


def swap_attributes(attrs: t.Dict[str, Prop]) -> None:
    """Swap attribute values passed in as kwargs.

    This changes snake_case to use dashes for HTML, as well as doing swaps for
    class_name and html_for.
    """
    for key, value in attrs.items():
        if key.startswith("data_") or key.startswith("aria_"):
            attrs[key.replace("_", "-")] = attrs.pop(key)
        elif key in RESERVED_PAIRS:
            attrs[RESERVED_PAIRS[key]] = attrs.pop(key)


def unsafe_from_string(unsafe_string: str) -> Element:
    """UNSAFE: Create an element from a string, skipping escaping.

    HTML will _not_ be escaped by this function, so using it with an untrusted
    string is a security vulnerability and could allow XSS attacks!

    Arguments:
        unsafe_string (str): A string to convert to an element.
    Returns:
        (Element) The converted element
    """
    return html.fromstring(unsafe_string)
