import typing as t
from functools import partial

from dashml.builder import Builder
from dashml.clean import safe_children, safe_props
from dashml.types import Child, Prop, BuilderCallable, Element
from dashml.html import render, unsafe_from_string


__all__ = ["_", "render", "unsafe_from_string"]


_ = Builder()
