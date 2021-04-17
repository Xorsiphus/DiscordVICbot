from PIL import Image
import numpy as np

g_scale = ('\u2B1B', '\U0001F5A4', '\U0001F90D', '\u2B1C')


class ImageConvertor:

    @staticmethod
    def covert_to_unicode(file_name):

        global g_scale

        image = Image.open(file_name).convert('L')

        g_width, g_high = image.size[0], image.size[1]

        cols = 51
        h = w = g_width / cols
        rows = int(g_high / h)

        if cols > g_width or rows > g_high:
            print("Image too small for specified cols!")
            exit(0)

        aimg = []

        for j in range(rows):
            y1 = int(j * h)
            y2 = int((j + 1) * h)

            if j == rows - 1:
                y2 = g_high

            aimg.append("")

            for i in range(cols):

                x1 = int(i * w)
                x2 = int((i + 1) * w)

                if i == cols - 1:
                    x2 = g_width

                img = image.crop((x1, y1, x2, y2))
                avg = int(ImageConvertor._get_average_l(img))
                gsval = g_scale[int((avg * 3) / 255)]
                aimg[j] += gsval

        return ImageConvertor.convert_to_string(aimg)

    @staticmethod
    def _get_average_l(cur_image):
        im = np.array(cur_image)
        width, high = im.shape
        return np.average(im.reshape(width * high))

    @staticmethod
    def convert_to_string(image_list):
        result = ''
        for row in image_list:
            # result += row + '\r'
            result += row + '\n'
        return result
