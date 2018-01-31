from unittest import TestLoader, TestSuite
from . import *


def add_tests_to_suite(suite, test_modules):
    suite.addTests([TestLoader().loadTestsFromModule(test_module) for test_module in test_modules])

__case_tests = [test_case_subscriptions, test_case_database, test_case_config_db]
case_suite = TestSuite()
add_tests_to_suite(case_suite, __case_tests)

__server_tests = [test_workflow_server, test_app_api_server, test_case_server, test_configuration_server, test_scheduler_actions,
                  test_device_server, test_app_blueprint, test_metrics_server,
                  test_scheduledtasks_database, test_scheduledtasks_server, test_authentication, test_roles_server,
                  test_users_server, test_message_history_database, test_message_db,
                  test_message, test_messaging_endpoints, test_workflow_authorization,
                  test_workflow_authorized_user_set, test_workflow_authorization_cache, test_trigger_helpers,
                  test_system_server]
server_suite = TestSuite()
add_tests_to_suite(server_suite, __server_tests)

__execution_tests = [test_argument, test_execution_runtime, test_execution_element, test_execution_events, test_execution_modes,
                     test_action, test_helper_functions, test_transform, test_condition, test_branch,
                     test_app_instance, test_controller, test_metrics,
                     test_app_utilities, test_input_validation, test_decorators,
                     test_app_api_validation, test_condition_transform_validation, test_workflow_results,
                     test_roles_pages_database, test_users_roles_database, test_playbook,
                     test_json_element_creator, test_json_element_reader, test_json_playbook_loader, test_playbook_store,
                     test_scheduler, test_walkoff_tag, test_app_cache, test_app_base]
execution_suite = TestSuite()
add_tests_to_suite(execution_suite, __execution_tests)

__workflow_tests = [test_load_workflow, test_simple_workflow, test_workflow_manipulation]
workflow_suite = TestSuite()
add_tests_to_suite(workflow_suite, __workflow_tests)

__integration_tests = [test_zmq_communication, test_zmq_communication_server, test_triggers_server]
integration_suite = TestSuite()
add_tests_to_suite(integration_suite, __integration_tests)

__interface_tests = [test_callback_container, test_interface_event_dispatch_helpers, test_app_action_event_dispatcher,
                     test_app_event_dispatcher, test_event_dispatcher, test_interface_event_dispatcher, test_events]
interface_suite = TestSuite()
add_tests_to_suite(interface_suite, __interface_tests)

full_suite = TestSuite()
for tests in [__workflow_tests, __execution_tests, __case_tests, __server_tests, __interface_tests]:
    add_tests_to_suite(full_suite, tests)
