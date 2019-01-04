mystr = "MadaM".lower()
revmystr = reversed(mystr)

if list(revmystr) == list(mystr):
    print(mystr, "is a palindrome")
else:
    print(mystr, "is not a palindrome")

