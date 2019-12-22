"""Generic tests for rendering DashML components."""


from dashml import _, render


def test_class_name_swapped():
    """Test that class_name is swapped properly."""
    val = render(_.div(class_name="myclass"))
    assert val == '<div class="myclass"></div>'

    val = render(_.p("Some Text", class_name="myclass"))
    assert val == '<p class="myclass">Some Text</p>'


def test_html_for_swapped():
    """Test that html_for is swapped."""
    val = render(_.label(html_for="my-input"))
    assert val == '<label for="my-input"></label>'


def test_render_aria():
    """Test the rendering of aria attributes."""

    val = render(_.button("Close", aria_label="Close"))
    assert val == '<button aria-label="Close">Close</button>'

    val = render(
        _.button("Collapse", aria_expanded="false", aria_controls="collapsible-0")
    )
    assert (
        val
        == '<button aria-expanded="false" aria-controls="collapsible-0">Collapse</button>'
    )


def test_render_data():
    """Test the rendering of data attributes."""
    val = render(_.div(data_text="Some text!"))
    assert val == '<div data-text="Some text!"></div>'

    val = render(_.div(data_lots_of_dashes="value"))
    assert val == '<div data-lots-of-dashes="value"></div>'


# =======================================
# Usage Tests
# Tests with more complicated documents.
# =======================================


def simple_article(content: str, title: str = "JSX in Python"):
    """Creates a simple article document. From the benchmarks."""
    return _.html(
        _.head(
            _.link(rel="stylesheet", type="text/css", ref="/index.css"), _.title(title),
        ),
        _.body(
            _.main(
                _.article(
                    _.header(
                        _.h1("Wow, it's like JSX in python!!"),
                        _.h3("That's really cool."),
                    ),
                    _.p(content),
                )
            )
        ),
    )


def test_render_simple_article():
    """Render out a simple article."""
    article = simple_article(content="Hello world!")
    assert article.xpath("//p")[0].text == "Hello world!"

    article = simple_article(content="Nice", title="My Title")
    assert article.xpath("//title")[0].text == "My Title"


def test_compose_elements():
    """Do some simple element composing."""
    my_paragraph = lambda text: _.p(text, class_name="text-content")
    my_header = lambda text: _.h1(text, class_name="header")

    assert (
        _.html(my_header("Hello world!"), my_paragraph("Nice"),)
        .xpath("//p[@class='text-content']")[0]
        .text
        == "Nice"
    )

    assert (
        _.html(my_header("Hello world!"), my_paragraph("Nice"),)
        .xpath("//h1[@class='header']")[0]
        .text
        == "Hello world!"
    )


def test_orm_style_functions():
    """An ORM-like example of an element function."""

    from typing import NamedTuple

    class Article(NamedTuple):
        """Basically a fake database model."""

        title: str
        content: str
        author: str

        def html(self):
            header = _.header(_.h1(self.title, class_name="article__header"))
            content = _.section(_.p(self.content, class_name="article__content"))
            byline = _.section(
                _.p(_.i(f"By {self.author}"), class_name="article__byline")
            )

            return _.article(header, content, byline,)

    article = Article(
        title="Hello from DashML!",
        content="Demo of ORM-style usage of DashML",
        author="Madelyn Eriksen",
    )

    assert render(article.html())
    assert (
        article.html().xpath("//p[@class='article__content']")[0].text
        == article.content
    )
    assert (
        article.html().xpath("//h1[@class='article__header']")[0].text == article.title
    )
    assert (
        article.html().xpath("//p[@class='article__byline']/i")[0].text
        == "By Madelyn Eriksen"
    )
