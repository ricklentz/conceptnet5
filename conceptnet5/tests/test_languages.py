from conceptnet5.languages import ALL_LANGUAGES, get_language_name


LANGUAGE_NAMES = {
    'en': 'English',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'es': 'Spanish',
    'ru': 'Russian',
    'pt': 'Portuguese',
    'ja': 'Japanese',
    'zh': 'Chinese',
    'nl': 'Dutch',
    'fi': 'Finnish',
    'pl': 'Polish',
    'bg': 'Bulgarian',
    'sv': 'Swedish',
    'cs': 'Czech',
    'sh': 'Serbo-Croatian',
    'sl': 'Slovenian',
    'ar': 'Arabic',
    'ca': 'Catalan',
    'hu': 'Hungarian',
    'se': 'Northern Sami',
    'is': 'Icelandic',
    'ro': 'Romanian',
    'el': 'Greek',
    'lv': 'Latvian',
    'ms': 'Malay',
    'id': 'Indonesian',
    'tr': 'Turkish',
    'da': 'Danish',
    'ga': 'Irish',
    'vi': 'Vietnamese',
    'ko': 'Korean',
    'hy': 'Armenian',
    'gl': 'Galician',
    'oc': 'Occitan',
    'fo': 'Faroese',
    'gd': 'Scottish Gaelic',
    'fa': 'Persian',
    'ast': 'Asturian',
    'hsb': 'Upper Sorbian',
    'ka': 'Georgian',
    'he': 'Hebrew',
    'no': 'Norwegian',
    'sq': 'Albanian',
    'mg': 'Malagasy',
    'nrf': 'Jèrriais',
    'sk': 'Slovak',
    'lt': 'Lithuanian',
    'et': 'Estonian',
}

# If the display name of a language changes, we should know about it
def test_language_names():
    for code in LANGUAGE_NAMES:
        name = get_language_name(code)
        assert name == LANGUAGE_NAMES[code]
