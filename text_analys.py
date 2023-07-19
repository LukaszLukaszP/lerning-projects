import string

usert_text = input("Enter text to analys: ")
print("Text with all uppercase:", usert_text.upper())
print("Text with all lowercase:", usert_text.lower())
word_count = len(usert_text.split())
print("Number of words =", word_count)
#letter = input("Enter a letter you want to count: ")
#letter_count = usert_text.count(letter)
#print("Number of occurrences of the letter", letter, "in the text:", letter_count)
print("ilość znaków: ", len(usert_text))

usert_text_list = list(usert_text.lower())
alphabet = string.ascii_lowercase

alph_user_text = []
for el in usert_text_list:
    if el not in list(string.punctuation):
        alph_user_text.append(el)

num_of_letters = len(alph_user_text)

def how_many_letters(letter):
    num = 0
    for element in alph_user_text:
        if letter == element:
            num = num + 1
    return num

alphabet_len = len(alphabet)

for i in alphabet:
    num_of_i = how_many_letters(i)
    print("number of occurrences of the letter " + i + ": " + str(num_of_i))
    perc = num_of_i / num_of_letters * 100
    print("percentage of occurrence", i, str(perc) + "%")

