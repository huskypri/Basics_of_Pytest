from Problem8 import Motor

def test_motor_starts_correctly():
    motor = Motor()
    assert motor.running is False
    motor.start()
    assert motor.running is True


def test_motor_stops_correctly():
    motor = Motor()
    motor.start()
    assert motor.running is True
    motor.stop()
    assert motor.running is False


def test_motor_transitions_correctly():
    motor = Motor()
    assert motor.running is False 
    motor.start()
    assert motor.running is True 
    motor.stop()
    assert motor.running is False

def test_motor_transitions_correctly_edge_case():
    motor = Motor()
    assert motor.running is False 
    motor.start()
    motor.start()
    assert motor.running is True 
    motor.stop()
    motor.stop()
    assert motor.running is False
