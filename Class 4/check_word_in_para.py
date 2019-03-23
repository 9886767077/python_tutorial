para = input("Enter one small paragraph")
word = input("Enter a word which you want to search")

word_strip_lower = word.strip().lower()
para_lower = para.lower()

if ( word_strip_lower in para_lower):
    print("your word is in para")
else:
    print("your word is not in para")

