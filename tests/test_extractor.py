from deckard.extractor import extract
from deckard import pl


def test_extract_email_address_pl():
    text = "Hello, my email is spaceshaman@tuta.io can you help me?"
    assert extract(text, [pl.EMAIL]) == {"email": "spaceshaman@tuta.io"}


def test_extract_mobile_phone_number_pl():
    text = "Hello, my phone number is +48 792 321 321 can you help me?"
    assert extract(text, [pl.MOBILE_PHONE]) == {"mobile_phone": "792 321 321"}


def test_extract_email_address_and_mobile_phone_number_pl():
    text = "Hello, my email is spaceshaman@tuta.io and my phone number is +48 792 321 321 can you help me?"
    assert extract(text, [pl.EMAIL, pl.MOBILE_PHONE]) == {
        "email": "spaceshaman@tuta.io",
        "mobile_phone": "792 321 321",
    }


def test_extract_email_address_and_mobile_phone_number_without_mobile_in_text_pl():
    text = "Hello, my email is spaceshaman@tuta.io and i dont have a mobile phone number can you help me?"
    assert extract(text, [pl.EMAIL, pl.MOBILE_PHONE]) == {
        "email": "spaceshaman@tuta.io",
        "mobile_phone": None,
    }


def test_extract_address_pl():
    text = "Cześć, mój adres to ulica Jana Pawła 12A/6, 66-700 Bielsko-Biała. Dziękuję za wiadomość."
    assert extract(text, [pl.ADDRESS]) == {
        "street": "ulica Jana Pawła",
        "building": "12A",
        "apartment": "6",
        "zip_code": "66-700",
        "city": "Bielsko-Biała",
    }


def test_extract_address_pl_with_multi_word_city():
    text = "Cześć, mój adres to ulica Jana Pawła 12/22B, 66-700 Nowe Miasto nad Pilicą. Dziękuję za wiadomość."

    assert extract(text, [pl.ADDRESS]) == {
        "street": "ulica Jana Pawła",
        "building": "12",
        "apartment": "22B",
        "zip_code": "66-700",
        "city": "Nowe Miasto nad Pilicą",
    }


def test_extract_address_pl_with_small_city_without_street():
    text = "Cześć, mój adres to Michałowo 1, 66-700 Dziękuję za wiadomość."
    assert extract(text, [pl.ADDRESS]) == {
        "street": None,
        "building": "1",
        "apartment": None,
        "zip_code": "66-700",
        "city": "Michałowo",
    }


def test_extract_address_mobile_phone_and_email_pl():
    text = "Witaj,\n\nmój adres to ulica Jana Pawła 12A/12, 66-700 Bielsko-Biała. Dziękuję za wiadomość.\n\nMobile: 792 321 321\nEmail: spaceshaman@tuta.io\n\nPozdrawiam,\nPan XYZ"
    assert extract(text, [pl.ADDRESS, pl.MOBILE_PHONE, pl.EMAIL]) == {
        "street": "ulica Jana Pawła",
        "building": "12A",
        "apartment": "12",
        "zip_code": "66-700",
        "city": "Bielsko-Biała",
        "mobile_phone": "792 321 321",
        "email": "spaceshaman@tuta.io",
    }
