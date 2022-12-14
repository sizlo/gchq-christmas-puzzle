with open('words.txt') as f:
    all_words = f.read().splitlines()
three_letter_words = [word for word in all_words if len(word) == 3]
nine_letter_words = [word for word in all_words if len(word) == 9]


def debug_print(msg):
    if False:
        print(msg)


def remove_possibilities_that_dont_have_a_valid_word_on_each_row(possibilities):
    result = []
    for possibility in possibilities:
        debug_print(f'\n\nChecking {possibility}')
        is_valid = True
        for i in range(0, 3):
            start = i * 3
            end = start + 3
            row = "".join(possibility[start: end])
            debug_print(f'Trying {row}')
            if row.lower() not in three_letter_words:
                debug_print('Failed')
                is_valid = False
            else:
                debug_print('Success')
        if is_valid:
            debug_print('Keeping this possibility')
            result.append(possibility)
    return result


def remove_possibilities_are_not_a_valid_9_letter_word(possibilities):
    result = []
    for possibility in possibilities:
        full_word = "".join(possibility)
        if full_word.lower() in nine_letter_words:
            result.append(possibility)
    return result


def main():
    initial = ['F', 'O', 'R', 'M', 'A', 'T', 'I', 'O', 'N']

    # Step 1
    post_step_1_possibilities = []
    for top_row_letter in 'PART':
        initial[1] = top_row_letter
        for middle_row_letter in 'PART':
            initial[3] = middle_row_letter
            for bottom_row_letter in 'PART':
                initial[6] = bottom_row_letter
                post_step_1_possibilities.append(initial.copy())

    print(f'Post step 1: {len(post_step_1_possibilities)}')
    filtered_post_step_1_possibilities = remove_possibilities_that_dont_have_a_valid_word_on_each_row(post_step_1_possibilities)
    print(f'Filtered post step 1: {len(filtered_post_step_1_possibilities)}')

    # Step 2
    post_step_2_possibilities = []
    for possibility in filtered_post_step_1_possibilities:
        for middle_row_letter in 'EYES':
            possibility[4] = middle_row_letter
            for bottom_row_letter in 'EYES':
                possibility[8] = bottom_row_letter
                post_step_2_possibilities.append(possibility.copy())

    print(f'Post step 2: {len(post_step_2_possibilities)}')
    filtered_post_step_2_possibilities = remove_possibilities_that_dont_have_a_valid_word_on_each_row(post_step_2_possibilities)
    print(f'Filtered post step 2: {len(filtered_post_step_2_possibilities)}')

    # Step 3
    post_step_3_possibilities = []
    for possibility in filtered_post_step_2_possibilities:
        for top_row_letter in 'UNCURL':
            possibility[0] = top_row_letter
            for middle_row_letter in 'UNCURL':
                possibility[5] = middle_row_letter
                for bottom_row_letter in 'UNCURL':
                    possibility[7] = bottom_row_letter
                    post_step_3_possibilities.append(possibility.copy())

    print(f'Post step 3: {len(post_step_3_possibilities)}')
    filtered_post_step_3_possibilities = remove_possibilities_that_dont_have_a_valid_word_on_each_row(post_step_3_possibilities)
    print(f'Filtered post step 3: {len(filtered_post_step_3_possibilities)}')

    filtered_for_full_word = remove_possibilities_are_not_a_valid_9_letter_word(filtered_post_step_3_possibilities)
    print(f'Filtered for full word: {len(filtered_for_full_word)}')

    print("Possibilities:")
    for possibility in filtered_for_full_word:
        print("".join(possibility))


if __name__ == "__main__":
    main()
