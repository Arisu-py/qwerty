from yandex_testing_lesson import is_prime


def check():
    if not is_prime(2):
        return 'NO'
    if not is_prime(3):
        return 'NO'
    if not is_prime(5):
        return 'NO'
    if not is_prime(7):
        return 'NO'
    if is_prime(4):
        return 'NO'
    if is_prime(22):
        return 'NO'
    # if is_prime(1):
    #     return 'NO'
    # if is_prime(0):
    #     return 'NO'
    # if is_prime(-1):
    #     return 'NO'
    return 'YES'


print(check())
