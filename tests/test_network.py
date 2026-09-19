import unittest
from unittest.mock import patch, MagicMock
from src.network.alert_dispatcher import AlertDispatcher

class TestAlertDispatcher(unittest.TestCase):

    @patch('requests.post')
    def test_send_alert_success(self, mock_post):
        # Configure mock to simulate a successful 200 OK response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        dispatcher = AlertDispatcher(endpoint="http://dummy-endpoint/api")
        result = dispatcher.send_alert("FIRE DETECTED", 0.95)

        self.assertTrue(result)
        mock_post.assert_called_once()
        
        # Verify JSON payload structure
        args, kwargs = mock_post.call_args
        import json
        payload = json.loads(kwargs['data'])
        self.assertEqual(payload['alert_type'], "FIRE DETECTED")
        self.assertEqual(payload['confidence'], 0.95)

if __name__ == '__main__':
    unittest.main()
