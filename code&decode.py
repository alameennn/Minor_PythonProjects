import string
import random

choice = int(input("1 for code, 2 for decode: "))
st = input("enter your message: ").lower()
words = st.split(" ")

if choice == 1:
    nwords = []  # empty list for encoded words
    for word in words:
        if len(word) >= 3:
            r1 = ''.join(random.choices(string.ascii_lowercase, k=3))  # Random string of length 3
            r2 = ''.join(random.choices(string.ascii_lowercase, k=3))  # Another random string of length 3
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])  # Reverse the word if length < 3
    print(" ".join(nwords))
if choice == 2:
    nwords = []  # empty list for decoded words
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]  # short logic
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])  # Reverse the word if length < 3
    print(" ".join(nwords))
