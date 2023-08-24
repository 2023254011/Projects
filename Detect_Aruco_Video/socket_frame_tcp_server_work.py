import socket, threading
import cv2
import pickle
import struct 
import time
import sys
from imutils.video import VideoStream
from imutils.video import FPS
from struct import pack, unpack, calcsize
col = -1
row = -1
mouse_rectangle = False

def onMouse(event, x, y, flags, parm):
    global client_socket, mouse_rectangle, col, row, frame

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_rectangle = True
        col, row = x, y
        print("EVENT_LBUTTONDOWN")
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_rectangle:
            frame_draw = frame.copy()
            cv2.rectangle(frame_draw, pt1=(col,row), pt2=(x, y),color=(0,255,255),thickness=2)
            cv2.imshow('TCP_Frame_Socket',frame_draw)
        print("EVENT_MOUSEMOVE")
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_rectangle = False
        w = x - col
        h = y - row
        if w > 0 and h > 0 :
            frame_draw = frame.copy()
            cv2.rectangle(frame_draw, pt1=(col,row), pt2=(x, y),color=(0,255,255),thickness=2)
            cv2.imshow('TCP_Frame_Socket',frame_draw)

        sendData = pack('BIIII', 1,col, row, x, y)
        print(col, row, x, y)
        client_socket.sendall(sendData)  # 클라이언트에게 응답

ip = '192.168.0.203' # ip 주소
port = 50001 # port 번호

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 소켓 객체를 생성
server_socket.bind((ip, port)) # 바인드(bind) : 소켓에 주소, 프로토콜, 포트를 할당
server_socket.listen(10) # 연결 수신 대기 상태(리스닝 수(동시 접속) 설정)
print('클라이언트 연결 대기')

# 연결 수락(클라이언트 소켓 주소를 반환)
client_socket, addr = server_socket.accept()
print(addr) # 클라이언트 주소 출력

data = b"" # 수신한 데이터를 넣을 변수
payload_size = struct.calcsize(">L")

# 마우스 입력, namedWIndow or imshow가 실행되어 창이 떠있는 상태에서만 사용가능
# 마우스 이벤트가 발생하면 on_mouse 함수 실행
cv2.namedWindow('TCP_Frame_Socket')   # should create window object first
cv2.setMouseCallback('TCP_Frame_Socket', onMouse)

try:
    # 서버는 여러 클라이언트를 상대하기 때문에 무한 루프를 사용한다.
    while True:
        # client로 접속이 발생하면 accept가 발생한다.
        # 그럼 client 소켓과 addr(주소)를 튜플로 받는다.
        #client_socket, addr = server_socket.accept()

        # 프레임 수신
        while len(data) < payload_size:
            data += client_socket.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        while len(data) < msg_size:
            data += client_socket.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        #print("Frame Size : {}".format(msg_size)) # 프레임 크기 출력

        # 역직렬화(de-serialization) : 직렬화된 파일이나 바이트를 원래의 객체로 복원하는 것
        frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes") # 직렬화되어 있는 binary file로 부터 객체로 역직렬화
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR) # 프레임 디코딩
        # 영상 출력
        cv2.imshow('TCP_Frame_Socket',frame)
        key = cv2.waitKey(1) & 0xFF
        # 1초 마다 키 입력 상태를 받음
        if key == ord('q') : # q를 입력하q면 종료
            break
        elif key == ord('r'):
            sendData = pack('BIIII', 0, 0, 0, 0, 0)
            client_socket.sendall(sendData)  # 클라이언트에게 응답
except:
    print("server")
finally:
    # 에러가 발생하면 서버 소켓을 닫는다.
    cv2.destroyAllWindows()
    server_socket.close()
    client_socket.close()