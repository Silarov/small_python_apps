import cv2

def show_webcam(mirror=False):
    scale = 100

    cam = cv2.VideoCapture(0)
    while True:
        ret_val, image = cam.read()
        if mirror: 
            image = cv2.flip(image, 1)

        # Get the webcam size
        height, width, channels = image.shape

        # Prepare the crop
        centerX, centerY = int(height / 2), int(width / 2)
        radiusX, radiusY = int(scale * height / 100), int(scale * width / 100)

        minX, maxX = max(centerX - radiusX, 0), min(centerX + radiusX, height)
        minY, maxY = max(centerY - radiusY, 0), min(centerY + radiusY, width)

        cropped = image[minX:maxX, minY:maxY]
        resized_cropped = cv2.resize(cropped, (width, height))

        cv2.imshow('my webcam', resized_cropped)

        key = cv2.waitKey(1)
        
        # Press 'esc' to quit
        if key == 27: 
            break

    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()
