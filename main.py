#!/usr/bin/env python3
"""
Main entry point for the Posture Detector application.
"""
import argparse
import sys

from config.settings import DEFAULT_CAMERA_WIDTH, DEFAULT_CAMERA_HEIGHT
from detector.posture_detector import PostureDetector
from utils.camera import CameraManager


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Posture Detection System')
    parser.add_argument('--width', type=int, default=DEFAULT_CAMERA_WIDTH,
                        help=f'Camera frame width (default: {DEFAULT_CAMERA_WIDTH})')
    parser.add_argument('--height', type=int, default=DEFAULT_CAMERA_HEIGHT,
                        help=f'Camera frame height (default: {DEFAULT_CAMERA_HEIGHT})')
    parser.add_argument('--camera', type=int, default=0, help='Camera index (default: 0)')
    parser.add_argument('--no-guidance', action='store_true', help='Disable posture correction guidance')

    return parser.parse_args()


def main():
    """Main function to run the posture detector"""
    args = parse_arguments()

    try:
        # Initialize camera with specified dimensions
        camera_manager = CameraManager(camera_index=args.camera, frame_width=args.width, frame_height=args.height)

        # Initialize posture detector
        detector = PostureDetector(camera_manager=camera_manager, show_guidance=not args.no_guidance)

        # Run the detector
        detector.run()

    except KeyboardInterrupt:
        print("\nApplication terminated by user")
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
