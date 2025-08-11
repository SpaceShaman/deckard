EMAIL = r"(?P<email>\w+@\w+\.\w+)"

MOBILE_PHONE = r"(?P<mobile_phone>\d{3}\s?\d{3}\s?\d{3})"


_STREET_PATTERN = r"(?:ul\.|al\.|pl\.|os\.|ulica|aleja|plac)\s+[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+(?:[\s-][A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+)*"

_HOUSE_NO = r"\d+[A-Za-z]?(?:/\d+[A-Za-z]?)?"

_ZIP_CODE_PATTERN = r"\d{2}-\d{3}"

STREET = rf"(?P<street>{_STREET_PATTERN})"

ZIP_CODE = rf"(?P<zip_code>{_ZIP_CODE_PATTERN})"

CITY = rf"(?<=\b{_ZIP_CODE_PATTERN}\s)(?P<city>[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+)"

STREET_NUMBER = rf"(?:{_STREET_PATTERN})\s+(?P<street_number>{_HOUSE_NO})"
