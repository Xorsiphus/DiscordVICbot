from moviepy.editor import *
from vid_to_images_convert import VideoConvertor
from image_to_unicode_convertor import ImageConvertor


class VideoParser:

    @staticmethod
    def parse_frames(file_name, frame_skip):

        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except OSError:
            print('Error: Creating directory of data')

        if len(os.listdir('./data')) == 0:
            VideoConvertor.convert_to_images(file_name, frame_skip)

        files = os.listdir('./data')

        try:
            if not os.path.exists('unicode'):
                os.makedirs('unicode')
        except OSError:
            print('Error: Creating directory of data')

        counter = 0
        for file_name in files:
            image = ImageConvertor.covert_to_unicode('./data/' + file_name)
            file_name = file_name.replace('.jpg', '')
            f = open('./unicode/' + file_name, 'wb')
            f.write(image.encode('UTF-8'))
            f.close()
            process = counter / len(files)
            if process * 20 % 100 == 0:
                print(str(counter) + ' / ' + str(len(files)))

    @staticmethod
    def parse_audio(file_name):
        video = VideoFileClip('./vids/' + file_name)
        audio = video.audio
        audio.write_audiofile('./audio/' + file_name.replace('.mp4', '.mp3'),
                              buffersize=100000)


def main():
    action = int(sys.argv[1])
    file_name = sys.argv[2]
    frame_skip = 3
    if len(sys.argv) > 3:
        frame_skip = 30 / int(sys.argv[3])

    if action == 1:
        VideoParser.parse_frames(file_name, frame_skip)
    if action == 2:
        VideoParser.parse_audio(file_name)
    if action == 3:
        VideoParser.parse_frames(file_name, frame_skip)
        VideoParser.parse_audio(file_name)


if __name__ == '__main__':
    main()
