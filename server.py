import socket
import subprocess
import sys
import time


def main(argv):

    channel_id = int(argv[1])
    bots_count = int(argv[2])
    video_fps = int(argv[3])

    # delay = (1 / video_fps) * bots_count

    sockets = []
    connects = []
    # sockets = ServerSocket()

    for i in range(bots_count):
        # sockets.set_up(i)
        sockets.append(socket.socket())
        sockets[i].bind(('127.0.0.1', 9951 + i))
        sockets[i].listen(1)

    for i in range(1, bots_count + 1):
        subprocess.Popen("python sample_bot.py %d %d %d" %
                         (i, channel_id, bots_count))
        # sockets.accept(i)
        conn, addr = sockets[i - 1].accept()
        connects.append(conn)

    player_sock = socket.socket()
    player_sock.connect(('127.0.0.1', 9901))
    player_sock.send('1'.encode('UTF-8'))

    time.sleep(1.5)
    pointer = time.time()

    while True:
        for i in range(bots_count):
            if connects[i].fileno() != -1:
                connects[i].send('1'.encode('UTF-8'))
                # sockets.send(i, '1')
                time.sleep(1 / (video_fps * 1.1))
                if i % 50 == 0:
                    time.sleep(time.time() - pointer - i / video_fps)

    # for i in range(bots_count):
    #     connects[i].close()


if __name__ == '__main__':
    main(sys.argv)
