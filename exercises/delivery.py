import re
def get_delivery(x):
    digit_list = re.findall('\d+', x)
    digit_list = [int(d) for d in digit_list]
    goods = digit_list[3:]
    n, m, T = digit_list[0], digit_list[1], digit_list[2]
    if n != len(goods):
        return 1
    deliv_count = 0
    sorted_time = sorted(goods)
    i = 0
    start_time = 0 - T
    gds = 1
    while i < n:
        if gds < m:
            if sorted_time[i] in range(start_time, start_time + T):
                gds += 1
            else:
                start_time = sorted_time[i]
                gds = 1
                deliv_count += 1
        else:
            start_time = sorted_time[i]
            deliv_count += 1
            gds = 1
        i += 1

    return deliv_count

if __name__=='__main__':
    x ='''
   4 4 3
1
2
3
4
    '''
    print(get_delivery(x))