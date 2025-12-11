"""
Link: https://kamacoder.com/problempage.php?pid=1070

Solution: Prefix Sum.
"""

def main():
    size = int(input())
    nums = []
    sum = [0]
    for _ in range(size):
        cur_num = int(input())
        nums.append(cur_num)
        sum.append(sum[-1] + cur_num)
    
    while True:
        try:
            line = input()
            l, r = map(int, line.split())
            res = sum[r + 1] - sum[l]
            print(res)
        except EOFError:
            break

if __name__ == '__main__':
    main()