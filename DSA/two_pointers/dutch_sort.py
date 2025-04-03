def sort_colors(colors):
    left: int = 0
    middle: int = 0
    right: int = len(colors) - 1
    while middle <= right:
        if colors[middle] == 0:
            colors[left], colors[middle] = colors[middle], colors[left]
            left += 1
            middle += 1
        elif colors[middle] == 1:
            middle += 1
        else:
            colors[middle], colors[right] = colors[right], colors[middle]
            right -= 1
    return colors


assert sort_colors([2, 0, 1]) == [0, 1, 2]
assert sort_colors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
