# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class IntentActionsTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.understand.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .intents(sid="UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .intent_actions().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/understand/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Intents/UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Actions',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "intent_sid": "UDdddddddddddddddddddddddddddddddd",
                "data": {},
                "url": "https://preview.twilio.com/understand/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Intents/UDdddddddddddddddddddddddddddddddd/Actions"
            }
            '''
        ))

        actual = self.client.preview.understand.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                               .intents(sid="UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                               .intent_actions().fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.understand.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .intents(sid="UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .intent_actions().update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/understand/Assistants/UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Intents/UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Actions',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "assistant_sid": "UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "intent_sid": "UDdddddddddddddddddddddddddddddddd",
                "data": {},
                "url": "https://preview.twilio.com/understand/Assistants/UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Intents/UDdddddddddddddddddddddddddddddddd/Actions"
            }
            '''
        ))

        actual = self.client.preview.understand.assistants(sid="UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                               .intents(sid="UDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                               .intent_actions().update()

        self.assertIsNotNone(actual)
