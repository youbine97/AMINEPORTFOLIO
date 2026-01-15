
# WORD = input("ENTEER THE WORD:")

# for i in WORD:
#     C = 0
#     for j in WORD:
#         if j == i:
#             C += 1
#     print(i,C)



WORDS = [
    "cat", "ktf", "ftk", "tac",
    "tfk", "cta", "atc",
]

def find_anagrams(word):
    sorted_word = sorted(word)
    result = []

    for i in WORDS:
        if sorted(i) == sorted_word:
            result.append(i)

    return result  
word = input("Enter the word: ")

matches = find_anagrams(word)

if matches:
    print("the word that has the same CARACTERE:")
    for j in matches:
        print("-", j)
else:
    print("dont found.")

