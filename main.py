import os
import sys
import time
import cv2
import numpy as np

ASCII_CHARS = np.array(list("@%#*+=-:. "))
NUM_CHARS = len(ASCII_CHARS) - 1

def terminalSize():
    sz = os.get_terminal_size()
    return sz.columns, sz.lines

def toAscii(frame, width, height):
    resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
    if len(resized.shape) == 3:
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    else:
        gray = resized
    asciiMat = ASCII_CHARS[(gray.astype(np.float32) / 255.0 * NUM_CHARS).astype(int)]
    lines = ["".join(row) for row in asciiMat]
    return "\n".join(lines)

def main():
    source = sys.argv[1] if len(sys.argv) > 1 else 0
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        print(f"Error: Could not open source {source}")
        sys.exit(1)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    frameDelay = 1.0 / (cap.get(cv2.CAP_PROP_FPS) or 60.0)
    sys.stdout.write("\033[2J\033[?25l")
    sys.stdout.flush()
    try:
        while cap.isOpened():
            stTime = time.time()
            ret, frame = cap.read()
            if not ret:
                break
            cols, lines = terminalSize()
            asciiFrame = toAscii(frame, cols, lines - 1)
            sys.stdout.write("\033[H" + asciiFrame)
            sys.stdout.flush()
            elapsed = time.time() - stTime
            slTime = frameDelay - elapsed
            if slTime > 0:
                time.sleep(slTime)
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        sys.stdout.write("\033[?25h\033[2J\033[H")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
