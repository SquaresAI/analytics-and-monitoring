import unittest
from analytics.visualization.dashboard_generator import DashboardGenerator

class TestDashboardGeneration(unittest.TestCase):
    def setUp(self):
        self.dashboard_gen = DashboardGenerator()

    def test_generate_dashboard(self):
        """Test dashboard generation with valid data."""
        data = {"CPU Usage": [10, 20, 30], "Memory Usage": [50, 60, 70]}
        dashboard = self.dashboard_gen.generate(data)
        self.assertIn("CPU Usage", dashboard)
        self.assertIn("Memory Usage", dashboard)

    def test_invalid_data(self):
        """Test handling of invalid data."""
        with self.assertRaises(ValueError):
            self.dashboard_gen.generate(None)

if __name__ == "__main__":
    unittest.main()
