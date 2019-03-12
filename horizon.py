'''
One fine day, Jack decided to complete his assignment of summer vacation, to draw the view of the city which he gets from his room's window. He tried so many times but he was not able to differentiate between the buildings. So he decided to ask you to make a program which will give him the horizon [an outline of land and buildings defined against the sky] coordinates of the city.

Suppose there are N rectangular buildings in a 2-dimensional city and your computer program will compute the horizon of these buildings, eliminating hidden lines. His main purpose behind this is to view the buildings from a side and remove all sections that are not visible.

Considering city to be in plain land and all buildings share common ground. Every building is represented by triplet (Length, height, breath).
Length: is x coordinate of left side (or wall).
Height: is height of building.
Breath: is x coordinate of right side

Consider building illustrated below is represented as (1, 11, 5) i.e. Length = 1, Height = 11 and Breadth= 5




Considering that computer program returns the coordinates of horizon which include the outline of the visible buildings that starts and ends at the ground level.

Let's consider Jack gets a view of 4 buildings. So he feeds coordinate of each building as the input of the program and program will return a string array having coordinates to draw the horizon.

The coordinates that jack provide will be,
(2, 9, 6), (3, 11, 8), (7, 13, 9), (1, 1, 1)

Input is a one dimensional array where A[i] Where i is equal to number of buildings
The output returned by the program is
(1,0), (1, 1), (2, 9), (3, 11), (7, 13), (9,0)

City view with given input coordinate and its output is shown below-

                                               Input                                                                                                    Output


Make a program which Jack can use to get horizon co-ordinate of the city.

Note :
1. Ignore the buildings that have equal x coordinate of left side and x coordinate right side
2. Ignore the buildings with height 0(zero).


Input Format
First line contains N having number of co-ordinates
Each of the next N lines contains a string describing a co-ordinates of a building as
< length of building-1 >#< height of building-1 >#< breadth of building-1 >


Constraints
1 <= |S| <= 10^3
1 <= Height <= 50


Output Format
Print all the the horizon coordinates.

Sample TestCase 1
Input
'''


def cord(arr):

    l = [a[0] for a in arr]
    h = [a[1] for a in arr]
    b = [a[2] for a in arr]
    all_val = []
    # print(l, b, h)
    max_val = max(b)
    min_val = min(l)

    for i, v in enumerate(arr):
        for r in range(l[i], b[i] + 1):
            all_val.append([r, h[i]])
    # print(all_val)
    count = {}

    for li in l:
        count[li] = [x[1] for x in all_val if x[0] == li]
    for bi in b:
        if bi not in l:
            count[bi] = [x[1] for x in all_val if x[0] == bi]

    arr.sort(key=lambda x: x[1], reverse=True)

    m = arr[0][0]
    n = arr[0][2]
    pts = []
    m1 = m
    m2 = n

    while m1 >= min_val:
        if m1 in count:
            print(m1)
            val = max(count[m1])
            pts.append([m1, val])
        m1 = m1 - 1
    while m2 < max_val:
        if m2 in count:
            val = min(count[m2])
            pts.append([m2, val])
        m2 = m2 + 1
    pts.append([min_val, 0])
    pts.append(([max_val, 0]))
    pts.sort()
    for i, v in enumerate(pts):
        if v[0] <= n and v[0] != min_val:
            if v[1] == pts[i - 1][1]:
                del pts[i]
        elif v[0] > m:
            if v[1] == pts[i - 1][1]:
                print(v)
                del pts[i - 1]

    print(pts)


if __name__ == '__main__':
    num = int(input())
    a = []
    for i in range(num):
        a.append([int(x) for x in input().split('#')])
    cord(a)
