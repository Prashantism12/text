def clean_text(text):
    return text[::-1]

if __name__ == "__main__":
    text = input("Enter text: ")
    reversed_text = clean_text(text)

    if text == reversed_text:
        print("palindrome")
    else:
        print("not palindrome")
