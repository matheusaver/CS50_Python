from twttr import shorten

def test_lower_vowel():
    assert shorten("matheus") == "mths"
    assert shorten("teste") == "tst"
def test_upper_vowel():
    assert shorten("MATHEUS") == "MTHS"
    assert shorten("TESte") == "TSt"
def test_number():
    assert shorten("CS50") == "CS50"
    assert shorten("abc123") == "bc123"
def test_ponctuation():
    assert shorten("hello!") == "hll!"
    assert shorten("Mandioca?") == "Mndc?"
