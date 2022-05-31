import random

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

def bubble_sort(l):
    for i in range(len(l)-1):
        already_sorted = True
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
                already_sorted = False
        if already_sorted:
            return None

def insertion_sort(l):
    for i in range(len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                temp = l[j]
                l[j] = l[j-1]
                l[j-1] = temp
            else:
                break

def merge_sort(l):
    if len(l)<2:
        return None
    left_l = l[ : int(len(l)/2)]
    right_l = l[int(len(l)/2) : ]
    merge_sort(left_l)
    merge_sort(right_l)

    lp, rp = 0, 0
    while lp<len(left_l) or rp<len(right_l):
        if lp==len(left_l):
            l[lp+rp] = right_l[rp]
            rp += 1
        elif rp==len(right_l):
            l[lp+rp] = left_l[lp]
            lp += 1
        elif left_l[lp] <= right_l[rp]:
            l[lp+rp] = left_l[lp]
            lp += 1
        else:
            l[lp+rp] = right_l[rp]
            rp += 1

    return None

def quick_sort(l, start:int=0, end:int=None):
    if end is None:
        end = len(l)-1
    
    if end < start:
        return None

    # randomize partition element selection to minimize chance of worst case n^2
    part_elem_idx = random.randint(start, end)
    temp = l[end]
    l[end] = l[part_elem_idx]
    l[part_elem_idx] = temp
    
    part_elem = l[end]
    part_idx = start
    for i in range(start, end):
        if l[i] <= part_elem:
            temp = l[i]
            l[i] = l[part_idx]
            l[part_idx] = temp
            part_idx += 1
    temp = l[part_idx]
    l[part_idx] = l[end]
    l[end] = temp

    quick_sort(l, start, part_idx-1)
    quick_sort(l, part_idx+1, end)
