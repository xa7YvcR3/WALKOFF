from unittest import TestCase

from walkoff.appbase import App as AppBase
from walkoff.devicedb import App, Device, DeviceField, EncryptedDeviceField, device_db


class TestAppBase(TestCase):
    def setUp(self):
        self.test_app_name = 'TestApp'
        self.device1 = Device('test', [], [], 'type1')
        plaintext_fields = [DeviceField('test_name', 'integer', 123), DeviceField('test2', 'string', 'something')]
        encrypted_fields = [EncryptedDeviceField('test3', 'boolean', True),
                            EncryptedDeviceField('test4', 'string', 'something else')]
        self.device2 = Device('test2', plaintext_fields, encrypted_fields, 'type2')
        self.db_app = App(name=self.test_app_name, devices=[self.device1, self.device2])

        device_db.session.add(self.db_app)
        device_db.session.commit()

    def tearDown(self):
        device_db.session.rollback()
        for device in device_db.session.query(Device).all():
            device_db.session.delete(device)
        for field in device_db.session.query(DeviceField).all():
            device_db.session.delete(field)
        for field in device_db.session.query(EncryptedDeviceField).all():
            device_db.session.delete(field)
        app = device_db.session.query(App).filter(App.name == self.test_app_name).first()
        if app is not None:
            device_db.session.delete(app)
        device_db.session.commit()

    def test_app_is_tagged(self):
        self.assertTrue(getattr(AppBase, '_is_walkoff_app', False))

    def test_init(self):
        app = AppBase(self.test_app_name, self.device1.id)
        self.assertEqual(app.app, self.db_app)
        self.assertEqual(app.device, self.device1)
        self.assertDictEqual(app.device_fields, {})
        self.assertEqual(app.device_type, 'type1')
        self.assertEqual(app.device_id, self.device1.id)

    def test_init_with_fields(self):
        app = AppBase(self.test_app_name, self.device2.id)
        self.assertEqual(app.app, self.db_app)
        self.assertEqual(app.device, self.device2)
        self.assertDictEqual(app.device_fields, self.device2.get_plaintext_fields())
        self.assertEqual(app.device_type, 'type2')
        self.assertEqual(app.device_id, self.device2.id)

    def test_init_with_invalid_app(self):
        app = AppBase('Invalid', self.device2.id)
        self.assertIsNone(app.app)
        self.assertIsNone(app.device)
        self.assertDictEqual(app.device_fields, {})
        self.assertEqual(app.device_type, None)
        self.assertEqual(app.device_id, self.device2.id)

    def test_init_with_invalid_device(self):
        app = AppBase(self.test_app_name, 'invalid')
        self.assertEqual(app.app, self.db_app)
        self.assertIsNone(app.device)
        self.assertDictEqual(app.device_fields, {})
        self.assertEqual(app.device_type, None)
        self.assertEqual(app.device_id, 'invalid')

    def test_get_all_devices(self):
        app = AppBase(self.test_app_name, self.device2.id)
        devices = app.get_all_devices()
        self.assertIn(self.device1, devices)
        self.assertIn(self.device2, devices)

    def test_get_all_devices_invalid_app(self):
        app = AppBase('Invalid', self.device2.id)
        self.assertListEqual(app.get_all_devices(), [])
