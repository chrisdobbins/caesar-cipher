import pytest
import importlib
import sys
import io
import builtins
import cipher

@pytest.mark.parametrize("original_sentence,encrypted_sentence",
                        [['python is fun!', 'udymts nx kzs!'],
                        ['aaa', 'fff'],
                        ['xyz', 'cde'],
                        ['A sentence with Capital letters.', 'f xjsyjshj bnym hfunyfq qjyyjwx.'],
                        ['#$%^&*()', '#$%^&*()']
                        ])
def test_cipher(original_sentence, encrypted_sentence):
    #mocked_stdout = io.StringIO()

    result = cipher.cipher(original_sentence)
    
    assert result == encrypted_sentence
