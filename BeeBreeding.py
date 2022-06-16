from operator import sub


def shortest_distance(first_num: int, last_num: int, spiral=[[0, 0, 0] * 2]):
    transforms = ((1, 0, -1), (1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1))

    for number in range(max(first_num, last_num)):
        for index, values in enumerate(transforms):

            for k in range(number - (index == 1)):
                spiral.append(list(map(sum, list(zip(spiral[-1], values)))))

    distance = max(list(map(abs, list(map(sub, *[spiral[last_num], spiral[first_num]])))))
    print("shotest distance of the two nodes is :", distance - 1)


first_num = int(input("Enter the first number :"))
last_num = int(input("Enter the last number :"))

shortest_distance(first_num, last_num)