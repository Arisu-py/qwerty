from yandex_testing_lesson import is_palindrome


def check():
    if not is_palindrome(""):
        return 'NO'
    if not is_palindrome("a"):
        return 'NO'
    if not is_palindrome("aba"):
        return 'NO'
    if is_palindrome("abc"):
        return 'NO'
    return 'YES'


print(check())