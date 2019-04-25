# def largestlowest(matrix):
#         largeset = 0
#         lowest = 0
#
#         for row in range(len(matrix)):
#             for col in range(len(matrix[row]-1)):
#                 if matrix[col] > matrix[col+1]:
#                     largest = matrix[col]
#             if matrix[col] < matrix[col+1]:
#                 lowest = matrix[col]
#         else:
#             print("there is no min/max value")
#             return largest and lowest
#
# print(largestlowest([[4,8,2,9,34,57,22,44], [1,2,8,9,1,2,55,3,22,4]]))
def largestlowest(matrix):
        # Declaring biggest and smallest variable
        largest = 0
        lowest = 0

        # Loop through every array in the matrix as you have defined it
        for row in matrix:
            # Loop through each item in the array
            for item in row:
                # If it is bigger than the largest, set the largest to be that value
                if item > largest:
                    largest = item
                # If it is smaller than the smallest, set the smallest to be that value
                if item < lowest:
                    lowest = item

        # Return the largest and lowest
        return largest, lowest
print(largestlowest([[4,8,2,9,34,57,22,44], [1,2,8,9,1,2,55,3,22,4]]))
