from os import sep
from os.path import join

test_path = join('.', 'walkoff', 'tests')
test_workflows_path = join('.', 'walkoff', 'tests', 'testWorkflows') + sep
test_invalid_workflows_path = join('.', 'walkoff', 'tests', 'testWorkflows', 'invalid_workflows') + sep
test_workflows_path_with_generated = join('.', 'walkoff', 'tests', 'testWorkflows', 'testGeneratedWorkflows') + sep
test_workflows_backup_path = join('.', 'walkoff', 'tests', 'testWorkflows', 'testGeneratedWorkflows_bkup') + sep
test_apps_path = join('.', 'walkoff', 'tests', 'testapps')
test_data_dir_name = 'testdata'
test_data_path = join('.', 'walkoff', 'tests', test_data_dir_name)
test_appdevice_backup = join(test_data_path, 'appdevice.json')
test_cases_backup = join(test_data_path, 'cases.json')
basic_app_api = join('.', 'walkoff', 'tests', 'schemas', 'basic_app_api.yaml')

