"""Test unsafe element creation."""


import pytest
from dashml import unsafe_from_string


def test_unsafe_string_loading():
    """Test the loading of unsafe html."""
    ele = unsafe_from_string("<script>alert()</script>")
    assert len(ele.xpath("//script")) == 1
    assert ele.xpath("//script")[0].text == "alert()"
