def greet(name: str) -> str:
    trimmed_name = name.strip()
    return f"Hello, {trimmed_name or 'guest'}!"
