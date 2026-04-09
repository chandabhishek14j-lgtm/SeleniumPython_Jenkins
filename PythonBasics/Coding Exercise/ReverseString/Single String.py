sample = "singlestring"

def reverse_single_string():
### using for loop
    for char in sample:
        result = char+sample
    print(result)

# ### using slicing
#     result = sample[::-1]
#     print(result)
#
# ### using while loop
#     i = len(sample)
#     while i>0:
#         result += sample[i]
#         i -=1
#     print(result)
#
# ### using built i reversed
#     result = "".join(reversed(sample))

reverse_single_string()

sent = "Hello Abhishek Chand"
def reverse_sentence(sentence):
    # 1) Reverse the order of words
    reverse_sent = sentence.split() # converting string to array
    reverse_sent.reverse() # reversing order of array
    print(" ".join(reverse_sent)) #converting back to string

    #Reverse each word, but keep the same word order
    words = sentence.split()
    reverse_array = []
    for word in words:
        reverse_array.append(word[::-1]) # using splicing to reverse characters in
                                         # word but keeping the same order as before
    print(" ".join(reverse_array))

    #reverse words and characters
    print(sentence[::-1])

reverse_sentence(sent)