"""DashML - Create HTML with composable Python functions.

Usage:

>>> from dashml import render, _
>>> render(_.p("Hello world!"))
"<p>Hello world!</p>"
"""

from .core import _, render


VERSION = "0.0.1"


__all__ = ["_", "render", "VERSION"]
