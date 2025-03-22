"""Practice with dictionaries."""

__author__ = "730559960"


def invert(input: dict[str, str]) -> dict[str, str]:
    "Inverts the key and value of a dictionary"
    inverted: dict[str, str] = {}
    for key in input:
        value = input[key]
        if value in inverted:
            raise KeyError("Duplicate key found")
        inverted[value] = key
    return inverted


def count(input: list[str]) -> dict[str, int]:
    """Counts the number of times a string appears in a list"""
    count: dict[str, int] = {}
    idx: int = 0
    while idx < len(input):
        if input[idx] in count:
            count[input[idx]] += 1
        else:
            count[input[idx]] = 1
        idx += 1
    return count


def favorite_color(input: dict[str, str]) -> str:
    """Finding the most frequent color in a dictionary"""
    color_list: list[str] = []
    for key in input:
        color_list.append(input[key])
    color_count: dict[str, int] = count(color_list)
    most_common: str = ""
    max_count: int = 0
    for key in color_count:
        if color_count[key] > max_count:
            max_count = color_count[key]
            most_common = key
    return most_common


def bin_len(input: list[str]) -> dict[int, set[str]]:
    """Counts the number of strings of each length in a list""" ""
    bin_lengths: dict[int, set[str]] = {}
    idx: int = 0
    while idx < len(input):
        if len(input[idx]) in bin_lengths:
            bin_lengths[len(input[idx])].add(input[idx])
        else:
            bin_lengths[len(input[idx])] = {input[idx]}
        idx += 1
    return bin_lengths
