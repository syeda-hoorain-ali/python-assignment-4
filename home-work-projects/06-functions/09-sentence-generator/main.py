TEMPLATES: list[str] = [
    "I am excited to add this {word} to my vast collection of them!",
    "It's so nice outside today it makes me want to {word}!",
    "Looking out my window, the sky is big and {word}!"
]

def make_sentence(word, part_of_speech: int):
    try:
        template = TEMPLATES[part_of_speech]
        return template.format(word=word)
    except: # part_of_speech is invalid (not 0, 1, or 2)
        return "Part of speech must be 0, 1, or 2! Can't make a sentence."


def main():
    word :  str = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    sentance = make_sentence(word, part_of_speech)
    print(sentance)

if __name__ == '__main__':
    main()
