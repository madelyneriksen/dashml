import typing as t
from functools import singledispatch, partial

from dashml.types import Child, Prop, BuilderCallable, Element
from dashml.clean import safe_children, safe_props

import lxml.html as html
from lxml.builder import E as raw_builder


__all__ = ["_", "render", "unsafe_from_string"]


class Builder:
    """DashML Markup Builder.

    Allows the creation of lxml.html elements via overriding __getattr__.

    >>> _.p("Hello world!")
    """

    def __getattr__(self, attr: str) -> BuilderCallable:
        """Get an attribute."""
        return partial(self.__build, attr)

    def __build(self, tag_name: str, *children: Child, **props: Prop) -> Element:
        """Build an element.

        Arguments:
            tag_name (str): The name of the HTML tag to build.
            children (Child): A list of strings, Elements, or None
        Keyword Arguments:
            properties (Prop): A list of HTML5 properties.
        Returns:
            (Element) An lxml Element.
        """
        tag: BuilderCallable = getattr(raw_builder, tag_name)
        return tag(*safe_children(children), **safe_props(props))


def render(ele: Element) -> str:
    """Render an Element to a string.

    Arguments:
        ele (Element): The element to render.
    Returns:
        (str) Rendered utf-8 string of the element.
    """
    return html.tostring(ele).decode("utf-8")


_ = Builder()


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
