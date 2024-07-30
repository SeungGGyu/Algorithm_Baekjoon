def is_palindrome(word):

    return word == word[::-1]


def main():

    word = input('단어 입력:').strip()

    if is_palindrome(word):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()