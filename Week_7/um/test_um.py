from um import count

def testes():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("Testing with no word") == 0
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album um") == 2
    assert count("Um? yummy um drum um umm, um?") == 4
