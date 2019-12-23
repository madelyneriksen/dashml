# Quickstart

## Install DashML

Like most Python packages, DashML is available on the Python Package Index for installation with Pip.

```bash
pip install dashml
```

When you install DashML, its two dependencies [MarkupSafe](https://pypi.org/project/MarkupSafe/) and [lxml](https://pypi.org/project/lxml/) will be installed as well.

## Create A Component

DashML's main interface is `dashml._` , a custom element builder for creating HTML. You can use the `_` object as a pseudo-DSL to declaratively create HTML from Python functions.

Let's try out DashML. Open a few source file `component.py` and add the following:

```python
from dashml import _

def my_component(text: str):
    return _.p(text)
```

This is a valid DashML component! Under the hood, this function will return an `lxml.etree.Element` object. `lxml` is written in C, so by extension DashML components are super fast.

You can render your DashML component to a string using the `dashml.render` function:

```python
from dashml import _, render

def my_component(text: str):
    return _.p(text)

print(render("Hello, world!"))
```

If you run your source file, you'll see printed markup.

```bash
python component.py
<p>Hello, world!</p>
```

## Component Composition

The low-level `_` object is great for creating raw html- but the power of DashML comes out when you create more complex components through _composition_.

Add a new file `example_page.py` and add in the following contents:


```
import typing as t
from dashml import _, render


def header(title: str, subtitle: t.Optional[str] = None):
    """Render our header element."""
    return _.header(
        _.h1(title),
        _.h3(subtitle) if subtitle else None,
    )


def content(text: str):
    """Render page content."""
    return _.main(_.p(text))


def page(title: str, text: str, subtitle: t.Optional[str] = None):
    """Render an entire page."""
    return _.html(
        _.body(
            header(title, subtitle=subtitle),
            content(text)
        )
    )

```

In this example, we create three functions: `header`, `content`, and `page`. The final function `page` _composes_ both `content` and `header` components to create a complete HTML page.

Add the following block of code to your Python file to render out page to an example file:

```python
# ...snip


if __name__ == "__main__":
    my_page = page(
        "Hello world!",
        "Look at my cool HTML page!! It was rendered entirely with Python.",
        subtitle="HTML has never had so many snakes."
    )
    with open("example.html", "w") as file:
        file.write(render(my_page))
```

Now, if you open `example.html` in your browser, you should be able to see your rendered HTML content.

With composition, you can create powerful, expressive functions for declaratively creating your UI. To use your functions in DashML, just remember to return an element generated with `_`.

## What's Next?

Congrats! You have finished the DashML quickstart. ✨ You're ready to create your own super sweet components for use on the web!

Now that you're a DashML expert, consider:

* [Contributing on Github](https://github.com/madelyneriksen/dashml) to help make DashML more awesome.
* [Opening Issues](https://github.com/madelyneriksen/dashml/issues) for feature requests (or bugs!).

And if you make something cool and open-source with DashML, consider posting back to the DashML repo to share the coolness with other developers!
