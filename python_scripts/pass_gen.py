import sys, random, string



def generate_password(length, special="true", numbers="true", uppercase="true"):
    characters = string.ascii_lowercase
    if special == "true":
        characters += string.punctuation
    if numbers == "true":
        characters += string.digits
    if uppercase == "true":
        characters += string.ascii_uppercase
    return ''.join(random.choice(characters) for l in range(int(length)))


x = 0

if __name__ == "__main__":
    length = sys.argv[1]
    spec = sys.argv[2]
    num = sys.argv[3]
    upper = sys.argv[4]
    print(generate_password(length, spec, num, upper))
    