import os

p = os.getcwd()


def human_read_format(size):
    n = ['Б', 'КБ', 'МБ', 'ГБ']
    m = size
    c = 0
    while m / 1024 >= 1:
        m = round(m / 1024)
        c += 1
    return f'{m}{n[c]}'


def get_files_sizes():
    sp = []
    for a in os.listdir():
        if os.path.isfile(a):
            s = f'{p}/{a}'
            sp.append(f'{a} {human_read_format(os.path.getsize(s))}')
    return ('\n').join(sp)
