def is_float(value: str) -> bool:
    try:
        _ = float(value)
        return True
    except ValueError:
        return False


def is_int(value: str) -> bool:
    try:
        _ = int(value)
        return True
    except ValueError:
        return False
