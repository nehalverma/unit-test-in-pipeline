import json
import datetime
import unittest

# Lambda function definition
def lambda_handler(event, context):
    print(event)
    data = {
        'output': 'Hello from ' + event['Country'],
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {'Content-Type': 'application/json'}
    }

# Unit tests for the Lambda function
class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("Testing response.")
        
        event = {'Country': 'USA'}
        result = lambda_handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello from ' + event['Country'], json.loads(result['body'])['output'])

        event = {'Country': 'INDIA'}
        result = lambda_handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello from ' + event['Country'], json.loads(result['body'])['output'])

if __name__ == '__main__':
    unittest.main()
