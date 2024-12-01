def consecutive_same_string(N, K, strings):
    # if k is equal to 1 than if just need to check if any duplicate exists
    if K == 1:
        return "yes" if len(set(strings)) < len(strings) else "no"
    #Check for the K consecutive same strings
    for i in range(N - K + 1):
        # check if the next k string are same by string extract
        if len(set(strings[i:i+K])) == 1:
            return "yes"
    #no k consecutive string found
    return "no"

N, K = map(int, input().split())
# Read N strings
strings = []
for _ in range(N):
    strings.append(input().strip())

#print Output
print(consecutive_same_string(N, K, strings))

# Sample Testcase :
# INPUT
# 5 3
# code
# overload
# vishal
# vishal
# vishal
# OUTPUT
# yes