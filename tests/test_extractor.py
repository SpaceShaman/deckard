from deckard.extractor import extract
from deckard import pl


def test_extract_email_address_pl():
    text = "Hello, my email is spaceshaman@tuta.io can you help me?"
    assert extract(text, [pl.EMAIL]) == {"email": "spaceshaman@tuta.io"}


def test_extract_mobile_phone_number_pl():
    text = "Hello, my phone number is +48 792 321 321 can you help me?"
    assert extract(text, [pl.MOBILE_PHONE]) == {"mobile_phone": "792321321"}


def test_extract_email_address_and_mobile_phone_number_pl():
    text = "Hello, my email is spaceshaman@tuta.io and my phone number is +48 792 321 321 can you help me?"
    assert extract(text, [pl.EMAIL, pl.MOBILE_PHONE]) == {
        "email": "spaceshaman@tuta.io",
        "mobile_phone": "792321321",
    }


def test_extract_zip_code_pl():
    text = "Cześć, mój adres to ul. Testowa 1, 60-700 Warszawa"
    assert extract(text, [pl.ZIP_CODE]) == {"zip_code": "60-700"}


def test_extract_street_pl():
    text = "Cześć, mój adres to ul. Testowa 1, 60-700 Warszawa"
    assert extract(text, [pl.STREET]) == {"street": "ul. Testowa"}
