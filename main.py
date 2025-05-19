# main.py

import json

def load_vocab():
    with open("vocab.json", "r", encoding="utf-8") as file:
        return json.load(file)

def display_categories(vocab):
    print("\nBlockchain Glossary Categories:\n")
    for i, category in enumerate(vocab.keys(), 1):
        print(f"{i}. {category}")
    print("\nType the number or name of the category you want to explore (or 'exit' to quit):")

def display_terms(terms):
    print("\nTerms in this Category:\n")
    for term, definition in terms.items():
        print(f"📘 {term}\n    → {definition}\n")

def main():
    vocab = load_vocab()
    while True:
        display_categories(vocab)
        choice = input("Enter your choice: ").strip()
        if choice.lower() == 'exit':
            print("Goodbye 👋")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(vocab):
            category = list(vocab.keys())[int(choice) - 1]
        elif choice in vocab:
            category = choice
        else:
            print("Invalid choice. Try again.")
            continue
        display_terms(vocab[category])

if __name__ == "__main__":
    main()
