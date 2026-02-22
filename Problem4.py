"""Sensor data quality check"""

def filter_temperature_readings(readings):
    no_invalid_values = 0
    for reading in readings:
        if reading is None:
            no_invalid_values = no_invalid_values + 1
        elif reading < -40:
            no_invalid_values = no_invalid_values + 1
        elif reading > 125: 
            no_invalid_values = no_invalid_values + 1

    if  no_invalid_values == 0:
        return True
    else:
        return False          
        

def temperature_readings_order_preserved(readings):
    list = []
    for reading in readings:
        if reading is None:
            continue
        elif reading < -40:
            continue
        elif reading > 125: 
            continue
        else: 
            list.append(reading)

    return list

def temperature_readings_empty_input_output(readings):
    if len(readings) == 0:
        return True
    else:
        return False

