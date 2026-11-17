import cv2 as cv #image detection
import zxingcpp #decoding

img = cv.imread('testphotos/TESTIMAGE4.jpg', cv.IMREAD_GRAYSCALE)
#reads the image and applies grayscale

assert img is not None, "file could not be read, check with os.path.exists()"
#message if image isn't found

results = zxingcpp.read_barcodes(img)

for r in results:
    print(f"Text: {r.text}")
    print(f"Format: {r.format}")
    print(f"Position: {r.position}")