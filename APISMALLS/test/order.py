# content of test_expectation.py
import pytest
import json


def test_addOrder(self):
        with self.app() as order, self.app_context():
            data = {"order": {"items": [{"name" : "Eggs", "quantity" : 34.00},{"name" : "Eggs", "quantity" : 34.00}]}}

            response = order.post(
                "/order",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
            self.assertEqual(200, response.status_code)
            self.assertEqual('Data checked, the date is', response.data.response)