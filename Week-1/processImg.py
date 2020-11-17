# Sử dụng OpenCV và Numpy để chuyển ảnh thành đen trắng, sau đó giảm kích thước ảnh còn 1 nửa (1 nửa chiều cao, 1 nửa chiều rộng). sau đó quay ảnh 90 độ sang trái hoặc phải tùy ý. In ra thông báo lỗi nếu đường dẫn để lưu không khả dụng (không có quyền ghi hoặc đường dẫn không khả dụng
# Lưu ảnh vào đường dẫn là string thứ 2.

import sys
import cv2
import os


def isValidInput(arr):
    print(arr)
    if(len(arr) < 2):
        print("Không đủ tham số")
        exit()
    elif len(arr) > 2:
        print("Thừa tham số")
        exit()
    else:
        print("Tham số hợp lệ")


def process():
    arr = sys.argv[1:]
    isValidInput(arr)
    path1 = arr[0]
    path2 = arr[1]
    img = cv2.imread(path1)

    # Kiểm tra tính hợp lệ của đường dẫn (tồn tại đường dẫn và có quyền ghi)
    if(os.path.isdir(path2) == False and os.access(path2, os.W_OK) == False):
        print("Đường dẫn để lưu không khả dụng")
        exit()

    if(img is None):
        print("Không tồn tại ảnh theo đường dẫn")
    else:
        cv2.imshow("cat", img)
        # heights, widths = img.shape # if read gray
        heights, widths, channels = img.shape  # if read gray
        print(heights, widths)
        # Giảm kích thước ảnh còn 1 nửa
        heights //= 2
        widths //= 2
        img_resize = cv2.resize(img, (widths, heights))
        # cv2.imshow("Resize", img_resize)

        # Xoay ảnh ngược chiều kim đồng hồ
        img_rotate = cv2.rotate(img_resize, cv2.ROTATE_90_COUNTERCLOCKWISE)
        # cv2.imshow("Rotate", img_rotate)

        # Chuyển ảnh sang sạng gray
        img_gray = cv2.cvtColor(img_rotate, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray", img_gray)

        # Chuyển ảnh dạng đen trắng
        (thresh, img_black_white) = cv2.threshold(
            img_gray, 127, 255, cv2.THRESH_BINARY)
        cv2.imshow("Gray", img_black_white)
        # Ghi ảnh
        cv2.imwrite(os.path.join(
            path2, "img_after_process.jpg"), img_black_white)

        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    process()
