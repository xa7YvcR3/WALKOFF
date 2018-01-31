import json
from datetime import timedelta

import walkoff.server.metrics as metrics
from walkoff.server import flaskserver as server
from walkoff.server.endpoints.metrics import _convert_action_time_averages, _convert_workflow_time_averages
from walkoff.tests import config
from walkoff.tests.util.assertwrappers import orderless_list_compare
from walkoff.tests.util.servertestcase import ServerTestCase


class MetricsServerTest(ServerTestCase):
    def setUp(self):
        metrics.app_metrics = {}

    def test_convert_action_time_average(self):
        '''
        ret = deepcopy(metrics.app_metrics)
        for app in ret:
            for action in app['actions']:
                ret[app]['actions'][action]['avg_time'] = str(action['avg_time'])
        return ret
        '''

        test1 = {'app1': {'actions': {'action1': {'success': {'count': 0,
                                                              'avg_time': timedelta(100, 0, 1)}},
                                      'action2': {'error': {'count': 2,
                                                            'avg_time': timedelta(0, 0, 1000)}}},
                          'count': 2},
                 'app2': {'actions': {'action1': {'success': {'count': 0,
                                                              'avg_time': timedelta(0, 100, 1)},
                                                  'error': {'count': 100,
                                                            'avg_time': timedelta(1, 100, 500)}}},
                          'count': 100}}
        expected_json = {'apps': [{'count': 100,
                                   'name': 'app2',
                                   'actions': [{'error_metrics': {'count': 100,
                                                                  'avg_time': '1 day, 0:01:40.000500'},
                                                'success_metrics': {'count': 0,
                                                                    'avg_time': '0:01:40.000001'},
                                                'name': 'action1'}]},
                                  {'count': 2,
                                   'name': 'app1',
                                   'actions': [{'success_metrics': {'count': 0,
                                                                    'avg_time': '100 days, 0:00:00.000001'},
                                                'name': 'action1'},
                                               {'error_metrics': {'count': 2,
                                                                  'avg_time': '0:00:00.001000'},
                                                'name': 'action2'}]}]}
        metrics.app_metrics = test1
        converted = _convert_action_time_averages()
        orderless_list_compare(self, converted.keys(), ['apps'])
        self.assertEqual(len(converted['apps']), len(expected_json['apps']))
        orderless_list_compare(self, [x['name'] for x in converted['apps']], ['app1', 'app2'])

        app1_metrics = [x for x in converted['apps'] if x['name'] == 'app1'][0]
        expected_app1_metrics = [x for x in expected_json['apps'] if x['name'] == 'app1'][0]
        orderless_list_compare(self, app1_metrics.keys(), ['count', 'name', 'actions'])
        self.assertEqual(app1_metrics['count'], expected_app1_metrics['count'])
        self.assertTrue(len(app1_metrics['actions']), len(expected_app1_metrics['actions']))
        for action_metric in expected_app1_metrics['actions']:
            self.assertIn(action_metric, app1_metrics['actions'])

        app2_metrics = [x for x in converted['apps'] if x['name'] == 'app2'][0]
        expected_app2_metrics = [x for x in expected_json['apps'] if x['name'] == 'app2'][0]
        orderless_list_compare(self, app2_metrics.keys(), ['count', 'name', 'actions'])
        self.assertEqual(app2_metrics['count'], expected_app2_metrics['count'])
        self.assertTrue(len(app2_metrics['actions']), len(expected_app2_metrics['actions']))
        for action_metric in expected_app2_metrics['actions']:
            self.assertIn(action_metric, app2_metrics['actions'])

    def test_convert_workflow_time_average(self):
        test1 = {'workflow1': {'count': 0,
                               'avg_time': timedelta(100, 0, 1)},
                 'workflow2': {'count': 2,
                               'avg_time': timedelta(0, 0, 1000)},
                 'workflow3': {'count': 0,
                               'avg_time': timedelta(0, 100, 1)},
                 'workflow4': {'count': 100,
                               'avg_time': timedelta(1, 100, 500)}}
        expected_json = {'workflows': [{'count': 100,
                                        'avg_time': '1 day, 0:01:40.000500',
                                        'name': 'workflow4'},
                                       {'count': 2,
                                        'avg_time': '0:00:00.001000',
                                        'name': 'workflow2'},
                                       {'count': 0,
                                        'avg_time': '0:01:40.000001',
                                        'name': 'workflow3'},
                                       {'count': 0,
                                        'avg_time': '100 days, 0:00:00.000001',
                                        'name': 'workflow1'}]}
        metrics.workflow_metrics = test1
        converted = _convert_workflow_time_averages()
        orderless_list_compare(self, converted.keys(), ['workflows'])
        self.assertEqual(len(converted['workflows']), len(expected_json['workflows']))
        for workflow in expected_json['workflows']:
            self.assertIn(workflow, converted['workflows'])

    def test_action_metrics(self):
        server.running_context.controller.load_playbook(resource=config.test_workflows_path +
                                                                 'multiactionError.playbook')

        server.running_context.controller.execute_workflow('multiactionError', 'multiactionErrorWorkflow')
        server.running_context.controller.wait_and_reset(1)

        response = self.app.get('/metrics/apps', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response = json.loads(response.get_data(as_text=True))
        self.assertDictEqual(response, _convert_action_time_averages())

    def test_workflow_metrics(self):
        server.running_context.controller.load_playbook(resource=config.test_workflows_path +
                                                                 'multiactionError.playbook')
        server.running_context.controller.load_playbook(resource=config.test_workflows_path +
                                                                 'multiactionWorkflowTest.playbook')
        server.running_context.controller.execute_workflow('multiactionError', 'multiactionErrorWorkflow')
        server.running_context.controller.execute_workflow('multiactionError', 'multiactionErrorWorkflow')
        server.running_context.controller.execute_workflow('multiactionWorkflowTest', 'multiactionWorkflow')
        server.running_context.controller.wait_and_reset(3)

        response = self.app.get('/metrics/workflows', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response = json.loads(response.get_data(as_text=True))
        self.assertDictEqual(response, _convert_workflow_time_averages())
