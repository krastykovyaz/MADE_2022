def multiple_push_back():
    n, m, k = map(int, input().split())

    mapped_list = list(map(int, input().split()))

    l1 = []
    for i in range(m):
        l1.append(list(map(int, input().split())))
    counter = {}
    for item in mapped_list:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1
    l2 = []
    for key, value in counter.items():
        l2.append([value, key])

    l1 += l2
    l1.sort(key=lambda x: x[1])

    for i in l1:
        k -= i[0]
        if k <= 0:
            break
    return i[1]


if __name__ == '__main__':
    print(multiple_push_back())
