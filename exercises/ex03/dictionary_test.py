"""Tests for dictionary functions."""

__author__ = "730559960"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert() -> None:
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}
    assert invert({"a": "z"}) == {"z": "a"}
    assert invert({}) == {}


def test_count() -> None:
    assert count(["a", "b", "a", "a", "c"]) == {"a": 3, "b": 1, "c": 1}
    assert count(["a", "z", "f"]) == {"a": 1, "z": 1, "f": 1}
    assert count([]) == {}


def test_favorite_color() -> None:
    assert (
        favorite_color({"tom": "blue", "jerry": "red", "spongebob": "yellow"}) == "blue"
    )
    assert favorite_color({"nat": "green", "jash": "green", "ryan": "blue"}) == "green"
    assert favorite_color({}) == ""


def test_bin_len() -> None:
    assert bin_len(["dog", "cat", "bird"]) == {3: {"dog", "cat"}, 4: {"bird"}}
    assert bin_len(["a", "b", "c"]) == {1: {"a", "b", "c"}}
    assert bin_len([]) == {}
