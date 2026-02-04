---

# 🟩 Wordle Solver

![Python](https://img.shields.io/badge/Python-3.7+-blue) ![License: MIT](https://img.shields.io/badge/License-MIT-green)

A Python command-line solver for [Wordle](https://www.nytimes.com/games/wordle/index.html) that suggests the best guesses based on letter frequency and position scoring.

---

## 🚀 Features

* Suggests **top 5 word guesses** each turn.
* Updates remaining possible words based on your **feedback** (`g`, `y`, `b`).
* Scores words using **letter frequency** and **position frequency**.
* Fully **interactive CLI** experience.

---

## 🎯 How It Works

1. Load a list of valid Wordle words (`valid_wordle_words.txt`).
2. Count letter and position frequencies.
3. Assign scores to letters and positions.
4. Suggest top scoring words as guesses.
5. Update possible words based on feedback after each turn.
6. Repeat until the word is guessed or 6 turns are used.

### Feedback Legend

| Symbol | Meaning                                           |
| ------ | ------------------------------------------------- |
| `g`    | Letter is in the correct position (green)         |
| `y`    | Letter is in the word but wrong position (yellow) |
| `b`    | Letter is not in the word (black/grey)            |

---

## 🛠 Requirements

* Python 3.7+
* Built-in `collections` module

---

## 💻 Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/wordle-solver.git
cd wordle-solver
```

2. Ensure you have a `valid_wordle_words.txt` file with valid 5-letter Wordle words, one per line.

3. Run the solver:

```bash
python wordle_solver.py
```

4. Follow prompts:

   * Choose a suggested word or type your own.
   * Enter feedback using `g`, `y`, `b`.
   * Repeat until the word is guessed or 6 turns are over.

---

## 📌 Example

```
Turn 1: Top 5 suggestions:
1. balls (score: 45)
2. trick (score: 44)
3. farts (score: 43)
4. shack (score: 42)
5. oater (score: 41)

Choose number or enter your own word: 1
Turn 1: Guessing 'raise' (score: 45)
Enter feedback: bgybb
Remaining possible words: 134
```

---

## ⚖️ License

MIT License – free to use, modify, and share.

---
