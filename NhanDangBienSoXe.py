import cv2
import pytesseract

# Bước 1: Đọc ảnh biển số xe
image = cv2.imread('biensonumberplate.jpg')

# Bước 2: Tiền xử lý ảnh
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 150)

# Bước 3: Phát hiện biển số xe
contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
number_plate = None

for contour in contours:
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

    if len(approx) == 4:
        number_plate = approx
        break

# Bước 4: Phân đoạn biển số xe
x, y, w, h = cv2.boundingRect(number_plate)
plate = gray[y:y + h, x:x + w]

# Bước 5: Nhận dạng ký tự (sử dụng Tesseract OCR)
custom_config = r'--oem 3 --psm 6'  # Cấu hình Tesseract OCR
number = pytesseract.image_to_string(plate, config=custom_config)

# Bước 6: Trích xuất dãy số biển số xe và hiển thị
print("Dãy số biển số xe: ", number)

# Hiển thị ảnh và dãy số biển số
cv2.imshow("Number Plate", plate)
cv2.waitKey(0)
cv2.destroyAllWindows()
