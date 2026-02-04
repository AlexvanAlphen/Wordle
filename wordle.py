from collections import Counter

def new_word(possible_words, guess, feedback):
    new_words = []

    for word in possible_words:
        match = True
        word_letters = list(word)
        
        for x in range(5):
            if feedback[x] == 'g':
                if word[x] != guess[x]:
                    match = False
                    break
                word_letters[x] = None

        for x in range(5):
            if feedback[x] == 'y':
                if guess[x] not in word_letters or word[x] == guess[x]:
                    match = False
                    break
                index = word_letters.index(guess[x])
                word_letters[index] = None

        for x in range(5):
            if feedback[x] == 'b':
                if guess[x] in word_letters:
                    match = False
                    break

        if match:
            new_words.append(word)

    return new_words

def count_word(new_words):
    count = Counter()
    for word in new_words:
        for character in word:
            count[character] += 1
        
    return count

def count_position(new_words):
    position_count = []

    for i in range(5):
        position_count.append(Counter())

    for word in new_words:
        for i in range(5):
            letter = word[i]
            position_count[i][letter] += 1

    return position_count

def letter_values(count):
    ranking = sorted(count, key=count.get)
    values = {}

    x = 1
    for letter in ranking:
        values[letter] = x
        x += 1

    return values

def position_values(pos_counts):
    position_values = []

    for i in range(5):
        values = {}
        sorted_letters = sorted(pos_counts[i], key=pos_counts[i].get)

        score = 1
        for letter in sorted_letters:
            values[letter] = score
            score += 1

        position_values.append(values)

    return position_values


def word_score(word, values, pos_vals):
    seen = set()
    score = 0

    for i, letter in enumerate(word):
        if letter in seen:
            continue
        seen.add(letter)

        score += values.get(letter, 0)
        score += pos_vals[i].get(letter, 0)

    return score

def best_word(possible_words, values):
    best = ""
    highest = 0

    for word in possible_words:
        score = word_score(word, values)
        if score > highest:
            highest = score
            best = word

    return best, highest

def top_words(possible_words, values, pos_vals):
    scored = []
    
    for word in possible_words:
        scored.append((word, word_score(word, values, pos_vals)))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:5]


def main():
    with open("valid_wordle_words.txt", "r", encoding="utf-8") as file:
        possible_words = [words.strip() for words in file.readlines() if words.strip()]

    turn = 0
    max_turns = 6

    print("Welcome to Wordle Solver!")
    print("Feedback legend: g = green, y = yellow, b = black/grey")

    while turn < max_turns and possible_words:
        
        count = count_word(possible_words)
        values = letter_values(count)

        pos_counts = count_position(possible_words)
        pos_vals = position_values(pos_counts)

        top5 = top_words(possible_words, values, pos_vals)

        print(f"\nTurn {turn + 1}: Top 5 suggestions:")
        for i, (word, score) in enumerate(top5, 1):
            print(f"{i}. {word} (score: {score:.2f})")

        choice = input("\nChoose number or enter your own word: ").lower()

        if choice.isdigit() and 1 <= int(choice) <= len(top5):
            guess, score = top5[int(choice) - 1]
        else:
            guess = choice
            score = word_score(guess, values, pos_vals)
            if guess not in possible_words:
                print("This word is not possible or contains letters that are not used")

        print(f"\nTurn {turn + 1}: Guessing '{guess}' (score: {score})")

        while True:
            feedback = input("Enter feedback: ").lower()
            if len(feedback) == 5 and all(letter in "gyb" for letter in feedback):
                break
            print("Invalid feedback")

        if feedback == "ggggg":
            turn += 1
            print(f"Word guessed correctly in {turn} turns!")
            break

        possible_words = new_word(possible_words, guess, feedback)
        print(f"Remaining possible words: {len(possible_words)}")
        
        turn += 1

    else:
        print("Failed to guess the word in 6 turns.")

if __name__ == "__main__":
    main()