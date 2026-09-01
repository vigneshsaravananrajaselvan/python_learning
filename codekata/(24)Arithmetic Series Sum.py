import sys
def arithmetic_series_sum():
    input= sys.stdin.read().split()
    if not input :
        return
    a=int(input[0])
    b=int(input[1])
    c=int(input[2])
    sum=(c*(2*a+(c-1)*b))//2
    print(sum)
if __name__ == "__main__":
    arithmetic_series_sum()