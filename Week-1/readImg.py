#Sử dụng OpenCV để đọc 1 ảnh có đường dẫn là string thứ nhất, in ra thông báo lỗi nếu ảnh không tồn tại tại đường dẫn đó.

import validateInput
import sys
import cv2

path1 = sys.argv[1];
img = cv2.imread(path1)

if(img is None):
    print("Không tồn tại ảnh theo đường dẫn")
else:
    cv2.imshow("cat", img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()



