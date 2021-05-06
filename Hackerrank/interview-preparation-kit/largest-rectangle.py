def largest_rectangle(h):
    k = 1
    largest_yet = 0
    area_till_now = 0

    for height in h:
        area = k * height
        area_till_now += area
        if area > largest_yet:
            area = largest_yet
    return largest_yet


def main():
    foo = largest_rectangle(h=[1, 2, 3, 4, 5])
    print(foo)


if __name__ == '__main__':
    main()
