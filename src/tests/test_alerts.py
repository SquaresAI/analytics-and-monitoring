import unittest
from analytics.alerts import AlertSystem

class TestAlertSystem(unittest.TestCase):
    def setUp(self):
        self.alert_system = AlertSystem()

    def test_threshold_alert(self):
        """Test if the system triggers alerts when a threshold is breached."""
        self.alert_system.set_threshold("CPU", 90)
        alert_triggered = self.alert_system.check_threshold("CPU", 95)
        self.assertTrue(alert_triggered)

    def test_no_alert(self):
        """Test if no alert is triggered when usage is within limits."""
        self.alert_system.set_threshold("Memory", 80)
        alert_triggered = self.alert_system.check_threshold("Memory", 70)
        self.assertFalse(alert_triggered)

if __name__ == "__main__":
    unittest.main()
