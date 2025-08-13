EMAIL = r"(?P<email>\w+@\w+\.\w+)"

MOBILE_PHONE = r"(?P<mobile_phone>\d{3}\s?\d{3}\s?\d{3})"

_STREET = r"(?:ul\.|al\.|pl\.|os\.|ulica|aleja|plac)\s+[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+(?:[\s-][A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+)*"

_HOUSE_NO = r"\d+[A-Za-z]?(?:/\d+[A-Za-z]?)?"

_ZIP_CODE = r"\d{2}-\d{3}"

STREET = rf"(?P<street>{_STREET})"

ZIP_CODE = rf"(?P<zip_code>{_ZIP_CODE})"

_WORD = r"[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+(?:-[A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+)*"
_CONNECT = r"(?:nad|pod|przy|w|we|koło)"
_TOKEN = rf"(?:{_WORD}|{_CONNECT})"

STREET_NUMBER = rf"(?:{STREET})\s+(?P<street_number>{_HOUSE_NO})"

CITY_0 = rf"(?<=\b{_ZIP_CODE}\s)(?P<city>{_TOKEN}(?:[ -]{_TOKEN}){{0,4}})"

CITY_1 = rf"(?P<city>{_TOKEN}(?:[ -]{_TOKEN}){{0,4}})(?=\s+{_HOUSE_NO}\b)(?=.*?\b{_ZIP_CODE}\b)"

_ADDRESS_0 = (
    rf"(?s)^(?=.*?{STREET})(?=.*?{STREET_NUMBER})(?=.*?{ZIP_CODE})(?=.*?{CITY_0})"
)

_ADDRESS_1 = (
    rf"(?s)^(?=.*?{CITY_1})(?=.*?\b(?P<street_number>{_HOUSE_NO})\b)(?=.*?{ZIP_CODE})"
)

ADDRESS = rf"(?x)(?|{_ADDRESS_0}|{_ADDRESS_1})"
