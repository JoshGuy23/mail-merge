

def start_letter():
    with open(file="./Input/Letters/starting_letter.txt", mode="r") as file:
        letter = file.read()
    return letter


def get_names():
    with open(file="./Input/Names/invited_names.txt", mode="r") as file:
        names = file.readlines()
    return names


def main():
    letter = start_letter()
    names = get_names()
    for name in names:
        new_letter = letter.replace("[name]", name.strip())
        with open(file=f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as file:
            file.write(new_letter)


main()
