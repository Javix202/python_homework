# Task 1
def hello():
    return "Hello!"

# Task 2
def greet(name):
    return f"Hello, {name}!"

# Task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation."
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

# Task 4
def data_type_conversion(value, type):
    try:
        match type:
            case "str":
                return str(value)
            case "int":
                return int(value)
            case "float":
                return float(value)
            case _:
                return "Invalid type requested."
    except ValueError:
        return f"You can't convert {value} into a {type}."

# Task 5
def grade(*args):
    try:
        numbers = [float(value) for value in args]
        average = sum(numbers) / len(numbers)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except ValueError:
        return "Invalid data was provided."

# Task 6
def repeat(text, number):
    result = ""
    for _ in range(number):
        result += text
    return result

# Task 7
def student_scores(mode, **kwargs):
    try:
        scores = {name: float(score) for name, score in kwargs.items()}
        if mode == "best":
            return max(scores, key=scores.get)
        elif mode == "mean":
            return sum(scores.values()) / len(scores)
        else:
            return "Invalid mode."
    except ValueError:
        return "Invalid data was provided."

# Task 8
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()
    result = []
    for index, word in enumerate(words):
        if index == 0 or index == len(words) - 1:
            result.append(word.capitalize())
        elif word.lower() in little_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
    return " ".join(result)

# Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

# Task 10
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
        if word.startswith("squ"):
            result.append(word[3:] + "squay")
        elif word.startswith("qu"):
            result.append(word[2:] + "quay")
        elif word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                i += 1
            result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)