import subprocess
import time
import os

from ImageToUnicodeConvert import ImageConvertor
from VidToImagesConvert import VideoConvertor


def main():
    # parse_video('ba.mp4', 3)

    bots_count = 17
    video_fps = 3

    delay = (1 / video_fps) * bots_count

    for i in range(1, bots_count + 1):
        subprocess.Popen("python sample_bot.py %d %d %d %d" %
                         (i, 536257258695426099, bots_count, delay),
                         shell=True)
        time.sleep(1 / video_fps * 0.95)


def parse_video(file_name, frame_skip):
    VideoConvertor.convert_to_images(file_name, frame_skip)

    files = os.listdir('./data')

    for file_name in files:
        image = ImageConvertor.covert_to_unicode('./data/' + file_name)
        file_name = file_name.replace('.jpg', '')
        f = open('./unicode/' + file_name, 'wb')
        f.write(image.encode('UTF-8'))
        f.close()
        print(file_name + ' is done')


if __name__ == '__main__':
    main()
