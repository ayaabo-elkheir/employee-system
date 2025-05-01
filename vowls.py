def countvowels(text):
   
    vowels = "aeiou"

    count = 0
    for v in vowels:
        count += text.lower().count(v)
    return count

user_input = input("enter a string")
vowelcount = countvowels(user_input)

print("number of vowels", vowelcount)