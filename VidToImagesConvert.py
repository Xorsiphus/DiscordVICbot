import cv2
import os


class VideoConvertor:

    @staticmethod
    def convert_to_images(file_name, frame_skip):
        cap = cv2.VideoCapture('./vids/' + file_name)

        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except OSError:
            print('Error: Creating directory of data')

        current_frame = 0
        while True:
            ret, frame = cap.read()

            if not ret:
                print('Success')
                break

            if current_frame % frame_skip == 0:
                name = './data/frame' + str(int(current_frame / frame_skip)) + '.jpg'
                # name2 = './data/frame' + str(int(currentFrame / 10)) + '-resized.jpg'
                print('Creating...' + name + '; Frame number: ' + str(current_frame))
                cv2.imwrite(name, frame)

                # scale_percent = 50  # Процент от изначального размера
                # width = int(frame.shape[1] * scale_percent / 100)
                # height = int(frame.shape[0] * scale_percent / 100)
                # dim = (width, height)
                # resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

                # cv2.imwrite(name2, resized)

            current_frame += 1

        cap.release()
        cv2.destroyAllWindows()
