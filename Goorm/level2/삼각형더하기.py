import sys
input_ = sys.stdin.readline


def det_triangle_shape(ys, xs):
    ys.sort()
    xs.sort()
    
    type_y = ""
    if ys[0] < ys[1] == ys[2]:
        type_y = "bottom"
    elif ys[0] == ys[1] < ys[2]:
        type_y = "top"
    
    type_x = ""
    if xs[0] == xs[1] < xs[2]:
        type_x = "left"
    elif xs[0] < xs[1] == xs[2]:
        type_x = "right"
        
    return f"{type_y}&{type_x}"
    

def inner_sum(arr, ys, xs, types):
    min_y, max_y = min(ys), max(ys)
    min_x, max_x = min(xs), max(xs)
    
    result = 0
    if types == "bottom&left":
        for i in range(max_y, min_y-1, -1):
            for j in range(min_x, max_x+1):
                result += arr[i][j]
            max_x -= 1
    elif types == "bottom&right":
        for i in range(max_y, min_y-1, -1):
            for j in range(min_x, max_x+1):
                result += arr[i][j]
            min_x += 1
    elif types == "top&left":
        for i in range(min_y, max_y+1):       # row
            for j in range(min_x, max_x+1):   # col
                result += arr[i][j]
            max_x -= 1
    elif types == "top&right":
        for i in range(min_y, max_y+1):
            for j in range(min_x, max_x+1):
                result += arr[i][j]
            min_x += 1

    return result


if __name__ == '__main__':
    N, Q = map(int, input_().strip().split())   # N: 배열의 크기, Q: 삼각형 개수
    arr = [list(map(int, input_().strip().split())) for _ in range(N)]

    for _ in range(Q):
        vertices = list(map(int, input_().strip().split()))
        vertices = [vertex - 1 for vertex in vertices]
        ys, xs = vertices[::2], vertices[1::2]
        types = det_triangle_shape(ys, xs)
        print(inner_sum(arr, ys, xs, types))
