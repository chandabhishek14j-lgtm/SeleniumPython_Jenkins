def count_vowels(word):
    # Using simple loop
    count = 0
    for char in word.lower():
        if char in 'aeiou':
            count +=1
    print(count)

    # Using sum()
    print(sum(1 for char in word if char in 'aeiou'))

    # Count each vowels separately
    words = word.lower()
    result = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for char in word:
        if char in 'aeiou':
            result[char] += 1
    print(result)

def count_vow_consonants(word):
    # only counting consonants and vowels
    v_count = 0
    c_count = 0
    words = word.lower()
    for char in words:
        if char.isalpha():
            if char in 'aeiou':
                c_count += 1
            else:
                v_count += 1
    print(f"consonant: {c_count}, vowel: {v_count}")

count_vowels("helloo")
count_vow_consonants("helloo")