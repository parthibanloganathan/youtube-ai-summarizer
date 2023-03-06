from typing import Set
import tiktoken
import math

enc = tiktoken.get_encoding("gpt2")

MAX_TOKENS = 3800

def count_tokens(text: str) -> int:
    """ Count the number of tokens in a string """
    return len(enc.encode(text))

def is_under_token_limit(text: str) -> bool:
    """ Tells you whether the string is under the token limit """
    num_tokens = len(enc.encode(text))
    return num_tokens < MAX_TOKENS

def get_text_chunks(text: str) -> list:
    """split texts into token limit chunks. encode - split array into token chunks - decode chunk - return chunks"""
    encoded_text = enc.encode(text)
    return [enc.decode(encoded_text[index*MAX_TOKENS:(index+1)*MAX_TOKENS]) for index in range(math.ceil(len(encoded_text)/MAX_TOKENS))]
