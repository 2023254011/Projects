import socket
import struct
import threading
import time
from _thread import *
import numpy as np
import cv2

mouse_rectangle = False


def receive_all(sock, count):
    buf = bytearray(b'')

    while count:
        newbuff = sock.recv(count)
        if not newbuff: return None
        buf += newbuff
        count -= len(newbuff)
    return buf


def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result


def int_to_bytes(value, length):
    result = []

    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)

    result.reverse()

    return result


def onMouse(event, x, y, flags, parm):
    global mouse_rectangle, g_copy_img, g_decode_img
    col = 0
    row = 0
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_rectangle = True
        col, row = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_rectangle:
            cv2.rectangle(g_decode_img, (col, row), (x, y), (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_rectangle = False


def run_server_cv():
    global mouse_rectangle, g_copy_img, g_decode_img

    HOST = ''
    PORT = 20001

    cv2.namedWindow('Client')   # should create window object first
    cv2.setMouseCallback('Client', onMouse, 0)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    server_socket.bind((HOST, PORT))
    print('Socket bind complete')
    server_socket.listen(10)
    print('Socket now listening')

    client_socket, addr = server_socket.accept()
    # print("wait accept to : ", addr[0], ":", str(addr[1]))
    print("Accept to : ", addr)
    print('wait image')

    while True:

        try:
            if mouse_rectangle is True:
                bytes_buf_null = receive_all(client_socket, 4)

                if bytes_buf_null is not None:
                    bytes_length_null = bytes_to_int(bytes_buf_null)
                    print("Clr Length = {} ".format(bytes_length_null))
                    byte_data_null = receive_all(client_socket, int(bytes_length_null))
            else:
                bytes_buf = receive_all(client_socket, 4)

                if bytes_buf is not None:
                    bytes_length = bytes_to_int(bytes_buf)
                    print("Rx Length = {} ".format(bytes_length))
                    byte_data = receive_all(client_socket, int(bytes_length))

                    # convert jpg image to matix
                    g_decode_img = np.frombuffer(byte_data, dtype=np.uint8)
                    g_decode_img = cv2.imdecode(g_decode_img, cv2.COLOR_RGB2BGR)

            g_copy_img = np.copy(g_decode_img)

            cv2.imshow('Client', g_copy_img)
            cv2.waitKey(1)

            # convert Mat to byte for sending to client
            ret, imgencoded = cv2.imencode('.jpg', g_copy_img)
            byte_img = np.array(imgencoded)

            int_len_byte_img = len(byte_img)
            bytes_len_img = int_len_byte_img.to_bytes(4, byteorder='big')

            client_socket.send(bytes_len_img)
            client_socket.send(byte_img)

        except IOError:
            client_socket.close()

            print("wait accept")
            client_socket, addr = server_socket.accept()
            print("accept to : ", addr[0], ":", str(addr[1]))
            print('wait image')

    server_socket.close()


if __name__ == "__main__":
    run_server_cv()