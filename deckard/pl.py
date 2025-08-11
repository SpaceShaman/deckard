EMAIL = r"(?P<email>\w+@\w+\.\w+)"

MOBILE_PHONE = r"(?P<mobile_phone>\d{3}\s?\d{3}\s?\d{3})"


_STREET_PATTERN = (
    r"(ul\.|al\.|pl\.|os\.|ulica|aleja|plac)\s+[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+"
)

_ZIP_CODE_PATTERN = r"\d{2}-\d{3}"

STREET = rf"(?P<street>{_STREET_PATTERN})"

ZIP_CODE = rf"(?P<zip_code>{_ZIP_CODE_PATTERN})"

CITY = rf"(?<=\b{_ZIP_CODE_PATTERN}\s)(?P<city>[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+)"
