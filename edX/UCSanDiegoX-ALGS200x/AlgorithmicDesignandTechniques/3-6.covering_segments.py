# Uses python3
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    # write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *data = map(int, input.split())
    # segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    segments = [
        Segment(start=1, end=3,),
        Segment(start=2, end=5,),
        Segment(start=3, end=6,),
    ]
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
