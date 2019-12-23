import typing as t
from functools import partial

import lxml.html as html

from dashml.builder import Builder
from dashml.clean import safe_children, safe_props
from dashml.types import Child, Prop, BuilderCallable, Element


__all__ = ["_", "render", "unsafe_from_string"]


_ = Builder()


def render(ele: Element) -> str:
    """Render an Element to a string.

    Arguments:
        ele (Element): The element to render.
    Returns:
        (str) Rendered utf-8 string of the element.
    """
    return html.tostring(ele).decode("utf-8")


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
