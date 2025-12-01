import unittest
from app import app  # Import your Flask app instance


class TestModelAppIntegration(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        
    def test_model_app_integration(self):
        # Valid test input that should work with the trained model
        form_data = {
            'temperature': '275.15',   # Kelvin
            'pressure': '1013',        # hPa
            'humidity': '85',          # %
            'wind_speed': '3.6',       # m/s
            'wind_deg': '180',         # degrees
            'rain_1h': '0',            # mm
            'rain_3h': '0',            # mm
            'snow': '0',               # mm
            'clouds': '20'             # %
        }

        response = self.client.post('/', data=form_data)

        # The route should not crash
        self.assertEqual(response.status_code, 200)

        html_text = response.data.decode('utf-8').lower()

        # Ensure the result page contains a weather prediction (look for the wording your template uses)
        self.assertIn("prediction", html_text)

        # Ensure the result includes a prediction time (common template phrase)
        self.assertIn("time", html_text)

        # Valid weather classes
        valid_classes = [
            'clear', 'cloudy', 'drizzly', 'foggy', 'hazey',
            'misty', 'rainy', 'smokey', 'thunderstorm'
        ]
        found = any(weather in html_text for weather in valid_classes)

        # Ensure classification is in valid classes
        self.assertTrue(found, "Weather class returned was not in the valid classes list.")


if __name__ == '__main__':
    unittest.main()
