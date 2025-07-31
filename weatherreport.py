

def sensorStub(data = None):
    if data is None:
        data = {
            'temperatureInC': 50,
            'precipitation': 70,
            'humidity': 26,
            'windSpeedKMPH': 52
        }
    return data


def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather


def testRainy():
    weather = report(lambda: sensorStub({
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }))    
    print(weather)
    assert "Alert" in weather, "Bug not exposed: should alert stormy weather"


def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)

    weather = report(lambda: sensorStub({
        'temperatureInC': 50,
        'precipitation': 50,
        'humidity': 26,
        'windSpeedKMPH': 30
    }))
    
    print(weather)
    assert "Cloudy" in weather, "Bug not exposed: Should be partly cloudy"
    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)
    assert(len(weather) > 0);


if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)");
