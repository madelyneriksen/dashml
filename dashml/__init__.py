"""DashML - Create HTML with composable Python functions.

Usage:

>>> from dashml import render, _
>>> render(_.p("Hello world!"))
"<p>Hello world!</p>"
"""

from .core import _, render, unsafe_from_string


VERSION = "0.1.0"


__all__ = ["_", "render", "unsafe_from_string", "VERSION"]
