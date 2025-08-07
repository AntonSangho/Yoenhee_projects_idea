import easyocr
import cv2
import matplotlib.pyplot as plt

reader = easyocr.Reader(['ko','en'], gpu=False)
img_path = '../img/road_sign.png'
img = cv2.imread(img_path)

# 1. 이미지 불러오기 및 표시
#plt.figure(figsize=(8, 8))
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.show()

# 2. 이미지의 텍스트 인식
result = reader.readtext(img_path)
#print("Detected text:", result)

# 3. 인식된 텍스트를 확인해보기
# 글자 앞에 있는 좌표는 차례대로 좌측 상단, 우측 상단, 우측 하단, 좌측 하측
# 마지막은 인식된 글자의 신뢰도
# 신뢰도가 0.5 이상인 것만 출력 

THRESHOLD = 0.5

for bbox, text, conf in result:
    if conf >= THRESHOLD:
        print(text)
        cv2.rectangle(img, pt1=bbox[0], pt2=bbox[2], color=(0, 255, 0), thickness=2)
    plt.figure(figsize=(8, 8))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()


print(result[1]) 
#cv2.waitKey(0)
#cv2.destroyAllWindows()