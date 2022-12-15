from difflib import SequenceMatcher as SM


def name_comparator(name_form, name_response):
    s1 = name_form.lower()
    s2 = name_response.lower()

    match_decimal = SM(None, s1, s2).ratio()

    match_percentage = (match_decimal * 100)

    porcentage = f'{match_percentage:.2f}'

    return porcentage

