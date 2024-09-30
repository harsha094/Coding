def find_indices_in_descending_order(f, focal_lengths):
    # Create pairs of (value, index)
    indexed_focal_lengths = [(focal_lengths[i], i) for i in range(f)]

    # Sort the pairs by value in descending order
    indexed_focal_lengths.sort(key=lambda x: x[0], reverse=True)

    # Extract the indices
    result_indices = [index for value, index in indexed_focal_lengths]

    # Print the indices
    print(*result_indices)

# Input processing
f = int(input())
focal_lengths = list(map(int, input().split()))

# Find indices in descending order
find_indices_in_descending_order(f, focal_lengths)


'''

Sample Input :
3
1 5 4
Sample Output :
1 2 0

'''