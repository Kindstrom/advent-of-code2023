import re

string_numbers = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main():
    total = 0
    with open("Day01\input.txt") as file:
        while line := file.readline():
            matches = re.findall(
                "(?=(" + "|".join(string_numbers.keys()) + "|\d))", line
            )
            total += int(
                "".join(
                    [
                        d if d.isdigit() else string_numbers[d]
                        for d in [matches[0], matches[-1]]
                    ]
                )
            )
    print(total)


if __name__ == "__main__":
    main()
