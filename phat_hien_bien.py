import cv2

# Đọc hình ảnh từ tệp
image = cv2.imread('anhDaXuLyNhiPhan.jpg', cv2.IMREAD_GRAYSCALE)

# Áp dụng phát hiện biên bằng phương thức Canny
edges = cv2.Canny(image, threshold1=100, threshold2=200)

# Hiển thị hình ảnh gốc và biên đã phát hiện
cv2.imshow('Before', image)
cv2.imshow('After', edges)

# Chờ người dùng nhấn một phím bất kỳ để thoát
cv2.waitKey(0)
cv2.destroyAllWindows()
