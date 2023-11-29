import cv2

# Đọc hình ảnh
image = cv2.imread("bienxe.jpg")
img = cv2.resize(image, (640, 480))
# Chuyển ảnh thành ảnh xám
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Khử nhiễu ảnh 
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)


# Khởi tạo ngưỡng ban đầu và ngưỡng cuối cùng
initial_threshold = 100
final_threshold = 220

# Duyệt qua các ngưỡng từ ngưỡng ban đầu đến ngưỡng cuối cùng
for threshold in range(initial_threshold, final_threshold + 1):
    # Áp dụng ngưỡng để tách vùng biển số
    _, thresholded_image = cv2.threshold(blurred_img, threshold, 255, cv2.THRESH_BINARY)

    # Lưu hình ảnh vùng biển số với ngưỡng hiện tại
    final_thresholded_image = thresholded_image

# Hiển thị hình ảnh vùng biển số với ngưỡng cuối cùng
cv2.imshow(f"Threshold {final_threshold}", final_thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
