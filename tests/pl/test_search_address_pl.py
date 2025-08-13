from deckard import search
from deckard.patterns import pl


def assert_search_address(address: str, expected: dict):
    text = f"Cześć, mój adres to {address}. Dziękuję za wiadomość."
    result = search([pl.ADDRESS], text)

    assert result.groupdict() == expected  # type: ignore


def test_search_address_pl_0():
    assert_search_address(
        "ulica Jana Pawła 12A/6, 66-700 Bielsko-Biała",
        {
            "street": "ulica Jana Pawła",
            "building": "12A",
            "apartment": "6",
            "zip_code": "66-700",
            "city": "Bielsko-Biała",
        },
    )


def test_search_address_pl_1():
    assert_search_address(
        "ul. Natolińska 26, 44-300 Łódź",
        {
            "street": "ul. Natolińska",
            "building": "26",
            "apartment": None,
            "zip_code": "44-300",
            "city": "Łódź",
        },
    )


def test_search_address_pl_2():
    assert_search_address(
        "Gądki Zdrój 22/6A 66-200",
        {
            "street": None,
            "building": "22",
            "apartment": "6A",
            "zip_code": "66-200",
            "city": "Gądki Zdrój",
        },
    )


def test_search_address_pl_3():
    assert_search_address(
        "Lednogóra 28C, 66-333",
        {
            "street": None,
            "building": "28C",
            "apartment": None,
            "zip_code": "66-333",
            "city": "Lednogóra",
        },
    )


def test_search_address_pl_4():
    assert_search_address(
        "ul. Błogosławionego Ładysława z Gielniowa 122/6A 66-700 Warszawa",
        {
            "street": "ul. Błogosławionego Ładysława z Gielniowa",
            "building": "122",
            "apartment": "6A",
            "zip_code": "66-700",
            "city": "Warszawa",
        },
    )
