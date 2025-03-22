"""Recreating the wordle game"""

__author__ = "730559960"


def contains_char(word: str, char: str) -> bool:
    """Checks if a word contains a character"""
    assert len(char) == 1, f"len('{char}') is not 1"
    idx: int = 0
    while idx < len(word):
        if word[idx] == char:
            return True
        idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emojified feedback on guess"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret), "Guess must be same length as secret"
    result: str = ""
    idx: int = 0
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1
    return result


def input_guess(expected_length: int) -> str:
    guess: str = input(f"Enter a {expected_length} character word:")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    guess: str = ""

    while guess != secret and turn <= 6:
        print(f"===Turn {turn}/6===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
        turn += 1

    if guess != secret:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
