"""
Link: https://kamacoder.com/problempage.php?pid=1044

Solution: Prefix Sum.
    Time Complexity: O(n*m).
"""

def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))

    n, m = data[0], data[1]
    idx = 2
    arr = []
    sum = 0
    for i in range(n):
        row = []
        for j in range(m):
            num = data[idx]
            row.append(num)
            sum += num
            idx += 1
        arr.append(row)
    
    hori_sum = [0] * n
    for i in range(n):
        for j in range(m):
            hori_sum[i] += arr[i][j]
    
    vert_sum = [0] * m
    for j in range(m):
        for i in range(n):
            vert_sum[j] += arr[i][j]
    
    res = float('inf')
    horiCut = 0
    for i in range(n):
        horiCut += hori_sum[i]
        res = min(res, abs(sum - 2 * horiCut))
    
    vertCut = 0
    for j in range(m):
        vertCut += vert_sum[j]
        res = min(res, abs(sum - 2 * vertCut))
    
    print(res)

if __name__ == '__main__':
    main()