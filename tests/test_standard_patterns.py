from deckard import search
from deckard.patterns import standard


def test_search_email_address_pl():
    text = "Hello, my email is spaceshaman@tuta.io can you help me?"

    result = search([standard.EMAIL], text)

    assert result.groupdict() == {"email": "spaceshaman@tuta.io"}  # type: ignore
