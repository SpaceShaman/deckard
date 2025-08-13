from deckard import search
from deckard.patterns import pl
from deckard.patterns import standard


def test_search_with_multiple_patterns():
    text = "Hello, my email is spaceshaman@tuta.io and my phone number is +48 792 321 321 and my address is ul. Tesotowa 12/6A, 66-700 Bielsko-Biała. Have a nice day"
    result = search([standard.EMAIL, pl.MOBILE_PHONE, pl.ADDRESS], text)

    assert result.groupdict() == {  # type: ignore
        "email": "spaceshaman@tuta.io",
        "mobile_phone": "792 321 321",
        "street": "ul. Tesotowa",
        "building": "12",
        "apartment": "6A",
        "zip_code": "66-700",
        "city": "Bielsko-Biała",
    }
