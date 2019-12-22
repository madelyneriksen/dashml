"""Tests that strings put into DashML functions are escaped and processed."""


from dashml import render, _


def test_render_script_fails():
    """Gratuitous test of the classic alert."""
    value = render(_.p("<script>alert('Hello, world!')</script>"))
    assert value == ("<p>&lt;script&gt;alert('Hello, world!')&lt;/script&gt;</p>")
