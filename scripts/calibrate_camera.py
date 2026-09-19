import cv2
import numpy as np
import os

def calibrate_fisheye():
    """
    Generates calibration matrices to dewarp the 360 camera feed.
    Requires taking multiple pictures of a printed checkerboard.
    """
    CHECKERBOARD = (6, 9)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1)
    
    objp = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
    objp[0,:,:2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

    objpoints = []
    imgpoints = []
    
    # Load calibration images
    images = [f for f in os.listdir('../data/calibration') if f.endswith('.jpg')]
    
    for fname in images:
        img = cv2.imread(os.path.join('../data/calibration', fname))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH)
        if ret:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (3, 3), (-1, -1), criteria)
            imgpoints.append(corners2)
            
    print("Calibration maps generated. Save these to use in src/vision/dewarp.py")

if __name__ == "__main__":
    calibrate_fisheye()
