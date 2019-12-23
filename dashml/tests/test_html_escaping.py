"""Tests that strings put into DashML functions are escaped and processed."""


from dashml import render, _


def test_render_script_fails():
    """Gratuitous test of the classic alert."""
    value = render(_.p("<script>alert('Hello, world!')</script>"))
    assert value == ("<p>&lt;script&gt;alert('Hello, world!')&lt;/script&gt;</p>")


def test_render_boolean():
    """Test the rendering of boolean attributes."""
    val = render(_.input(type="checkbox", checked=True))
    assert val == '<input type="checkbox" checked>'

    val = render(_.option("California", selected=True))
    assert val == "<option selected>California</option>"


def test_render_numbers():
    val = render(_.p(8))
    assert val == "<p>8</p>"

    val = render(_.p(8.8))
    assert val == "<p>8.8</p>"

    val = render(_.div(data_number=8))
    assert val == '<div data-number="8"></div>'
