def last_word_length():
    """
    最后一个单词的长度
    :return:
    """
    list = input().split(' ')
    print(len(list[-1]))


def multi_lines_sort():
    """
    将输入排序。第一行是个数，后面每一行是待排序数字
    :return:
    """
    while True:
        try:
            num = int(input())
            arr = []
            for i in range(num):
                arr.append(int(input()))
            for n in sorted(list(set(arr))):
                print(n)
        except:
            break


def split_str():
    while True:
        try:
            s = input()
            k = len(s) // 8
            for i in range(k + 1):
                output = s[i * 8: (i + 1) * 8]
                while len(output) < 8:
                    output += '0'
                print(output)
        except:
            break


def jinzhi_transform():
    """
    16进制转10进制
    :return:
    """
    while True:
        try:
            input_str = input().lower()[2:]
            num_dic = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
            res = 0
            for ch in input_str:
                x = int(ch) if ch not in num_dic else num_dic[ch]
                res = 16 * res + x
            print(res)
        except:
            break


def prime_factor():
    num = int(input())
    x = 2
    while x * x <= num:
        if num % x == 0:
            print(x, end=' ')
            num /= x
        else:
            x += 1
    print(int(num), end=' ')


def merge_records():
    num = int(input())
    dic = {}
    for _ in range(num):
        s = input()
        key = int(s.split()[0])
        value = int(s.split()[1])
        dic[key] = dic.get(key, 0) + value
    for key, value in sorted(dic.items()):
        print(str(key) + ' ' + str(value))


def fruit_sort():
    n = int(input())
    fruits = []
    dic = {}
    while True:
        try:
            s = input().split()
            fruit, man, price = s
            if fruit not in fruits:
                fruits.append(fruit)
            if fruit not in dic:
                dic[fruit] = {}
            dic[fruit][man] = price
        except:
            break
    for fruit in fruits:
        single_dic = dic[fruit]
        for key, value in sorted(single_dic.items(), key=lambda x: int(x[1]) * n + int(x[0])):
            print(fruit + ' ' + key + ' ' + value)


def check_str(s):
    s = s.lower()
    for ch in s:
        is_digit = False
        is_alpha = False
        if '0' <= ch <= '9':
            is_digit = True
        if 'a' <= ch <= 'z':
            is_alpha = True
        if not is_digit and not is_alpha and ch != '-':
            return False
    return True


def process_str():
    input_str = input()
    for i in range(2, 20):
        x = '-' * i
        if x in input_str:
            input_str = input_str.replace(x, ' ')

    input_str = input_str.split()
    l = []
    for x in input_str:
        while x.startswith('-'):
            x = x[1:]
        while x.endswith('-'):
            x = x[:-1]
        if check_str(x):
            l.append(x)
    l = l[::-1]
    print(' '.join(l))


if __name__ == "__main__":
    # fruit_sort()
    process_str()
