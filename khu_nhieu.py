import cv2

# Đọc hình ảnh từ tệp
image = cv2.imread('biensoxe.jpg')

# Áp dụng Gaussian Blur để khử nhiễu
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Lưu hình ảnh đã khử nhiễu vào bộ nhớ
cv2.imwrite('khu_nhieu_image.jpg', blurred_image)

# Hiển thị hình ảnh gốc và hình ảnh đã khử nhiễu
cv2.imshow('Ảnh Trước', image)
cv2.imshow('Ảnh Sau', blurred_image)

# Chờ người dùng nhấn một phím bất kỳ để thoát
cv2.waitKey(0)
cv2.destroyAllWindows()
