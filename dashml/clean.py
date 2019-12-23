"""Functions for cleaning children or attribute values."""


import typing as t
from dashml.types import Element, Child, Prop


def safe_child(var: Child) -> Child:
    """Mark a child value as safe."""
    if isinstance(var, Element):
        return var
    else:
        return str(var)


def safe_children(children: t.Iterable[Child]) -> t.List[Child]:
    """Make all children safe."""
    return [safe_child(x) for x in children if x is not None]


# Like `className` or `htmlFor` in React.
RESERVED_PAIRS = {
    "class_name": "class",
    "html_for": "for",
}


def safe_props(props: t.Dict[str, Prop]) -> t.Dict[str, Prop]:
    """Swap property values passed in as kwargs to become render safe.

    This changes snake_case to use dashes for HTML, as well as doing swaps for
    class_name and html_for.
    """
    for key, value in props.items():
        if isinstance(value, bool) or value is None:
            # Convert booleans/Nonetypes into HTML5 compatible booleans.
            if value:
                props[key] = ""
            else:
                del props[key]
                continue
        if key.startswith("data_") or key.startswith("aria_"):
            props[key.replace("_", "-")] = str(props.pop(key))
        elif key in RESERVED_PAIRS:
            props[RESERVED_PAIRS[key]] = str(props.pop(key))
        else:
            props[key] = str(value)
    return props
