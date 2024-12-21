from collections import defaultdict
import re


def most_repeated_words(text):
    words = re.findall(r'\w+', text.lower())
    print(words)
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    print(word_count)
    first_most_repeated = ''
    second_most_repeated = ''
    first_max_count = 0
    second_max_count = 0
    print(word_count.items())
    for word, count in word_count.items():
        if count > first_max_count:
            second_max_count = first_max_count
            second_most_repeated = first_most_repeated
            first_max_count = count
            first_most_repeated = word
        elif count > second_max_count:
            second_max_count = count
            second_most_repeated = word

    print(f"1st most repeated word: '{first_most_repeated}' (count: {first_max_count})")
    print(f"2nd most repeated word: '{second_most_repeated}' (count: {second_max_count})")


text = "Sain baina uu, Minii neriig Sodbileg gedeg, clear clear, Sodbileg, clear"

most_repeated_words(text)
