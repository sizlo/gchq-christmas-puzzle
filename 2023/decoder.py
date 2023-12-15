import sys

def main():
    input_lines = [
        "Agklq ldhum qom ndem.",
        "Gembqgax c 4-hmqqmk vdke.",
        "Hddp mumkxvomkm.",
        "Ycxim gq'l umkx diugdsl.",
    ]

    decoder = {
        " ": " ",
        ".": ".",
        "-": "-",
        "'": "'",
        "4": "4",
        "c": "a",
        "m": "e",
        "u": "v",
        "k": "r",
        "x": "y",
        "v": "w",
        "o": "h",
        "y": "m",
        "i": "b",
        "q": "t",
        "g": "i",
        "l": "s",
        "a": "f",
        "d": "o",
        "h": "l",
        "s": "u",
        "p": "k",
        "e": "d",
        "b": "n",
        "n": "c",
    }

    counts = {}

    decoded = ""

    for line in input_lines:
        for letter in line:
            letter = letter.lower()
            if letter not in counts.keys():
                counts[letter] = 0
            counts[letter] += 1

            if letter in decoder.keys():
                decoded += decoder[letter]
            else:
                decoded += "?"
        decoded += "\n"

    for letter, count in sorted(counts.items(), key=lambda item: item[1]):
        print(f"{letter} => {counts[letter]}")

    print()
    print(decoded)


if __name__ == "__main__":
    main()
