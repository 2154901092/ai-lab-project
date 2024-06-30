import sys
import easygui as g
import cv2
import matplotlib.pyplot as plt
import easyocr
import os
# from google.colab.patches import cv2_imshow

reader = easyocr.Reader(['bn'], gpu=False)
blockstr = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
while True:
    if g.ccbox(msg="Select file path:", title="AI Lab Project"):
        image_path = g.fileopenbox(default=r"E:\Test Folder")
        if (not isinstance(image_path, str)):
            continue
        else:
            image = cv2.imread(image_path)
            output = reader.readtext(image_path, blocklist=blockstr, slope_ths=0.3, height_ths=0.7, width_ths=0.7, add_margin=0.15, x_ths=1.0, y_ths=0.7)
            string = ''        
            for detection in output:
                # print(detection)
                bounding_box, text, conf = detection
                if (conf > 0.4):
                    string = string + text + ' '
                    cv2.line(image, (int(bounding_box[0][0]), int(bounding_box[0][1])), (int(bounding_box[1][0]), int(bounding_box[1][1])), (255, 60, 0), 2)
                    cv2.line(image, (int(bounding_box[1][0]), int(bounding_box[1][1])), (int(bounding_box[2][0]), int(bounding_box[2][1])), (255, 60, 0), 2)
                    cv2.line(image, (int(bounding_box[2][0]), int(bounding_box[2][1])), (int(bounding_box[3][0]), int(bounding_box[3][1])), (255, 60, 0), 2)
                    cv2.line(image, (int(bounding_box[3][0]), int(bounding_box[3][1])), (int(bounding_box[0][0]), int(bounding_box[0][1])), (255, 60, 0), 2)
                else:
                    cv2.line(image, (int(bounding_box[0][0]), int(bounding_box[0][1])), (int(bounding_box[1][0]), int(bounding_box[1][1])), (255, 0, 240), 2)
                    cv2.line(image, (int(bounding_box[1][0]), int(bounding_box[1][1])), (int(bounding_box[2][0]), int(bounding_box[2][1])), (255, 0, 240), 2)
                    cv2.line(image, (int(bounding_box[2][0]), int(bounding_box[2][1])), (int(bounding_box[3][0]), int(bounding_box[3][1])), (255, 0, 240), 2)
                    cv2.line(image, (int(bounding_box[3][0]), int(bounding_box[3][1])), (int(bounding_box[0][0]), int(bounding_box[0][1])), (255, 0, 240), 2)
                # top_left, bottom_right = bounding_box[0], bounding_box[2]
                # x_center, y_center = (top_left[0] + bottom_right[0]) // 2, (top_left[1] + bottom_right[1]) // 2
                print(f"Confidence: {conf:.2f}, Text: {text}")

                # cv2.rectangle(image, output[0][0][0], output[0][0][2], (10, 10, 255), 2)        # How it should be
                # fix for slanted text
                # cv2.line(image, (int(bounding_box[0][0]), int(bounding_box[0][1])), (int(bounding_box[1][0]), int(bounding_box[1][1])), (10, 50, 255), 2)
                # cv2.line(image, (int(bounding_box[1][0]), int(bounding_box[1][1])), (int(bounding_box[2][0]), int(bounding_box[2][1])), (10, 50, 255), 2)
                # cv2.line(image, (int(bounding_box[2][0]), int(bounding_box[2][1])), (int(bounding_box[3][0]), int(bounding_box[3][1])), (10, 50, 255), 2)
                # cv2.line(image, (int(bounding_box[3][0]), int(bounding_box[3][1])), (int(bounding_box[0][0]), int(bounding_box[0][1])), (10, 50, 255), 2)
            upimg = image_path+"detected.jpg"
            cv2.imwrite(upimg, image)
            if (string == ""):
                string = "Could not read license plate. Try a better image."
            g.msgbox(string, image=upimg, ok_button="ok", title="40 e 40")
    else:
        sys.exit()