import sys
def counting_digit_of_number():
    input_data=sys.stdin.read().strip()
    if not input_data:
        return
    print(len(input_data))
if __name__=="__main__"   :
    counting_digit_of_number()
