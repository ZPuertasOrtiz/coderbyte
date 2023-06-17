def alphabetSoup(string):
    new_string = sorted(list(string))
    string = "".join(new_string)
    return string

print(alphabetSoup("hello"))