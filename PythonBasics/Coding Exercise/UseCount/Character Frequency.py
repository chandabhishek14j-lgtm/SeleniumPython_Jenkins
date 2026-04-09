# count the number of times each character is there
def char_freq(word):
    # Method 1: Using dictionary + loop
    sample = {}
    duplicates = 0
    for c in word:
        if c in sample:
            sample[c] += 1
        else:
            sample[c] = 1
    print(sample)
    # Method 2: Using dict.get()
    freq = {}
    for char in word:
        freq[char] = freq.get(char, 0) + 1
    print(freq)

    # only count alphabets
    vowels = {}
    for s in word:
        if s in 'aeiou':
            if s in vowels:
                vowels[s] += 1
            else:
                vowels[s] = 1
    print(vowels)

    # Using count()
    counts = {}
    for i in word:
        counts[i] = word.count(i)
    print(counts)
char_freq("madam")