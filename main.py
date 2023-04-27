from unidecode import unidecode
from string import punctuation
import numpy as np
import Levenshtein

def big_LtH_chars(input_file):
    # Define a mapping between the Ladino phonetic representation and Hebrew characters
    mapping = {
        'a': 'א',
        'b': 'ב',
        'c': 'ק',
        'd': 'ד',
        'e': 'י',
        'f': '׳פ',
        'g': 'ג',
        'h': 'ה',
        'i': 'י',
        'j': '׳ג',
        'k': 'ק',
        'l': 'ל',
        'm': 'מ',
        'n': 'נ',
        'o': 'ו',
        'p': 'פ',
        'q': 'ק',
        'r': 'ר',
        's': 'ס',
        't': 'ט',
        'u': 'ו',
        'v': '׳ב',
        'w': 'וו',
        'x': 'סק',
        'y': 'י',
        'z': 'ז',
        'A': 'א',
        'B': 'ב',
        'C': 'ק',
        'D': 'ד',
        'E': 'יא',
        'F': '׳פ',
        'G': 'ג',
        'H': 'ה',
        'I': 'יא',
        'J': '׳ג',
        'K': 'ק',
        'L': 'ל',
        'M': 'מ',
        'N': 'נ',
        'O': 'וא',
        'P': 'פ',
        'Q': 'ק',
        'R': 'ר',
        'S': 'ס',
        'T': 'ט',
        'U': 'וא',
        'V': '׳ב',
        'W': 'וו',
        'X': 'סק',
        'Y': 'י',
        'Z': 'ז'
    }

    lig_mapping = {
        'hc': '׳ג',
        'hC': '׳ג',
        'jd': '׳ג',
        'jD': '׳ג',
        'ic': 'יס',
        'iC': 'יס',
        'ec': 'יס',
        'eC': 'יס',
        'ac': 'אק',
        'aC': 'אק',
        'oc': 'וק',
        'oC': 'וק',
        'uc': 'וק',
        'uC': 'וק',
        'eu': 'יאו',
        'eU': 'יאוא',
        'oe': 'ואי',
        'oE': 'ואיא',
        'ue': 'ואי',
        'uE': 'ואיא',
        'aU': 'אוא',
        'hs': 'ש',
        'hS': 'ש'
    }

    # Load the Ladino text file
    with open(input_file, 'r', encoding='utf-8') as f:
        ladino_text = f.read()

    # Capitalize the first letter of every word
    ladino_text = ladino_text.title()

    # Reverse the order of the words in the text
    ladino_text = ladino_text.strip()[::-1]

    # Transliterate each word in the Ladino text to a phonetic representation using the Latin alphabet
   # ladino_text = ladino_text + '\n'
    phonetic_text = []
    for word in ladino_text.split():
        phonetic_word = unidecode(word)
        phonetic_text.append(phonetic_word)

    # Convert the phonetic representation to Hebrew characters using the mapping and reverse the order of the letters
    hebrew_text = []
    for word in phonetic_text:
        modified_word = word
        for key in lig_mapping:
            modified_word = modified_word.replace(key, lig_mapping[key])
        hebrew_word = ''.join(mapping.get(c, c) for c in modified_word)[::-1]
        if hebrew_word == 'א':
            hebrew_word += 'ה'
        if hebrew_word.strip(punctuation)[-1] == 'א':
            if hebrew_word[-1] == 'א':
                if word.strip(punctuation)[1] == 'o' or word.strip(punctuation)[1] == 'u' or word.strip(punctuation)[
                    1] == 'e':
                    hebrew_word = hebrew_word + 'ה'
                else:
                    hebrew_word = hebrew_word[:-1]
                    hebrew_word = hebrew_word + 'ה'
            else:
                if word.strip(punctuation)[1] == 'o' or word.strip(punctuation)[1] == 'u' or word.strip(punctuation)[
                    1] == 'e':
                    hebrew_word = hebrew_word[:-2] + 'ה' + hebrew_word[-2 + 1:]
                else:
                    temp = hebrew_word[-1]
                    hebrew_word = hebrew_word[:-2]
                    hebrew_word += 'ה'
                    hebrew_word += temp
        if hebrew_word.strip(punctuation)[-1] == 'נ':
            if hebrew_word[-1] == 'נ':
                hebrew_word = hebrew_word[:-1]
                hebrew_word = hebrew_word + 'ן'
            else:
                hebrew_word = hebrew_word[:-2] + 'ן' + hebrew_word[-2 + 1:]
        if hebrew_word.strip(punctuation)[-1] == 'מ':
            if hebrew_word[-1] == 'מ':
                hebrew_word = hebrew_word[:-1]
                hebrew_word = hebrew_word + 'ם'
            else:
                hebrew_word = hebrew_word[:-2] + 'ם' + hebrew_word[-2 + 1:]
        hebrew_text.append(hebrew_word)

    # Reverse the order of the words in the text back to the original order
    hebrew_text = hebrew_text[::-1]

    # Write the transliterated text to a file
    with open('src/hebrew_text.txt', 'w', encoding='utf-8') as f:
        f.write(' '.join(hebrew_text))
    return hebrew_text

