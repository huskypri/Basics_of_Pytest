import pytest
from unittest.mock import Mock, call
from Problem5 import Camera

def test_camera_connect_called_before_capture():
    camera = Camera()

    # Replace hardware methods with mocks
    camera.connect = Mock()
    camera.capture = Mock()

    manager = Mock()
    manager.attach_mock(camera.connect, "connect")
    manager.attach_mock(camera.capture, "capture")

    camera.connect()
    camera.capture()

    manager.assert_has_calls([call.connect(), call.capture()])


