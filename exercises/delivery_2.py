import sys

def get_delivery(x):
    string = sys.stdin.read().splitlines()
    n, m, T = map(int, string[0].split())
    goods = list(map(int, string[1:]))
    if n != len(goods):
        return 1
    deliv_count = 0
    sorted_time = sorted(goods)
    i = 0
    st = []
    while i < n:
        st.sort()
        if st and st[0] < sorted_time[i]:
            st = []
            deliv_count += 1
        st.append(sorted_time[i] + T)
        if len(st) == m:
            st = []
            deliv_count += 1
        i += 1
    deliv_count += (len(st) > 0)
    print(deliv_count)

if __name__=='__main__':
    x ='''
   8 3 4
7
2
11
9
12
13
8
7
    '''
    get_delivery(x)