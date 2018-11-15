import pytest

from app.display import display_format


@pytest.mark.parametrize(
    "test_display_type, expected",
    [
        (
            "ROUND",
            dict(
                backButton="HIDDEN",
                template="BodyTemplate1",
                title="Random Acts of Kindness",
            ),
        ),
        (
            "RECTANGLE",
            dict(
                backButton="HIDDEN",
                template="BodyTemplate2",
                title="Random Acts of Kindness - Christmas edition",
            ),
        ),
    ],
)
def test_display_format(test_display_type, expected):
    assert display_format(test_display_type) == expected
