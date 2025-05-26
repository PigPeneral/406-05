def tri_left_fixed(current_row, level):
    """靠左對齊 - 簡化版本"""
    elements_count = current_row  # 第幾行就有幾個元素
    for j in range(elements_count):
        print("●", end="")
        if j < elements_count - 1:  # 不是最後一個元素就加空格
            print("　", end="")


def tri_mid_fixed(current_row, level):
    """置中對齊 - 簡化版本"""
    width = 2 * level - 1
    space = level - current_row  # 左邊需要的空格數

    for col in range(width):
        if space <= col < width - space:  # 在有效範圍內
            position = col - space
            if position % 2 == 0:  # 偶數位置印元素
                print("●", end="")
            else:
                print("　", end="")
        else:
            print("　", end="")


def tri_right_original(current_row, level):
    """你原本的tri_right邏輯"""
    width = 2 * level - 1
    elements_count = current_row  # 這裡有問題！

    for col in range(width):
        posit = width - 1 - col  # 從右邊開始算位置
        if posit < elements_count * 2 - 1:
            if posit % 2 == 0:
                print("●", end="")
            else:
                print("　", end="")
        else:
            print("　", end="")


def tri_right_fixed(current_row, level):
    """修正後的tri_right"""
    width = 2 * level - 1
    elements_count = current_row

    # 方法1：從右邊開始放置元素
    for col in range(width):
        # 計算從右邊開始的相對位置
        right_position = width - 1 - col

        # 這一行應有的元素範圍：最右邊的 (current_row * 2 - 1) 個位置
        if right_position < current_row * 2 - 1:
            if right_position % 2 == 0:  # 偶數位置放元素
                print("●", end="")
            else:
                print("　", end="")
        else:
            print("　", end="")


def tri_right_alternative(current_row, level):
    """另一種思路：先算出要印幾個空格，再印元素"""
    width = 2 * level - 1
    left_spaces = width - (current_row * 2 - 1)  # 左邊空格數

    # 印左邊的空格
    for _ in range(left_spaces):
        print("　", end="")

    # 印元素部分（交替印●和空格）
    for j in range(current_row * 2 - 1):
        if j % 2 == 0:
            print("●", end="")
        else:
            print("　", end="")


# 測試所有函數
def test_all_alignments():
    level = 3

    print("=== 靠左對齊 ===")
    for i in range(1, level + 1):
        tri_left_fixed(i, level)
        print()

    print("\n=== 置中對齊 ===")
    for i in range(1, level + 1):
        tri_mid_fixed(i, level)
        print()

    print("\n=== 你原本的靠右對齊 ===")
    for i in range(1, level + 1):
        tri_right_original(i, level)
        print()

    print("\n=== 修正後的靠右對齊（方法1）===")
    for i in range(1, level + 1):
        tri_right_fixed(i, level)
        print()

    print("\n=== 修正後的靠右對齊（方法2）===")
    for i in range(1, level + 1):
        tri_right_alternative(i, level)
        print()


# 執行測試
test_all_alignments()

print("\n" + "=" * 50)
print("邏輯說明：")
print("靠左：直接印出當前行數量的元素")
print("置中：計算左右空格，中間部分交替印元素和空格")
print("靠右：方法1 - 從右邊開始計算位置")
print("靠右：方法2 - 先印左邊空格，再印元素部分")