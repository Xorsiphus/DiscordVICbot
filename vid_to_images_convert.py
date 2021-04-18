import cv2
import os


class VideoConvertor:

    @staticmethod
    def convert_to_images(file_name, frame_skip):
        cap = cv2.VideoCapture('./vids/' + file_name)

        current_frame = 0
        offset = 0

        while True:
            ret, frame = cap.read()

            if not ret:
                print('Success')
                break

            if current_frame == round(offset):
                name = './data/frame' + str(int(current_frame / frame_skip)) + '.jpg'
                print('Creating...' + name)
                cv2.imwrite(name, frame)
                offset += frame_skip

            current_frame += 1

        cap.release()
        cv2.destroyAllWindows()
