import cv2
import numpy as np
import pixellib
from pixellib.semantic import semantic_segmentation


def resize(img):
    img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)
    return img    

def img_to_mask(img):
    prev_shape = img.shape
    mask = np.reshape(img, (-1,1))

    for i in range(len(mask)):
        if mask[i] != 0:
            mask[i] = [255]
    mask = np.reshape(mask, prev_shape)
    return mask

def apply_mask(img, mask):
    return cv2.bitwise_and(img, img, mask = mask)


def forImage():

    img = cv2.imread('2.jpg')
    img = resize(img)

    mask = cv2.imread('2_output.jpg', 0)
    mask = resize(mask)

    mask = img_to_mask(mask)

    maskedImg = apply_mask(img, mask)

    cv2.imshow('Image',img)
    cv2.imshow("Mask", mask)
    cv2.imshow("MaskedImg", maskedImg)


    cv2.waitKey(0)


def forVideo():
    
    cap = cv2.VideoCapture(0)

    while 1:
        ret, frame = cap.read()
        frame = resize(frame)
        mask = cv2.imread('2_output.jpg', 0)
        mask = resize(mask)

        mask = img_to_mask(mask)

        maskedImg = apply_mask(frame, mask)

        cv2.imshow('Video', maskedImg)
        
        if ord('q') == cv2.waitKey(1) & 0xFF:
            break

    cap.release()
    cv2.destroyAllWindows()

def maskedBgVideo():
    cap = cv2.VideoCapture(0)
    bgVideo = cv2.VideoCapture("resources/nature.mp4")

    segment_image = semantic_segmentation()
    segment_image.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
    # output, segmap = segment_image.segmentAsPascalvoc(INPUT_IMG_PATH)
    while 1:
        ret, frame = cap.read()
        success, bg = bgVideo.read()

        frame = resize(frame)
        bg = resize(bg)
        segmap, mask = segment_image.segmentAsPascalvoc(frame)
        # print(type(mask))
        # cv2.imshow('MASK', mask)    
        mask = resize(mask)
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

        mask = img_to_mask(mask)

        mask_inv = cv2.bitwise_not(mask)

        maskedImg = apply_mask(frame, mask)
        bgMask = cv2.bitwise_and(bg, bg, mask = mask_inv)
        finalImg = cv2.add(bgMask, maskedImg)


        cv2.imshow('maskedImg', maskedImg)
        cv2.imshow('finalImg', finalImg)


        if ord('q') == cv2.waitKey(1) & 0xFF:
            break
    cap.release()
    cv2.destroyAllWindows()


def main():
    maskedBgVideo()


#Driver's Code
if __name__ == '__main__':
    main()