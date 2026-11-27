import re


def greet(name: str) -> str:
    normalized_name = re.sub(r" {2,}", " ", name.strip())
    return f"Hello, {normalized_name or 'guest'}!"
