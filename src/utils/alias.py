def to_camelCase(string: str):
    return string[0].lower() + string.title()[1:].replace("_", "")
