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
