#!/usr/bin/env python3

import random

while True:
# Load the lists from files
    with open("first.txt", "r") as f:
        first_names = [line.strip() for line in f.readlines()]

    with open("last.txt", "r") as f:
        last_names = [line.strip() for line in f.readlines()]

    with open("nickname.txt", "r") as f:
        nicknames = [line.strip() for line in f.readlines()]

    with open("adjective.txt", "r") as f:
        adjectives = [line.strip() for line in f.readlines()]

# Define the possible formats
    formats = [
        "First Last",
        "First Nickname Last",
        "First The Nickname Last",
        "First Adjective Nickname Last",
        "First The Adjective Nickname Last",
        "Nickname First",
        "Nickname Last",
        "Adjective Nickname First",
        "Adjective Nickname Last",
        "The Nickname First",
        "The Nickname Last",
        "The Adjective Nickname First",
        "The Adjective Nickname Last",
        "Random"
    ]

# Get the user's choice
    print("Choose a format:")
    for i, fmt in enumerate(formats):
        print(f"{i+1}. {fmt}")
    choice = input("Enter the number of the format you want: ")

    if choice == "14":  # Random
        choice = random.choice(range(1, 13))

# Get the chosen format
    chosen_format = formats[int(choice) - 1]

# Generate a random name based on the chosen format
    def generate_name(format):
        parts = format.split()
        for i, part in enumerate(parts):
            if part == "First":
                parts[i] = random.choice(first_names)
            elif part == "Last":
                parts[i] = random.choice(last_names)
            elif part == "Nickname":
                parts[i] = random.choice(nicknames)
            elif part == "Adjective":
                parts[i] = random.choice(adjectives)
            elif part == "The":
                parts[i] = "The"
        return " ".join(parts)

    print("Generated name:", generate_name(chosen_format))

    continue_prog = input("Generate Another? (y/n) ")
    if continue_prog.lower() != "y":
        break





