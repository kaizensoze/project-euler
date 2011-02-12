
maxSum = 0
triangle = []
maxSumTriangle = []

rows = [x.strip() for x in open('../triangle.txt')]

for row in rows:
    if len(row.strip()) > 1:
        triangle.append([int(col) for col in row.split()])
        maxSumTriangle.append([int(col) for col in row.split()])

for row in range((len(triangle)-1), 0-1, -1):
    for col in range(len(triangle[row])):
        # left
        if (row-1) >= 0 and (col-1) >= 0:
            newSum = maxSumTriangle[row][col] + triangle[row-1][col-1]
            if newSum > maxSumTriangle[row-1][col-1]:
                maxSumTriangle[row-1][col-1] = newSum
            
        # right
        if (row-1) >= 0 and col >= 0 and col < len(triangle[row-1]):
            newSum = maxSumTriangle[row][col] + triangle[row-1][col]
            if newSum > maxSumTriangle[row-1][col]:
                maxSumTriangle[row-1][col] = newSum

# debugging code
#for row in range(len(triangle)):
#    for col in range(len(triangle[row])):
#        print(triangle[row][col], end=" ") 
#    print('\n')

print(maxSumTriangle[0][0])