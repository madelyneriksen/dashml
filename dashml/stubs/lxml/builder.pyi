import typing as t

from lxml.etree import Element

from mypy_extensions import VarArg, KwArg

Children = t.Union[Element, str]

class ElementMaker:
    def __getattr__(
        self, tag: str
    ) -> t.Callable[
        [VarArg(Children), KwArg(t.Union[str, int, None, bool])], Element
    ]: ...

def E() -> Element: ...
