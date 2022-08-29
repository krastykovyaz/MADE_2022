def count_permut(s):
    s = s.split()
    s1 = s[0]
    s2 = s[1:]
    N = int(s1)
    if N == len(s2):
        mapped_lst = list(map(int, s2))
        max_el_1 = max(mapped_lst)
        mapped_lst_abs = [abs(i - (max_el_1 / 2)) for i in mapped_lst]
        min_el_abs = min(mapped_lst_abs)
        lst_collector = []
        i = 0
        for e in mapped_lst_abs:
            if e == min_el_abs:
                lst_collector.append(mapped_lst[i])
            i += 1

        max_el_2 = max(lst_collector)

    return max_el_1, max_el_2


if __name__ == '__main__':
    string = '''
    2
0 1
    '''
    print(count_permut(string))
