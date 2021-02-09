import ch1text

text = ch1text.text

def count_sentences(words):
    count = 0
    vowels = '.?!'

    for word in words:
        if word in vowels:
            count += 1
    return count

def compute_readability(text):
    total_words = len(text.split())
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(text.split())
    print(f'В тексте {total_words} - слов, {total_sentences} предложений, {total_syllables} - слогов')


def count_syllables(words):
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count +=word_count

    return count

def count_syllables_in_word(word):
    count = 0

    endings = '.,;!?:'
    last_char = word[-1]
    if last_char in endings:
        proccesed_word = word[0:-1]
    else:
        proccesed_word = word


    if len(proccesed_word) <= 3:
        return 1

    if proccesed_word[-1] in 'eE':
        proccesed_word = proccesed_word[0:-1]

    vowels = 'aeiouAEIOU'
    prev_char = False

    for char in proccesed_word:
        if char in vowels:
            if not prev_char:
                count += 1
            prev_char = True
        else:
            prev_char = False
    if proccesed_word[-1] in 'yY':
        count += 1

    return count


compute_readability(text)
