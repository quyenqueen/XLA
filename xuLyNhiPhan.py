import cv2

# Đọc hình ảnh từ tệp
image = cv2.imread('biensoxe.jpg', cv2.IMREAD_GRAYSCALE)

# Áp dụng phân ngưỡng nhị phân (binary threshold)
# Ở đây, ta sử dụng phân ngưỡng đơn giản với giá trị 128 làm ngưỡng
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# Lưu hình ảnh đã khử nhiễu vào bộ nhớ
cv2.imwrite('anhDaXuLyNhiPhan.jpg', binary_image)


# Hiển thị hình ảnh gốc và hình ảnh nhị phân
cv2.imshow('Original Image', image)
cv2.imshow('Binary Image', binary_image)

# Chờ người dùng nhấn một phím bất kỳ để thoát
cv2.waitKey(0)
cv2.destroyAllWindows()
