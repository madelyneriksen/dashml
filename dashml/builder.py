"""Builder module.

This is the class behind the main `_` object exported by DashML. The builder
is basically a few utilities wrapped around an lxml element factory, for
ergonomic handling of HTML-specific quirks.
"""

from functools import partial

from lxml.builder import E as raw_builder

from dashml.types import Child, Prop, BuilderCallable, Element
from dashml.clean import safe_children, safe_props


__all__ = ["Builder"]


class Builder:
    """DashML Markup Builder.

    Allows the creation of `lxml.html` elements via overriding `__getattr__`.

    >>> from dashml import render
    >>> from dashml.builder import Builder
    >>> _ = Builder()
    >>> render(_.p("Hello world!"))
    '<p>Hello world!</p>'

    Under the hood, `__getattr__` curries the `build` method to create an element
    of the tag type you access. This is just syntatic sugar, and you can use build
    directly:

    >>> from dashml import render
    >>> from dashml.builder import Builder
    >>> _ = Builder()
    >>> render(_.build("p", "Hello world!"))
    '<p>Hello world!</p>'
    """

    def __getattr__(self, attr: str) -> BuilderCallable:
        """Get a curried element builder."""
        return partial(self.build, attr)

    def build(self, tag_name: str, *children: Child, **props: Prop) -> Element:
        """Build a DashML element.

        Children passed in can be `Elements` or `None` natively. Nonetype objects
        will be filtered out from the final document (for easy conditional rendering).
        Non-string types will be cast to a string by calling their `__str__()` method. 

        Properties can be strings, booleans, or `None` natively. Booleans and Nontypes
        will function like HTML5 boolean attributes- `True` will leave the property in
        the document; `False` and `None` will leave no value present.

        >>> from dashml import render
        >>> from dashml.builder import Builder
        >>> _ = Builder()
        >>> render(_.build("input", type="checkbox", checked=True))
        '<input type="checkbox" checked>'

        Arguments:
            tag_name (str): The name of the HTML tag to build.
            children (Child): A list of strings, Elements, or None
        Keyword Arguments:
            properties (Prop): A list of HTML5 properties.
        Returns:
            (Element) A DashML/lxml Element.
        """
        tag: BuilderCallable = getattr(raw_builder, tag_name)
        return tag(*safe_children(children), **safe_props(props))
