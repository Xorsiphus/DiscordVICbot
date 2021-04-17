import socket
import subprocess
import sys
import time


def main(argv):

    channel_id = int(argv[1])
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
                         (i, channel_id, bots_count, delay))
        conn, addr = sockets[i - 1].accept()
        connects.append(conn)

    player_sock = socket.socket()
    player_sock.connect(('127.0.0.1', 9901))
    player_sock.send('1'.encode('UTF-8'))

    while connects[0].fileno() != -1:
        for i in range(bots_count):
            connects[i].send('1'.encode('UTF-8'))
            time.sleep(0.95 / video_fps)

    for i in range(bots_count):
        connects[i].close()


if __name__ == '__main__':
    main(sys.argv)
