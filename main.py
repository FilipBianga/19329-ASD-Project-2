from collections import defaultdict


def heappop(heap):
    ret = heap[0]
    last = heap.pop()
    size = len(heap)
    if size == 0: return ret
    heap[0] = last
    cur = 0
    while True:
        ch1 = 2 * cur + 1
        if ch1 >= size: return ret
        ch2 = ch1 + 1
        child = ch2 if ch2 < size and heap[ch2] < heap[ch1] else ch1
        if heap[cur] <= heap[child]: return ret
        heap[child], heap[cur] = heap[cur], heap[child]
        cur = child
        pass
    pass


def heappush(heap, val):
    cur = len(heap)
    heap.append(val)
    while cur > 0:
        parent = (cur - 1) // 2
        if heap[parent] <= heap[cur]: break
        heap[cur], heap[parent] = heap[parent], heap[cur]
        cur = parent
        pass
    pass


def heapify(arr, n, i):
    # Znajdź największy wśród korzeni i dzieci
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Jeśli root nie jest największy, zamień z największym i kontynuuj heapifing
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Zbuduj maksymalny kopiec
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)


def convert(example):
    # Tworzenie heap
    heap = [[wt, [sym, ""]] for sym, wt in example.items()]
    heapSort(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


# wczytanie tekstu
with open('ipsum.txt', 'r') as file:
    tekst = file.read().replace('\n', '')

# Defining the dict
example = defaultdict(int)
for i in tekst:
    example[i] += 1
# print(example)
text_to_convert = convert(example)

file = open('ipsum_convert.txt', 'w')
print("Dane wyświetlane w kolejności: Znak, Ilość powtarzająca się poszczególnego znaku w tekście, kod\n")
for j in text_to_convert:
    file.write("%s\t\t%s\t%s\n" % (j[0], example[j[0]], j[1]))
    print("%s\t\t%s\t%s\n" % (j[0], example[j[0]], j[1]))

file.close()
