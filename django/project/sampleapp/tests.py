from django.test import TestCase
import json
# Create your tests here.
class Test(TestCase):

    def test_x(self):
        self.fail('x')

class ApiTests(TestCase):
    def test_ner_endpoint_given_json_body_returns_200(self):
        response = self.client.post('/ner',{'sentence': 'Steve Malimu is in a good band.'})
        self.assertEqual(200, response.status_code)

    def test_ner_endpoint_given_json_body_with_known_entities_returns_entity_result_in_response(self):
        response = self.client.post('/ner',{'sentence': 'Kamala Harris'})
        self.assertEqual(200, response.status_code)
        data = json.loads(response.content)
        self.assertGreater(len(data['entities']), 0)
        self.assertEqual(data['entities'][0]['ent'], 'Kamala Harris')
        self.assertEqual(data['entities'][0]['label'], 'Person')
