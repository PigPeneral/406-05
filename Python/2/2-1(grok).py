def get_valid_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            n = input(prompt)
            if not n.strip():
                print("輸入不可為空，請重新輸入！")
                continue
            n = int(n)
            if (min_val is not None and n < min_val) or (max_val is not None and n > max_val):
                print(f"請輸入 {min_val} 到 {max_val} 之間的數字！")
                continue
            return n
        except ValueError:
            print("無效數值，請重新輸入！")

def print_row(start_spaces, num_elements, width):
    print("　" * start_spaces, end="")
    print("●" * num_elements, end="")
    print("　" * (width - start_spaces - num_elements))

def tri_left(ss, c, lev, width):
    if c == 1:  # 向下遞增
        print_row(0, lev - ss, width)
    elif c == 2:  # 向下遞減
        print_row(0, ss + 1, width)

def tri_mid(ss, c, lev, width):
    if c == 1:  # 向下遞增
        print_row(ss, 2 * (lev - ss) - 1, width)
    elif c == 2:  # 向下遞減
        print_row(ss, 2 * (ss + 1) - 1, width)

def tri_right(ss, c, lev, width):
    if c == 1:  # 向下遞增
        print_row(ss, lev - ss, width)
    elif c == 2:  # 向下遞減
        print_row(width - (ss + 1), ss + 1, width)

def tri_setup(op, c, lev, width):
    for i in range(1, lev + 1):
        ss = lev - i
        if op == 1:
            tri_left(ss, c, lev, width)
        elif op == 2:
            tri_mid(ss, c, lev, width)
        elif op == 3:
            tri_right(ss, c, lev, width)
        print()

def main():
    while True:
        op = get_valid_input("選擇排版類型：(1)置左 (2)置中 (3)置右 (0)結束程式　", 0, 3)
        if op == 0:
            break
        c = get_valid_input("選擇排列方式：(1)向下遞增 (2)向下遞減 (0)返回　", 0, 2)
        if c == 0:
            continue
        lev = get_valid_input("輸入高度:　", 1, 20)
        width = 2 * lev - 1
        tri_setup(op, c, lev, width)

if __name__ == '__main__':
    main()