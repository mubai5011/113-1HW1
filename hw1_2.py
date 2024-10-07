def reverse_number(num:int)->int:
    reversed_num=str(num)[::-1]
    return int(reversed_num)

input_number=int(input("請輸入一個數字:"))
output_number=reverse_number(input_number)
print(output_number)

