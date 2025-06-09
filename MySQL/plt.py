#import
import matplotlib.pyplot as plt
import random as rng
import timeit

#def
def main():

    the_list = rlg()
    unsorted_list = list(the_list)

#quick sort
    print("list to sort:")
    print(unsorted_list)
    start = timeit.default_timer()
    sorted_list = quick(the_list)
    end = timeit.default_timer()
    print(sorted_list)
    sort_time = round(end - start, 3)
    print(sort_time)

    plt.rcParams["font.sans-serif"] = "mingliu"
    plt.rcParams["axes.unicode_minus"] = False
    plt.title("Quick Sort")
    plt.xlabel(f"花費時間{sort_time}秒")
    plt.plot(unsorted_list)
    plt.plot(sorted_list)
    plt.show()

#python(tim)
    unsorted_list = list(the_list)
    print("list to sort:")
    print(unsorted_list)
    start = timeit.default_timer()
    sorted_list = sorted(the_list)
    end = timeit.default_timer()
    print(sorted_list)
    sort_time = round(end-start, 3)
    print(sort_time)

    plt.rcParams["font.sans-serif"] = "mingliu"
    plt.rcParams["axes.unicode_minus"] = False
    plt.title("Tim Sort")
    plt.xlabel(f"花費時間{sort_time}秒")
    plt.plot(unsorted_list)
    plt.plot(sorted_list)
    plt.show()

#bubble sort
    unsorted_list = list(the_list)
    print("list to sort:")
    print(unsorted_list)
    start = timeit.default_timer()
    bubble(the_list)
    end = timeit.default_timer()
    print(the_list)
    sort_time = round(end-start, 3)
    print(sort_time)

    plt.rcParams["font.sans-serif"] = "mingliu"
    plt.rcParams["axes.unicode_minus"] = False
    plt.title("Bubble Sort")
    plt.xlabel(f"花費時間{sort_time}秒")
    plt.plot(unsorted_list)
    plt.plot(sorted_list)
    plt.show()

#random list generate
def rlg():
    n = 20000
    unsorted_list = []
    for i in range(n):
        j = rng.randint(0,20000)
        unsorted_list.append(j)
    return unsorted_list

#bubble sort (from internet)
def bubble(list):
    n = len(list)
    for i in range(n):
        swapped = False  # 假設本次遍歷中沒有進行交換
        for j in range(0, n - i - 1):
            # 比較相鄰的元素
            if list[j] > list[j + 1]:
                # 如果左邊的元素大於右邊的元素，則交換它們的位置
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True  # 表示進行了交換

        # 如果在本次遍歷中沒有進行任何交換，則數列已經排序完成，提前退出
        if not swapped:
            break

#quick sort (from internet)
def quick(list):
    if len(list) <= 1:
        return list
    left = []
    right = []
    piv = []
    pivot = rng.choice(list)
    for val in list:
        if val == pivot:
            piv.append(val)
        elif val < pivot:
            left.append(val)
        else:
            right.append(val)
    return quick(left) + piv + quick(right)

#main
if __name__ == '__main__':
    main()