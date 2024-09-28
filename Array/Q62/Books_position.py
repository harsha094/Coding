def find_positions(existing_books, new_books):
    positions = []
    n = len(existing_books)

    for new_book in new_books:
        position = n + 1 #Assume it will go at the end
        for i in range(n):
            if existing_books[i] <= new_book:
                position = i + 1
                break

        positions.append(position)
    return positions
# Input Reading
n = int(input())
existing_books = list(map(int, input().split()))
m = int(input())
new_books = list(map(int, input().split()))

# Finding positions for new books
positions = find_positions(existing_books, new_books)

# Output positions
print(*positions)


'''

Sample Input :
7
95 68 62 58 55 41 30
2
45 61
Sample Output :
6 4

'''