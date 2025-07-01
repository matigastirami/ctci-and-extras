import pprint

image = [
    ['R', 'R', 'R', 'R', 'B'],
    ['R', 'R', 'R', 'G', 'R'],
    ['R', 'G', 'G', 'R', 'B'],
    ['R', 'G', 'R', 'B', 'B'],
    ['R', 'G', 'B', 'B', 'B'],
]

def paint_fill(image, r, c, new_color, old_color = None):
    if (r < 0
        or r >= len(image)
        or c >= len(image[0])
        or image[r][c] == new_color):
        return

    if old_color is None:
        old_color = image[r][c]

    if image[r][c] == old_color:
        image[r][c] = new_color
        paint_fill(image, r + 1, c, new_color, old_color)
        paint_fill(image, r - 1, c, new_color, old_color)
        paint_fill(image, r, c + 1, new_color, old_color)
        paint_fill(image, r, c - 1, new_color, old_color)


if __name__ == '__main__':
    print('before: ')
    pprint.pprint(image)
    paint_fill(image, 3, 1, 'Y')
    print('After: ')
    pprint.pprint(image)
