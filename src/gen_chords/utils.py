def chord_type_to_pretty_symbol(chord_type: str) -> str:
    """
    Format the chord type to a pretty symbol.
    """
    match chord_type:
        case "major_seventh":
            return "Δ7"
        case "dominant_seventh":
            return "7"
        case "minor_seventh":
            return "m7"
        case _:
            raise ValueError(f"Unknown chord type: {chord_type}")


def chord_type_to_ugly_symbol(chord_type: str) -> str:
    """
    Format the chord type to an ugly symbol.
    """
    match chord_type:
        case "major_seventh":
            return "M7"
        case "dominant_seventh":
            return "7"
        case "minor_seventh":
            return "m7"
        case _:
            raise ValueError(f"Unknown chord type: {chord_type}")


def chord_type_to_long_symbol(chord_type: str) -> str:
    """
    Format the chord type to a long symbol.
    """
    match chord_type:
        case "major_seventh":
            return "maj7"
        case "dominant_seventh":
            return "dom7"
        case "minor_seventh":
            return "min7"
        case _:
            raise ValueError(f"Unknown chord type: {chord_type}")


def ugly_root_str_to_pretty_root_str(ugly_root_str: str) -> str:
    """
    Convert a root string like "C#" to a prettier format like "C♯".
    """

    return ugly_root_str.replace("#", "♯").replace("b", "♭")
