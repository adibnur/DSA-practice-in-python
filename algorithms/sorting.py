def selection_sort(l, reverse=False):
    for i in range(len(l)):
        min_idx = i
        for j in range(i, len(l)):
            if not reverse:
                if l[j] < l[min_idx]:
                    min_idx = j
            else:
                if l[j] > l[min_idx]:
                    min_idx = j
        temp = l[i]
        l[i] = l[min_idx]
        l[min_idx] = temp
