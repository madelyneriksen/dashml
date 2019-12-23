"""DashML - Create HTML with composable Python functions.

Usage:

>>> from dashml import render, _
>>> render(_.p("Hello world!"))
"<p>Hello world!</p>"
"""

from .html import render, unsafe_from_string
from .builder import Builder


__all__ = ["_", "render", "unsafe_from_string", "VERSION"]


VERSION = "0.1.0"
_ = Builder()
