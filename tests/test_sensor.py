import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Sesame Street", 100)
        self.entry_sensor = EntrySensor(123, True, self.car_park)
        self.exit_sensor = ExitSensor(321, False, self.car_park)

    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 123)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)

    def test_exit_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.id, 321)
        self.assertEqual(self.exit_sensor.is_active, False)
        self.assertIsInstance(self.exit_sensor.car_park, CarPark)

    def test_detect_vehicle_adds_and_removes_plates(self):
        self.entry_sensor.detect_vehicle()
        self.exit_sensor.detect_vehicle()
