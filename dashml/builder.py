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

    Allows the creation of lxml.html elements via overriding __getattr__.

    >>> from dashml.builder import Builder
    >>> _ = Builder()
    >>> _.p("Hello world!")
    """

    def __getattr__(self, attr: str) -> BuilderCallable:
        """Get a curried element builder."""
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
