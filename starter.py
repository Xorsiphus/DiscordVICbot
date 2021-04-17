import socket
import subprocess
import time


def main():
    # parse_video('ba.mp4', 3)

    bots_count = 17
    video_fps = 10

    delay = (1 / video_fps) * bots_count

    sockets = []
    connects = []
    for i in range(bots_count):
        sockets.append(socket.socket())
        sockets[i].bind(('127.0.0.1', 9951 + i))
        sockets[i].listen(1)

    for i in range(1, bots_count + 1):
        subprocess.Popen("python sample_bot.py %d %d %d %d" %
                         (i, 536257258695426099, bots_count, delay))
        conn, addr = sockets[i - 1].accept()
        connects.append(conn)

    while connects[0].fileno() != -1:
        for i in range(bots_count):
            connects[i].send('1'.encode('UTF-8'))
            time.sleep(0.95 / video_fps)

    # for i in range(bots_count):
    #     connects[i].close()


if __name__ == '__main__':
    main()
