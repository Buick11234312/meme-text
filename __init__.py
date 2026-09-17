import argparse


def memeify(text: str) -> str:
    result = []
    uppercase = False

    for character in text:
        if character.isalpha():
            result.append(character.upper() if uppercase else character.lower())
            uppercase = not uppercase
        else:
            result.append(character)

    return "".join(result)


def main() -> None:
    parser = argparse.ArgumentParser(description="Turn text into meme text")
    parser.add_argument("text", help="text to transform")
    args = parser.parse_args()
    print(memeify(args.text))


__all__ = ["memeify", "main"]
