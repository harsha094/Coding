x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
# if The slope between point A and B should be equal to the slope between point B and C
if (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2):
    print('yes')
else:
    print('no')
# or by Area Determinant approach Area = 0.5×(x1×(y2−y3)+x2×(y3−y1)+x3×(y1−y2)) if Area = 0 then yes else no
'''
Sample Testcase :
INPUT
0 1
0 0
0 2
OUTPUT
yes

'''