
# ================= GLOBAL ============= #
oo = int(1e18)


# ================= FUNCTIONS =========== #
def built_tree(lst: list, tree: list, l, r, index=1) -> int:
    if r < l:
        return oo
    if r == l:
        tree[index] = lst[l]
        return tree[index]
    mid = (l+r)//2
    tree[index] = min(built_tree(lst, tree, l, mid, index*2), built_tree(lst, tree, mid+1, r, index*2+1))
    return tree[index]


def find(tree: list, l: int, r: int, ql: int, qr: int, index=1):
    if r < ql or l > qr:
        return oo
    if ql <= l and qr >= r:
        return tree[index]

    mid = (l+r) // 2
    return min(find(tree, l, mid, ql, qr, index*2), find(tree, mid+1, r, ql, qr, index*2+1))


def update_range(tree: list, l: int, r: int, s: int, e: int, u_list: list, index=1):
    if l == r and s <= l <= e:
        tree[index] = u_list[l-s]
        return tree[index]
    if l > r:
        return oo
    if e < l or s > r:
        return tree[index]

    mid = (r+l) // 2
    tree[index] = min(update_range(tree, l, mid, s, e, u_list, index*2), update_range(tree, mid+1, r, s, e, u_list, index*2+1))
    return tree[index]


def update(tree: list, l: int, r: int, u_index: int, val: int, index=1) -> int:
    if l == r and l == u_index:
        tree[index] = val
        return val
    if u_index > r or u_index < l:
        return tree[index]
    if l > r:
        return oo

    mid = (r+l)//2
    tree[index] = min(update(tree, l, mid, u_index, val, index*2), update(tree, mid+1, r, u_index, val, index*2+1))
    return tree[index]


# ============== MAIN ============ #
if __name__ == '__main__':
    lst = [1, 3, 2, -5, 4, 6]
    tree = [oo]*(len(lst)*4+1)
    built_tree(lst, tree, 0, len(lst)-1)
    print(tree)
    # update(tree, 0, len(lst)-1, 3, 5)
    up = [3, 4, 5]
    update_range(tree, 0, len(lst)-1, 3, 5, up)  # [1, 3, 2, 3, 4, 5]
    print(tree)
    while True:
        x, y = [int(i) for i in input().split()]
        res = find(tree, 0, len(lst)-1, x, y)
        print(res)

