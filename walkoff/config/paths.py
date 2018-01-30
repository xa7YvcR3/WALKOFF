from os.path import join
from os import sep

arby_path = join('.', 'arby')
data_path = join(arby_path, 'walkoff_data')

installed_apps_path = join(arby_path, 'walkoff_apps')
installed_interfaces_path = join(arby_path, 'walkoff_interfaces')

base_apps_path = join('.', 'walkoff', 'appbase')
base_interfaces_path = join('.', 'walkoff', 'interfacebase')

api_path = join('.', 'walkoff', 'api')
case_db_path = join(data_path, 'events.db')

client_path = join('.', 'walkoff', 'client')
config_path = join(data_path, 'walkoff.config')
db_path = join(data_path, 'walkoff.db')
default_appdevice_export_path = join(data_path, 'appdevice.json')
default_case_export_path = join(data_path, 'cases.json')
device_db_path = join(data_path, 'devices.db')
keywords_path = join('.', 'walkoff', 'keywords')
logging_config_path = join(data_path, 'log', 'logging.json')

walkoff_schema_path = join(data_path, 'walkoff_schema.json')
workflows_path = join('.', 'workflows')

keys_path = join(arby_path, '.certificates')
certificate_path = join(keys_path, 'walkoff.crt')
private_key_path = join(keys_path, 'walkoff.key')
zmq_private_keys_path = join(keys_path, 'private_keys')
zmq_public_keys_path = join(keys_path, 'public_keys')


