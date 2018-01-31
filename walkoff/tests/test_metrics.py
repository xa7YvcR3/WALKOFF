import walkoff.server.metrics as metrics
from walkoff.server import flaskserver as server
from walkoff.tests import config
from walkoff.tests.util.assertwrappers import orderless_list_compare
from walkoff.tests.util.servertestcase import ServerTestCase


class MetricsTest(ServerTestCase):
    def setUp(self):
        metrics.app_metrics = {}
        metrics.workflow_metrics = {}

    def test_action_metrics(self):
        server.running_context.controller.load_playbook(resource=config.test_workflows_path +
                                                                 'multiactionError.playbook')

        server.running_context.controller.execute_workflow('multiactionError', 'multiactionErrorWorkflow')

        server.running_context.controller.wait_and_reset(1)
        self.assertListEqual(list(metrics.app_metrics.keys()), ['HelloWorldBounded'])
        orderless_list_compare(self, list(metrics.app_metrics['HelloWorldBounded'].keys()), ['count', 'actions'])
        self.assertEqual(metrics.app_metrics['HelloWorldBounded']['count'], 3)
        orderless_list_compare(self,
                               list(metrics.app_metrics['HelloWorldBounded']['actions'].keys()),
                               ['repeatBackToMe', 'helloWorld', 'Buggy'])
        orderless_list_compare(self,
                               list(metrics.app_metrics['HelloWorldBounded']['actions']['repeatBackToMe'].keys()),
                               ['success'])
        for form in ['success']:
            orderless_list_compare(self,
                                   list(metrics.app_metrics['HelloWorldBounded']['actions']['repeatBackToMe'][
                                            form].keys()),
                                   ['count', 'avg_time'])
            self.assertEqual(metrics.app_metrics['HelloWorldBounded']['actions']['repeatBackToMe'][form]['count'], 1)
        orderless_list_compare(self,
                               list(metrics.app_metrics['HelloWorldBounded']['actions']['helloWorld'].keys()),
                               ['success'])
        orderless_list_compare(self,
                               list(
                                   metrics.app_metrics['HelloWorldBounded']['actions']['helloWorld']['success'].keys()),
                               ['count', 'avg_time'])
        self.assertEqual(metrics.app_metrics['HelloWorldBounded']['actions']['helloWorld']['success']['count'], 1)

    def test_workflow_metrics(self):
        server.running_context.controller.load_playbook(resource=config.test_workflows_path +
                                                                 'multiactionError.playbook')
        server.running_context.controller.load_playbook(resource=config.test_workflows_path +
                                                                 'multiactionWorkflowTest.playbook')

        error_key = 'multiactionErrorWorkflow'
        multiaction_key = 'multiactionWorkflow'
        server.running_context.controller.execute_workflow('multiactionError', 'multiactionErrorWorkflow')
        server.running_context.controller.execute_workflow('multiactionError', 'multiactionErrorWorkflow')
        server.running_context.controller.execute_workflow('multiactionWorkflowTest', 'multiactionWorkflow')

        server.running_context.controller.wait_and_reset(3)

        keys = [error_key, multiaction_key]
        orderless_list_compare(self,
                               list(metrics.workflow_metrics.keys()),
                               keys)

        for key in keys:
            orderless_list_compare(self, metrics.workflow_metrics[key], ['count', 'avg_time'])

        self.assertEqual(metrics.workflow_metrics[error_key]['count'], 2)
        self.assertEqual(metrics.workflow_metrics[multiaction_key]['count'], 1)
