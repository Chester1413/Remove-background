import cv2
import os

def resize_and_pad(image_path, output_path, target_width, target_height):
    # 讀取圖片
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to read image {image_path}")
        return

    h, w = image.shape[:2]

    # 計算縮放比例
    scale = min(target_width / w, target_height / h)
    new_w = int(w * scale)
    new_h = int(h * scale)

    # 縮放圖片
    resized_image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # 創建一個新的圖片，並填充背景
    result = cv2.copyMakeBorder(
        resized_image,
        top=(target_height - new_h) // 2,
        bottom=(target_height - new_h + 1) // 2,
        left=(target_width - new_w) // 2,
        right=(target_width - new_w + 1) // 2,
        borderType=cv2.BORDER_CONSTANT,
        value=[255, 255, 255]  # 背景顏色設為白色
    )

    # 保存圖片
    cv2.imwrite(output_path, result)

def batch_resize_and_pad(input_folder, output_folder, target_width, target_height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg','JPG', '.jpeg', '.png', '.bmp', '.tiff')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            resize_and_pad(input_path, output_path, target_width, target_height)

# 使用範例
input_folder = r'C:\Users\Mike\Desktop\IMG\IBC COUPLING'
output_folder = r'C:\Users\Mike\Desktop\IMG\IBC COUPLING\resized'
batch_resize_and_pad(input_folder, output_folder, 640, 460)
