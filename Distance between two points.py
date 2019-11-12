import math
def distance(x1, y1, x2, y2):
    dist = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    return float("{0:.2f}".format(dist))

