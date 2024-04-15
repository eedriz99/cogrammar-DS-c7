\

def alternating_character(n: str) -> str:
    alt_str: str = ''
    for i in range(len(n)):
        if i%2 == 0:
            alt_str += n[i].upper()
        else:
            alt_str += n[i].lower()
    return alt_str

print(alternating_character("Hello World"))

def alternating_word(n: str) -> str:
    alt_word_list: list[str] = n.split(' ')
    for i in range(len(alt_word_list)):
        if i%2 == 0:
            alt_word_list[i] = alt_word_list[i].lower()
        else:
            alt_word_list[i] = alt_word_list[i].upper()
    return " ".join(alt_word_list) 

print(alternating_word("I am learning to code"))
