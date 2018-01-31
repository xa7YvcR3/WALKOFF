import json
import unittest

import walkoff.case.database as case_database
from walkoff.case.subscription import *
from walkoff.tests.util.assertwrappers import orderless_list_compare


class TestCaseDatabase(unittest.TestCase):
    def setUp(self):
        case_database.initialize()

    def tearDown(self):
        case_database.case_db.session.query(case_database.Event).delete()
        case_database.case_db.session.query(case_database.Case).delete()
        case_database.case_db.session.commit()

    @staticmethod
    def __construct_basic_db():
        cases = {'case1': {'uid1': ['e1', 'e2', 'e3'],
                           'uid2': ['e1']},
                 'case2': {'uid1': ['e2', 'e3']},
                 'case3': {'uid3': ['e', 'b', 'c'],
                           'uid4': ['d']},
                 'case4': {'uid1': ['a', 'b']}}
        set_subscriptions(cases)
        return cases

    def test_register_cases(self):
        cases = TestCaseDatabase.__construct_basic_db()
        cases_in_db = [case.name for case in case_database.case_db.session.query(case_database.Case).all()]
        self.assertSetEqual(set(cases.keys()), set(cases_in_db), 'Not all cases were added to subscribed cases')
        self.assertEqual(len(set(cases_in_db)), len(cases_in_db), 'Duplicate case was added to database')

    def test_add_duplicate_case_not_allowed(self):
        TestCaseDatabase.__construct_basic_db()
        case_database.case_db.add_cases(['case1', 'case2'])
        cases_in_db = [case.name for case in case_database.case_db.session.query(case_database.Case).all()]
        orderless_list_compare(self, cases_in_db, ['case1', 'case2', 'case3', 'case4'])

    def test_add_cases_with_empty_list(self):
        TestCaseDatabase.__construct_basic_db()
        case_database.case_db.add_cases([])
        cases_in_db = [case.name for case in case_database.case_db.session.query(case_database.Case).all()]
        orderless_list_compare(self, cases_in_db, ['case1', 'case2', 'case3', 'case4'])

    def test_delete_cases(self):
        TestCaseDatabase.__construct_basic_db()
        case_database.case_db.delete_cases(['case1', 'case2'])
        cases_in_db = [case.name for case in case_database.case_db.session.query(case_database.Case).all()]
        expected_cases = ['case3', 'case4']
        self.assertSetEqual(set(expected_cases), set(cases_in_db))
        self.assertEqual(len(set(cases_in_db)), len(expected_cases))

    def test_rename_case(self):
        TestCaseDatabase.__construct_basic_db()
        case_database.case_db.rename_case('case1', 'renamed')
        cases_in_db = [case.name for case in case_database.case_db.session.query(case_database.Case).all()]
        expected_cases = ['renamed', 'case2', 'case3', 'case4']
        self.assertSetEqual(set(expected_cases), set(cases_in_db))
        self.assertEqual(len(set(cases_in_db)), len(expected_cases))

    def test_rename_case_empty_name(self):
        TestCaseDatabase.__construct_basic_db()
        case_database.case_db.rename_case('case1', '')
        cases_in_db = [case.name for case in case_database.case_db.session.query(case_database.Case).all()]
        expected_cases = ['case1', 'case2', 'case3', 'case4']
        self.assertSetEqual(set(expected_cases), set(cases_in_db))
        self.assertEqual(len(set(cases_in_db)), len(expected_cases))

    def test_rename_case_invalid_case(self):
        TestCaseDatabase.__construct_basic_db()
        case_database.case_db.rename_case('case5', 'renamed')
        cases_in_db = [case.name for case in case_database.case_db.session.query(case_database.Case).all()]
        expected_cases = ['case1', 'case2', 'case3', 'case4']
        self.assertSetEqual(set(expected_cases), set(cases_in_db))
        self.assertEqual(len(set(cases_in_db)), len(expected_cases))

    def test_add_event(self):
        TestCaseDatabase.__construct_basic_db()
        event1 = case_database.Event(type='SYSTEM', message='message1')
        case_database.case_db.add_event(event=event1, cases=['case1', 'case3'])
        event2 = case_database.Event(type='WORKFLOW', message='message2')
        case_database.case_db.add_event(event=event2, cases=['case2', 'case4'])
        event3 = case_database.Event(type='ACTION', message='message3')
        case_database.case_db.add_event(event=event3, cases=['case2', 'case3', 'case4'])
        event4 = case_database.Event(type='BRANCH', message='message4')
        case_database.case_db.add_event(event=event4, cases=['case1'])

        expected_event_messages = {'case1': [('SYSTEM', 'message1'), ('BRANCH', 'message4')],
                                   'case2': [('WORKFLOW', 'message2'), ('ACTION', 'message3')],
                                   'case3': [('SYSTEM', 'message1'), ('ACTION', 'message3')],
                                   'case4': [('WORKFLOW', 'message2'), ('ACTION', 'message3')]}

        # check cases to events is as expected
        for case_name, expected_events in expected_event_messages.items():
            case = case_database.case_db.session.query(case_database.Case) \
                .filter(case_database.Case.name == case_name).all()
            self.assertEqual(len(case), 1, 'There are more than one cases sharing a name {0}'.format(case_name))

            case_event_info = [(event.type, event.message) for event in case[0].events.all()]

            self.assertEqual(len(case_event_info), len(expected_events),
                             'Unexpected number of messages encountered for case {0}'.format(case_name))
            self.assertSetEqual(set(case_event_info), set(expected_events),
                                'Expected event info does not equal received event info for case {0}'.format(case_name))

        # check events to cases is as expected
        expected_cases = {'message1': ['case1', 'case3'],
                          'message2': ['case2', 'case4'],
                          'message3': ['case2', 'case3', 'case4'],
                          'message4': ['case1']}
        for event_message, message_cases in expected_cases.items():
            event = case_database.case_db.session.query(case_database.Event) \
                .filter(case_database.Event.message == event_message).all()

            self.assertEqual(len(event), 1,
                             'There are more than one events sharing a message {0}'.format(event_message))

            event_cases = [case.name for case in event[0].cases.all()]
            self.assertEqual(len(event_cases), len(message_cases),
                             'Unexpected number of cases encountered for messages {0}'.format(event_message))
            self.assertSetEqual(set(event_cases), set(message_cases),
                                'Expected cases does not equal received cases info for event {0}'.format(event_message))

    def test_edit_note(self):
        TestCaseDatabase.__construct_basic_db()

        event1 = case_database.Event(type='SYSTEM', message='message1')
        case_database.case_db.add_event(event=event1, cases=['case1', 'case3'])
        event2 = case_database.Event(type='WORKFLOW', message='message2')
        case_database.case_db.add_event(event=event2, cases=['case2', 'case4'])
        event3 = case_database.Event(type='ACTION', message='message3')
        case_database.case_db.add_event(event=event3, cases=['case2', 'case3', 'case4'])
        event4 = case_database.Event(type='BRANCH', message='message4')
        case_database.case_db.add_event(event=event4, cases=['case1'])

        events = case_database.case_db.session.query(case_database.Event).all()
        smallest_id = min([event.id for event in events])
        expected_json_list = [event.as_json() for event in events]
        for event in expected_json_list:
            if event['id'] == smallest_id:
                event['note'] = 'Note1'

        case_database.case_db.edit_event_note(smallest_id, 'Note1')
        events = case_database.case_db.session.query(case_database.Event).all()
        result_json_list = [event.as_json() for event in events]
        self.assertEqual(len(result_json_list), len(expected_json_list))
        self.assertTrue(all(expected_event in result_json_list for expected_event in expected_json_list))

    def test_edit_note_invalid_id(self):
        TestCaseDatabase.__construct_basic_db()

        event1 = case_database.Event(type='SYSTEM', message='message1')
        case_database.case_db.add_event(event=event1, cases=['case1', 'case3'])
        event2 = case_database.Event(type='WORKFLOW', message='message2')
        case_database.case_db.add_event(event=event2, cases=['case2', 'case4'])
        event3 = case_database.Event(type='ACTION', message='message3')
        case_database.case_db.add_event(event=event3, cases=['case2', 'case3', 'case4'])
        event4 = case_database.Event(type='BRANCH', message='message4')
        case_database.case_db.add_event(event=event4, cases=['case1'])

        events = case_database.case_db.session.query(case_database.Event).all()
        expected_json_list = [event.as_json() for event in events]

        case_database.case_db.edit_event_note(None, 'Note1')
        events = case_database.case_db.session.query(case_database.Event).all()
        result_json_list = [event.as_json() for event in events]
        self.assertEqual(len(result_json_list), len(expected_json_list))
        self.assertTrue(all(expected_event in result_json_list for expected_event in expected_json_list))

        invalid_id = max([event.id for event in events]) + 1
        case_database.case_db.edit_event_note(invalid_id, 'Note1')
        events = case_database.case_db.session.query(case_database.Event).all()
        result_json_list = [event.as_json() for event in events]
        self.assertEqual(len(result_json_list), len(expected_json_list))
        self.assertTrue(all(expected_event in result_json_list for expected_event in expected_json_list))

    def test_data_json_field(self):
        TestCaseDatabase.__construct_basic_db()
        event4_data = {"a": 4, "b": [1, 2, 3], "c": "Some_String"}
        event1 = case_database.Event(type='SYSTEM', message='message1')
        case_database.case_db.add_event(event=event1, cases=['case1', 'case3'])
        event2 = case_database.Event(type='WORKFLOW', message='message2', data='some_string')
        case_database.case_db.add_event(event=event2, cases=['case2', 'case4'])
        event3 = case_database.Event(type='ACTION', message='message3', data=6)
        case_database.case_db.add_event(event=event3, cases=['case2', 'case3', 'case4'])
        event4 = case_database.Event(type='BRANCH', message='message4', data=json.dumps(event4_data))
        case_database.case_db.add_event(event=event4, cases=['case1'])

        events = case_database.case_db.session.query(case_database.Event).all()
        event_json_list = [event.as_json() for event in events]
        input_output = {'message1': '',
                        'message2': 'some_string',
                        'message3': 6,
                        'message4': event4_data}

        self.assertEqual(len(event_json_list), len(list(input_output.keys())))
        for event in event_json_list:
            self.assertIn(event['message'], input_output)
            self.assertEqual(event['data'], input_output[event['message']])
