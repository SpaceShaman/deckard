EMAIL = r"(?P<email>\w+@\w+\.\w+)"

MOBILE_PHONE = r"(?P<mobile_phone>\d{3}\s?\d{3}\s?\d{3})"

STREET = r"(?P<street>(ul\.|al\.|pl\.|os\.|ulica|aleja|plac)\s+[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+)"

ZIP_CODE = r"(?P<zip_code>\d{2}-\d{3})"

CITY = r"(?<=\b\d{2}-\d{3}\s)(?P<city>[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+)"
