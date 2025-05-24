import argparse
import os
from dotenv import load_dotenv  # type: ignore

def count_words(txt: str) -> int:
    return len(txt.split())


def main():
    parser = argparse.ArgumentParser(description="Count words in a text file.")
    parser.add_argument("text")
    args = parser.parse_args()

    print(count_words(args.text))

    load_dotenv(".env", override=True)

    print(os.environ["VERY_SECRET_KEY"])


if __name__ == "__main__":
    main()