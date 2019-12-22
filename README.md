DashML - Functional HTML Generation
====================================

<!-- Badge Spam -->
[![PyPI](https://img.shields.io/pypi/v/dashml?style=flat-square)](https://pypi.org/project/dashml/)
[![GitHub issues](https://img.shields.io/github/issues/madelyneriksen/dashml?style=flat-square)](https://github.com/madelyneriksen/dashml/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](/LICENSE)
![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-black?style=flat-square)

Create functions to build HTML in Python- inspired by the "component movement" in Javascript.

```python
>>> from dashml import _, render
>>>
>>> render(_.p("Hello, world!"))
'<p>Hello, world!</p>'
```

## Why DashML?

JavaScript frameworks like React or Vue took over the frontend landscape because of the ease of creating reusable components. React _especially_ thrives with the fact that components are _code_, and can be manipulated as such.

Meanwhile, server-side languages are stuck with difficult to compose template languages to generate HTML. It's hard to extract components out of Jinja2 or Django templates to re-use.

DashML expands on existing Python libraries to create an ergonomic way to generate HTML in Python.

* Built on `lxml` (built on C) for extreme speed- check out the benchmarks (or run them yourself!).
* `markupsafe` to prevent injection attacks (like React does!)
* A minimal API you can pick up in ~15 minutes- DashML is so simple, you could have written it yourself!

Adopting DashML in your project allows you to create traditional server rendered webpages faster, while embracing the good parts of component driven design.

## Get Started

To get started with DashML, you will need:

* Python 3.6+
* `pip`
* About 5 minutes.

### Install From PyPi

Like almost every Python package, you can install DashML from PyPi:

```bash
pip install dashml
```

Wow, that was really simple.

### Writing Components

DashML components are just functions that return `lxml` `Element` objects. You can write one like this:


```python
# greeter.py

from dashml import _

def greeter(name: str) -> 'Element':
    """My first DashML component!!"""
    return _.p(f"Hello, {name}!")
```

The function `greeter` returns an `Element`, which is a special representation of an xml document from the library `lxml`. `lxml` uses C, so it's really fast to create and modify elements.

You can get a string out of an `Element` by using the DashML function `render`.

```python
# greeter.py

from dashml import render, _

# ...snip

print(render(greeter("Maddie")))
```

If you save this to `greeter.py` and run it, you can see your component get rendered out as a string:

```bash
python greeter.py
<p>Hello, Maddie!</p>
```

### Adding Attributes

HTML documents almost always have attributes on some elements. You can add in attributes to DashML functions as keyword arguments.

```python
# greeter.py

from dashml import _

def greeter(name: str) -> 'Element':
    """My first DashML component!!"""
    return _.p(f"Hello, {name}!", id="my-greeter", class_name="my-greeter")
```

DashML attributes are always snake case. The attributes `class` and `for` are replaced with `class_name` and `html_for`. Additionally, attributes prefixed with `data_` or `aria_` are converted to use dashes instead of underscores. If you've used React, this probably feels familiar!

## DashML Tips

Congrats! You've completed a tour of the DashML API. Here are some friendly suggestions of how to use DashML effectively in your projects.

#### Create composable, reusable functions.

Writing out element names by hand everywhere is _no better_ than just writing plain HTML, and doesn't use the composable and reusable powers DashML has.

For example, than typing out `_.h1(...)` everywhere, create a function called `header` that is specific to your project and creates the elements you need:

```python
def header(text: str) -> 'Element':
    """Creates a header for a page."""
    return _.header(
        _.h1(text, class_name="header__title"),
        class_name="header"
    )
```

Composing functions that create elements is expressive, and a lot cleaner:

```python
page(
    header("HTML in Python? More likely than you think."),
    content(),
    footer(),
)
```

Now that's component driven code!

#### Work With Your Data Structures

A great strategy with DashML components is to have them accept your data objects as arguments, and just control display logic.

For example, if you're working with an ORM object for a blog post, creating a component called `blog_post` provides an easy way to render out your database records:


```python
# components.py

def blog_post(post: BlogPost) -> 'Element':
    return page(
        header(post.title),
        content(post.text),
        footer(),
    )
```

#### Keep DashML Components Separate

Consider keeping your DashML code in a different module from your code that contains business logic (and everything else). Keeping a separate `components.py` file in each module with DashML components keeps your intent clear and code clean:

```
mymodule/
|- components.py
|- models.py
|- views.py
```

Additionally, it allows easier mirroring of objects in other modules. From the blog post example above:

```python
# views.py

from . import components

def my_view(request, post_id: int):
    # ...snip
    post = BlogPost.get(post_id)
    return components.blog_post(post)
```

#### ...And Keep Business Logic out of Components

Components should be as slim as possible, and only handle presentation logic. It's an anti-pattern to bundle up business logic in your DashML components.

```python

# BAD: Don't do this!
def render_post(pk: int):
    post = get_or_404(BlogPost, pk)
    return _.p(post.content)

# GOOD: Just pass in objects to render!
def render_post(post: BlogPost):
    return _.p(post.content)
```

Additionally, every DashML component is ideally a _pure function_, that will always return the same result for a given input.

#### Consider Functional CSS

If you want to bring functional styling into your DashML components, consider using a css library like [Tachyons](https://tachyons.io/) for styling.

```python
def my_text(text: str):
    return _.p(text, class_name="f5 f4-l lh-copy athelas")
```

Atomic/functional CSS blends _exceptionally_ well with DashML, and allows the embracing of functional components in styles and markup.

## Special Thanks

DashML could not be built without these libraries:

* [lxml](https://lxml.de) for creating a _fast_ XML library.
* [Pallets Projects](https://palletsprojects.com/) for creating MarkupSafe

## License

Copyright 2019 under terms of the MIT license. See [LICENSE](/LICENSE) for details.
