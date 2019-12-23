"""DashML - Create HTML with composable Python functions.

Usage:

>>> from dashml import render, _
>>> render(_.p("Hello world!"))
'<p>Hello world!</p>'
"""

from dashml.html import render, unsafe_from_string
from dashml.builder import Builder


__all__ = ["_", "render", "unsafe_from_string", "VERSION"]


VERSION = "0.1.1"
_ = Builder()
