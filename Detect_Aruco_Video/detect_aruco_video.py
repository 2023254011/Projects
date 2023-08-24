# import the necessary packages

import argparse
import imutils
import time
import cv2
import sys
from imutils.video import VideoStream
from realsensecv import RealsenseCapture
from imutils.video import FPS

'''
생성자는 알고리즘에 따라 다양합니다.

tracker = cv2.TrackerBoosting_create(): AdaBoost 알고리즘 기반
tracker = cv2.TrackerMIL_create(): MIL(Multiple Instance Learning) 알고리즘 기반
tracker = cv2.TrackerKCF_create(): KCF(Kernelized Correlation Filters) 알고리즘 기반
tracker = cv2.TrackerTLD_create(): TLD(Tracking, Learning and Detection) 알고리즘 기반
tracker = cv2.TrackerMedianFlow_create(): 객체의 전방향/역방향을 추적해서 불일치성을 측정
tracker = cv2.TrackerGOTURN_cretae(): CNN(Convolutional Neural Networks) 기반 - OpenCV 3.4 버전에서는 버그로 동작이 안 됨
tracker = cv2.TrackerCSRT_create(): CSRT(Channel and Spatial Reliability)
tracker = cv2.TrackerMOSSE_create(): 내부적으로 그레이 스케일 사용
'''
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

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--type", type=str,
	default="DICT_APRILTAG_16h5",
	help="type of ArUCo tag to detect")
args = vars(ap.parse_args())
# define names of each possible ArUco tag OpenCV supports
ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}

# verify that the supplied ArUCo tag exists and is supported by
# OpenCV
if ARUCO_DICT.get(args["type"], None) is None:
	print("[INFO] ArUCo tag of '{}' is not supported".format(
		args["type"]))
	sys.exit(0)
# load the ArUCo dictionary and grab the ArUCo parameters
print("[INFO] detecting '{}' tags...".format(args["type"]))
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])

arucoParams = cv2.aruco.DetectorParameters_create()
# initialize the video stream and allow the camera sensor to warm up

print("[INFO] starting video stream...")
#src="rtsp://192.168.1.9/screenlive" 
#src = "F:/AutoLanding/2016_0205_185422_003.MOV"
src = 0
trackers = cv2.MultiTracker_create()
#cap = RealsenseCapture()
# Property setting
#cap.WIDTH = 640
#cap.HEIGHT = 480
#cap.FPS = 30

# Unlike cv2.VideoCapture (), do not forget cap.start ()
#cap.start()
vs = VideoStream(src).start()
time.sleep(2.0)
keynum = 0
key = 0
roi = None
trackerIdx = 0  # 트랙커 생성자 함수 선택 인덱스
tracker = None
box = None
# initialize the FPS throughput estimator
fps = None
# loop over the frames from the video stream
fps = FPS().start()
t0 = time.time()
while True:

	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 1000 pixels
	timer = cv2.getTickCount()
	#ret, frames = cap.read()
	#frame = frames[0]

	frame = vs.read()
	#frame = imutils.resize(frame, width=1920, height=1080, inter=cv2.INTER_LINEAR)
	(success, boxes) = trackers.update(frame)

	# loop over the bounding boxes and draw them on the frame
	if success:
		for box in boxes:
			(x, y, w, h) = [int(v) for v in box]
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
			roi = frame[x: x + w,y: y + h]

		#roi = imutils.resize(roi, width=640, height=480, inter=cv2.INTER_LINEAR)
	# detect ArUco markers in the input frame
	(corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)

	# verify *at least* one ArUco marker was detected
	markerID = 0
	if len(corners) > 0:
		# flatten the ArUco IDs list
		ids = ids.flatten()
		# loop over the detected ArUCo corners
		for (markerCorner, markerID) in zip(corners, ids):
			# extract the marker corners (which are always returned
			# in top-left, top-right, bottom-right, and bottom-left
			# order)
			corners = markerCorner.reshape((4, 2))

			(topLeft, topRight, bottomRight, bottomLeft) = corners
			# convert each of the (x, y)-coordinate pairs to integers
			topRight = (int(topRight[0]), int(topRight[1]))
			bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
			bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
			topLeft = (int(topLeft[0]), int(topLeft[1]))
			# draw the bounding box of the ArUCo detection
			cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
			cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
			cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
			cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)
			# compute and draw the center (x, y)-coordinates of the
			# ArUco marker
			cX = int((topLeft[0] + bottomRight[0]) / 2.0)
			cY = int((topLeft[1] + bottomRight[1]) / 2.0)
			if keynum == int(markerID):
				cv2.circle(frame, (cX, cY), 4, (255, 0, 0), -1)
			else:
				cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)			
			# draw the ArUco marker ID on the frame
			cv2.putText(frame, str(markerID),
				(topLeft[0], topLeft[1] - 15),
				cv2.FONT_HERSHEY_SIMPLEX,
				0.5, (0, 255, 0), 2)
	# show the output frame
	if roi is not None:
		(H, W) = roi.shape[:2]
		if H > 0 and W > 0:
			cv2.imshow("roi", roi)
		else :
			cv2.destroyWindow("roi")

	fps.update()
	fps.stop()
	#fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
	cv2.putText(frame, str(int(fps.fps())), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
	#trackerName = tracker.__class__.__name__
	#cv2.putText(frame, str(trackerIdx) + ":"+trackerName , (100,20), \
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0),2,cv2.LINE_AA)

	cv2.imshow("Frame", frame)

	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

	#print(key,type(key), markerID,type(markerID))
	# if the `q` key was pressed, break from the loop
    # if the 's' key is selected, we are going to "select" a bounding
    # box to track
	if key == ord("s"):
		colors = []
		# select the bounding box of the object we want to track (make
		# sure you press ENTER or SPACE after selecting the ROI)
		box = cv2.selectROIs("Frame", frame, fromCenter=False,
								showCrosshair=True)

		#box=[262,116,71,49]
		#print(box,tuple)
		box = tuple(map(tuple, box)) 
		for bb in box:
			tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
			trackers.add(tracker, frame, bb)

	# if you want to reset bounding box, select the 'r' key 
	elif key == ord("r"):
		retval = cv2.Tracker.init(frame, box)#Tracker 초기화
		#frame: 입력 영상
		#box: 추적 대상 객체가 있는 좌표 (x, y)
		trackers.clear()
		trackers = cv2.MultiTracker_create()

		box = cv2.selectROIs("Frame", frame, fromCenter=False,
							showCrosshair=True)
		box = tuple(map(tuple, box))
		for bb in box:
			tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
			trackers.add(tracker, frame, bb)

	if key in range(48, 56):		
		trackerIdx = key-48     # 선택한 숫자로 트랙커 인덱스 수정

	if key == ord("q"):
		break
	elif key == ord("0"):
		keynum = 0
		trackerName = 'csrt'
	elif key == ord("1"):
		keynum = 1
		trackerName = 'kcf'
	elif key == ord("2"):
		keynum = 2
		trackerName = 'boosting'
	elif key == ord("3"):
		keynum = 3
		trackerName = 'mil'
	elif key == ord("4"):
		keynum = 4
		trackerName = 'tld'
	elif key == ord("5"):
		keynum = 5
		trackerName = 'medianflow'
	elif key == ord("6"):
		keynum = 6
		trackerName = 'mosse'
	elif key == ord("7"):
		keynum = 7
	elif key == ord("8"):
		keynum = 8
	elif key == ord("9"):
		keynum = 9
	else:
		continue

# do a bit of cleanup

#cap.stop()
vs.stop()
cv2.destroyAllWindows()