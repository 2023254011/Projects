import socket
import cv2
import pickle
import struct 
import time
import sys
from imutils.video import VideoStream
from imutils.video import FPS
col = -1
row = -1

mouse_rectangle = False
def onMouse(event, x, y, flags, parm):
    global mouse_rectangle, col, row, frame

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_rectangle = True
        col, row = x, y
        print("EVENT_LBUTTONDOWN")
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_rectangle:
            cv2.rectangle(frame, pt1=(col,row), pt2=(x, y),color=(0,255,255),thickness=2)
            cv2.imshow('TCP_Frame_Socket',frame)
        print("EVENT_MOUSEMOVE")
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_rectangle = False
        cv2.rectangle(frame, pt1=(col,row), pt2=(x, y),color=(0,255,255),thickness=2)
        cv2.imshow('TCP_Frame_Socket',frame)
        client_socket.sendall("welcome!".encode())  # 클라이언트에게 응답
        print("EVENT_LBUTTONUP")

trackerName= 'csrt'
OPENCV_OBJECT_TRACKERS = {
    "csrt": cv2.TrackerCSRT_create,
    "kcf": cv2.TrackerKCF_create,
    "boosting": cv2.TrackerBoosting_create,
    "mil": cv2.TrackerMIL_create,
    "tld": cv2.TrackerTLD_create,
    "medianflow": cv2.TrackerMedianFlow_create,
    "mosse": cv2.TrackerMOSSE_create
}
#cap.set(3,320)
# floate 형태로 rc값을 받으므로 int로 변환해서 list로 감싸고 tuple로 변환
def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
trackers = cv2.MultiTracker_create()

ip = '192.168.1.9' # ip 주소
port = 50001 # port 번호

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 소켓 객체를 생성
client_socket.bind((ip, port)) # 바인드(bind) : 소켓에 주소, 프로토콜, 포트를 할당
client_socket.listen(10) # 연결 수신 대기 상태(리스닝 수(동시 접속) 설정)
print('클라이언트 연결 대기')

# 연결 수락(클라이언트 소켓 주소를 반환)
conn, addr = client_socket.accept()
print(addr) # 클라이언트 주소 출력

data = b"" # 수신한 데이터를 넣을 변수
payload_size = struct.calcsize(">L")

cv2.namedWindow('TCP_Frame_Socket')   # should create window object first
cv2.setMouseCallback('TCP_Frame_Socket', onMouse)

while True:
    # 프레임 수신
    while len(data) < payload_size:
        data += conn.recv(4096)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    #print("Frame Size : {}".format(msg_size)) # 프레임 크기 출력

    # 역직렬화(de-serialization) : 직렬화된 파일이나 바이트를 원래의 객체로 복원하는 것
    frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes") # 직렬화되어 있는 binary file로 부터 객체로 역직렬화
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR) # 프레임 디코딩
    #frame = imutils.resize(frame, width=1920, height=1080, inter=cv2.INTER_LINEAR)
    (success, boxes) = trackers.update(frame)
    # loop over the bounding boxes and draw them on the frame
    if success:
        for box in boxes:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi = frame[x: x + w,y: y + h]

    # 영상 출력
    cv2.imshow('TCP_Frame_Socket',frame)
    # 마우스 입력, namedWIndow or imshow가 실행되어 창이 떠있는 상태에서만 사용가능
    # 마우스 이벤트가 발생하면 on_mouse 함수 실행

    key = cv2.waitKey(1) & 0xFF
    # 1초 마다 키 입력 상태를 받음
    if key == ord('q') : # q를 입력하q면 종료
        break

    if key == ord("s"):
        colors = []
        box = cv2.selectROIs("TCP_Frame_Socket", frame, fromCenter=False,
                                showCrosshair=True)

        #box=[262,116,71,49]
        #print(box,tuple)
        box = tuple(map(tuple, box)) 
        for bb in box:
            tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
            trackers.add(tracker, frame, bb)

    # if you want to reset bounding box, select the 'r' key 
    elif key == ord("r"):
        trackers.clear()
        trackers = cv2.MultiTracker_create()
        box = cv2.selectROIs("TCP_Frame_Socket", frame, fromCenter=False,
                            showCrosshair=True)
        box = tuple(map(tuple, box))
        for bb in box:
            tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
            trackers.add(tracker, frame, bb)

cv2.destroyAllWindows()
client_socket.close()