# Viết 1 phần mềm dòng lệnh nhận vào 2 tham số là 2 string
# In ra thông báo lỗi khi người dùng nhập sai (không đủ tham số, thừa tham số)

import sys

def isValidInput(arr):
    """
    Check input: Not empty, don't contain space in string
    """
    print(arr)
    if(len(arr) < 2):
        print("Không đủ tham số")
    elif len(arr) > 2:
        print("Thừa tham số")
    else:
        print("Tham số hợp lệ")

isValidInput(sys.argv[1:])


