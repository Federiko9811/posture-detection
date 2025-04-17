"""
Camera utility for handling video capture and frame processing.
"""
import cv2


class CameraManager:
    """Manages camera operations and frame processing"""

    def __init__(self, camera_index=0, frame_width=640, frame_height=480):
        """
        Initialize the camera manager

        Args:
            camera_index: Index of the camera to use (default: 0)
            frame_width: Width of the camera frame (default: 640)
            frame_height: Height of the camera frame (default: 480)
        """
        self.camera_index = camera_index
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.cap = None

    def initialize(self):
        """Initialize the camera capture"""
        self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():
            raise RuntimeError("Could not open webcam")

        # Set frame dimensions
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

        # Get actual dimensions (may differ from requested if camera doesn't support them)
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        return self.frame_width, self.frame_height

    def read_frame(self):
        """
        Read a frame from the camera

        Returns:
            Tuple of (success, frame)
        """
        if self.cap is None:
            raise RuntimeError("Camera not initialized")

        return self.cap.read()

    def release(self):
        """Release the camera resources"""
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def is_open(self):
        """Check if camera is open"""
        return self.cap is not None and self.cap.isOpened()

    def resize_frame(self, new_width, new_height):
        """
        Resize the camera frame

        Args:
            new_width: New width for the frame
            new_height: New height for the frame
        """
        if self.cap is not None:
            self.frame_width = new_width
            self.frame_height = new_height
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

            # Get actual dimensions
            self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        return self.frame_width, self.frame_height
