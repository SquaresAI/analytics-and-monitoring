import unittest
from analytics.data_collection.collector import DataCollector

class TestDataCollection(unittest.TestCase):
    def setUp(self):
        self.data_collector = DataCollector()

    def test_collect_valid_data(self):
        """Test data collection with a valid data source."""
        source = "system_metrics"
        collected_data = self.data_collector.collect(source)
        self.assertIsInstance(collected_data, dict)

    def test_collect_invalid_data_source(self):
        """Test handling of invalid data sources."""
        source = "invalid_source"
        with self.assertRaises(Exception):
            self.data_collector.collect(source)

if __name__ == "__main__":
    unittest.main()
