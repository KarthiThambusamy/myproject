## How to reverse a word ##

n=input("Enter a word:  ")
def letter(n):
    word=""
    for i in n:
        word=i+word
    print(word)
letter(n)
