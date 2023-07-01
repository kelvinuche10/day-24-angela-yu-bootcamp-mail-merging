PLACEHOLDER = '[name]'

with open("input/letters/starting_letter.txt", "r") as letter:
    letter_template = letter.read()
    with open("input/names/invited_names.txt", "r") as name_data:
        names = name_data.readlines()
        for name in names:
            stripped_name = name.strip()
            new_letter = letter_template.replace(PLACEHOLDER, stripped_name)
            with open(f"output/readytosend/{stripped_name}.txt", 'w') as ready_letters:
                ready_letters.write(new_letter)