def LtH_chars(word):
    # Define a mapping between the Ladino phonetic representation and Hebrew characters
    mapping = {
        'a': 'א',
        'b': 'ב',
        'c': 'ק',
        'd': 'ד',
        'e': 'י',
        'f': '׳פ',
        'g': 'ג',
        'h': 'ה',
        'i': 'י',
        'j': '׳ג',
        'k': 'ק',
        'l': 'ל',
        'm': 'מ',
        'n': 'נ',
        'o': 'ו',
        'p': 'פ',
        'q': 'ק',
        'r': 'ר',
        's': 'ס',
        't': 'ט',
        'u': 'ו',
        'v': '׳ב',
        'w': 'וו',
        'x': 'סק',
        'y': 'י',
        'z': 'ז',
        'A': 'א',
        'B': 'ב',
        'C': 'ק',
        'D': 'ד',
        'E': 'יא',
        'F': '׳פ',
        'G': 'ג',
        'H': 'ה',
        'I': 'יא',
        'J': '׳ג',
        'K': 'ק',
        'L': 'ל',
        'M': 'מ',
        'N': 'נ',
        'O': 'וא',
        'P': 'פ',
        'Q': 'ק',
        'R': 'ר',
        'S': 'ס',
        'T': 'ט',
        'U': 'וא',
        'V': '׳ב',
        'W': 'וו',
        'X': 'סק',
        'Y': 'י',
        'Z': 'ז'
    }

    lig_mapping = {
        'hc': '׳ג',
        'hC': '׳ג',
        'jd': '׳ג',
        'jD': '׳ג',
        'ic': 'יס',
        'iC': 'יס',
        'ec': 'יס',
        'eC': 'יס',
        'ac': 'אק',
        'aC': 'אק',
        'oc': 'וק',
        'oC': 'וק',
        'uc': 'וק',
        'uC': 'וק',
        'eu': 'יאו',
        'eU': 'יאוא',
        'oe': 'ואי',
        'oE': 'ואיא',
        'ue': 'ואי',
        'uE': 'ואיא',
        'aU': 'אוא',
        'hs': 'ש',
        'hS': 'ש'
    }

    word = word.title()

    word = word.strip()[::-1]

    # Transliterate each word in the Ladino text to a phonetic representation using the Latin alphabet
    phonetic_text = unidecode(word)

    # Convert the phonetic representation to Hebrew characters using the mapping and reverse the order of the letters

    modified_word = word
    for key in lig_mapping:
        modified_word = modified_word.replace(key, lig_mapping[key])
    hebrew_word = ''.join(mapping.get(c, c) for c in modified_word)[::-1]
    if hebrew_word == 'א':
        hebrew_word += 'ה'
    if hebrew_word.strip(punctuation)[-1] == 'א':
        if hebrew_word[-1] == 'א':
            if word.strip(punctuation)[1] == 'o' or word.strip(punctuation)[1] == 'u' or word.strip(punctuation)[
                1] == 'e':
                hebrew_word = hebrew_word + 'ה'
            else:
                hebrew_word = hebrew_word[:-1]
                hebrew_word = hebrew_word + 'ה'
        else:
            if word.strip(punctuation)[1] == 'o' or word.strip(punctuation)[1] == 'u' or word.strip(punctuation)[
                1] == 'e':
                hebrew_word = hebrew_word[:-2] + 'ה' + hebrew_word[-2 + 1:]
            else:
                temp = hebrew_word[-1]
                hebrew_word = hebrew_word[:-2]
                hebrew_word += 'ה'
                hebrew_word += temp
    if hebrew_word.strip(punctuation)[-1] == 'נ':
        if hebrew_word[-1] == 'נ':
            hebrew_word = hebrew_word[:-1]
            hebrew_word = hebrew_word + 'ן'
        else:
            hebrew_word = hebrew_word[:-2] + 'ן' + hebrew_word[-2 + 1:]
    if hebrew_word.strip(punctuation)[-1] == 'מ':
        if hebrew_word[-1] == 'מ':
            hebrew_word = hebrew_word[:-1]
            hebrew_word = hebrew_word + 'ם'
        else:
            hebrew_word = hebrew_word[:-2] + 'ם' + hebrew_word[-2 + 1:]

    return hebrew_word
def editDist(x, y):
    if x == "":
        return len(y)
    elif y == "":
        return len(x)
    else:
        return Levenshtein.distance(x, y)

def AlignScore(seq1, seq2):
    if len(seq1) == 0:
        return AlignScore([], seq2[:-1]) + editDist("", seq2[-1])
    if len(seq2) == 0:
        return AlignScore(seq1[:-1], []) + editDist(seq1[-1], "")
    first = AlignScore(seq1[:-1], seq2[:-1]) + editDist(seq1[-1], seq2[-1])
    second = AlignScore(seq1[:-1], seq2) + editDist(seq1[-1], "")
    third = AlignScore(seq1, seq2[:-1]) + editDist("", seq2[-1])
    return min(first, second, third)

def align_words(source_file, target_file):

    # Open Ladino characters file and map text to Hebrew chars
    with open(source_file, 'r', encoding='utf-8') as f:
        ladino_text = f.read()
    print(ladino_text.split())
    ladino = ladino_text.split()
    mymap = []
    for word in ladino:
        mymap.append(LtH_chars(word))
    mymap.reverse()
    print(mymap)

    # Open file with real Hebrew-letter text
    with open(target_file, 'r', encoding='utf-8') as f:
        hebrew_text = f.read()
    hebrew = hebrew_text.split()
    hebrew.reverse()
    print(hebrew)
    #print(AlignScore(mymap, hebrew))

align_words("src/ladino_text.txt", "src/real_hebrew_text.txt")