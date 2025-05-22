def print_pyramid(height):
    """
    打印一個金字塔，第n行有n個元素，且元素置中

    Args:
        height: 金字塔的高度（行數）
    """
    # 計算最後一行的元素數量，用於計算置中所需的空格
    max_elements = height

    for row in range(1, height + 1):
        # 計算當前行需要的空格數來實現置中效果
        spaces = (max_elements - row) // 2

        # 打印前置空格
        for _ in range(spaces):
            print("　", end="")

        # 打印當前行的元素
        for _ in range(row):
            print("。", end="")

        # 換行
        print()

# 測試不同高度的金字塔
print("高度為3的金字塔:")
print_pyramid(3)

print("\n高度為5的金字塔:")
print_pyramid(5)

print("\n高度為7的金字塔:")
print_pyramid(7)


def print_special_pyramid(height):
    """
    打印一個特殊的金字塔，其中元素「●」和空格「○」交替出現
    每行的總寬度為 2*height-1

    Args:
        height: 金字塔的高度（行數）
    """
    width = 2 * height - 1  # 計算總寬度

    for row in range(1, height + 1):
        # 計算每行開頭的空格數（○）
        start_spaces = height - row

        for col in range(width):
            # 如果在當前行的有效範圍內
            if col >= start_spaces and col < width - start_spaces:
                # 判斷應該打印元素還是空格
                # 從該行的第一個位置開始算，偶數位置（0-based）打印空格，奇數位置打印元素
                position = col - start_spaces
                if position % 2 == 0:
                    print("●", end="")
                else:
                    print("○", end="")
            else:
                print("○", end="")

        # 換行
        print()


# 測試不同高度的金字塔
print("高度為3的金字塔:")
print_special_pyramid(3)

print("\n高度為4的金字塔:")
print_special_pyramid(4)

print("\n高度為5的金字塔:")
print_special_pyramid(5)
