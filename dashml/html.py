"""Functions for exporting DashML to (or importing from) raw HTML.

The most notable function here is `render()`, which takes a DashML element
as an argument and returns an HTML representation of it.

>>> from dashml import _, render
>>> render(_.p("Hello world!"))
'<p>Hello world!</p>'

Additionally, the method `unsafe_from_string` exists here to transform
trusted HTML strings into DashML/lxml Element instances. Use this great
unsafe power responsibly!
"""


import lxml.html as html

from dashml.types import Element


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
