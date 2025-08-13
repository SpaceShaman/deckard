from deckard import search
from deckard.patterns import pl


def test_search_mobile_phone_pl():
    text = "Hello, my phone number is +48 792 321 321 can you help me?"
    result = search([pl.MOBILE_PHONE], text)

    assert result.groupdict() == {"mobile_phone": "792 321 321"}  # type: ignore
