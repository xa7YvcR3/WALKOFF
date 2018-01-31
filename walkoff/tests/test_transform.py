import unittest
import uuid

import walkoff.appgateway
import walkoff.config.config
from walkoff.core.argument import Argument
from walkoff.core.executionelements.transform import Transform
from walkoff.helpers import UnknownTransform, InvalidArgument
from walkoff.tests.config import test_apps_path


class TestTransform(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        walkoff.appgateway.clear_cache()
        walkoff.appgateway.cache_apps(path=test_apps_path)
        walkoff.config.config.load_app_apis(test_apps_path)

    @classmethod
    def tearDownClass(cls):
        walkoff.appgateway.clear_cache()

    def __compare_init(self, elem, app_name, action_name, arguments=None, uid=None):
        arguments = arguments if arguments is not None else {}
        self.assertEqual(elem.app_name, app_name)
        self.assertEqual(elem.action_name, action_name)
        arguments = {arg.name: arg for arg in arguments}
        if arguments:
            self.assertDictEqual(elem.arguments, arguments)
        if uid is None:
            self.assertIsNotNone(elem.uid)
        else:
            self.assertEqual(elem.uid, uid)

    def test_init_action_only(self):
        filter_elem = Transform('HelloWorld', 'Top Transform')
        self.__compare_init(filter_elem, 'HelloWorld', 'Top Transform')

    def test_init_invalid_action(self):
        with self.assertRaises(UnknownTransform):
            Transform('HelloWorld', 'Invalid')

    def test_init_with_uid(self):
        uid = uuid.uuid4().hex
        filter_elem = Transform('HelloWorld', 'Top Transform', uid=uid)
        self.__compare_init(filter_elem, 'HelloWorld', 'Top Transform', uid=uid)

    def test_init_with_args(self):
        filter_elem = Transform('HelloWorld', action_name='mod1_filter2', arguments=[Argument('arg1', value='5.4')])
        self.__compare_init(filter_elem, 'HelloWorld', 'mod1_filter2', arguments=[Argument('arg1', value='5.4')])

    def test_init_with_args_with_routing(self):
        filter_elem = Transform('HelloWorld', action_name='mod1_filter2',
                                arguments=[Argument('arg1', reference="action1")])
        self.__compare_init(filter_elem, 'HelloWorld', 'mod1_filter2',
                            arguments=[Argument('arg1', reference="action1")])

    def test_init_with_invalid_arg_name(self):
        with self.assertRaises(InvalidArgument):
            Transform('HelloWorld', action_name='mod1_filter2', arguments=[Argument('invalid', value='5.4')])

    def test_init_with_invalid_arg_type(self):
        with self.assertRaises(InvalidArgument):
            Transform('HelloWorld', action_name='mod1_filter2', arguments=[Argument('arg1', value='invalid')])

    def test_execute_with_no_args_no_conversion(self):
        self.assertAlmostEqual(Transform('HelloWorld', 'Top Transform').execute(5.4, {}), 5.4)

    def test_execute_with_no_args_with_conversion(self):
        self.assertAlmostEqual(Transform('HelloWorld', 'Top Transform').execute('-10.437', {}), -10.437)

    def test_execute_with_invalid_input(self):
        self.assertEqual(Transform('HelloWorld', 'Top Transform').execute('invalid', {}), 'invalid')

    def test_execute_with_filter_which_raises_exception(self):
        self.assertEqual(Transform('HelloWorld', 'sub1_filter3').execute('anything', {}), 'anything')

    def test_execute_with_args_no_conversion(self):
        self.assertAlmostEqual(
            Transform('HelloWorld', action_name='mod1_filter2', arguments=[Argument('arg1', value='10.3')]).execute(
                '5.4', {}), 15.7)

    def test_execute_with_args_with_conversion(self):
        self.assertAlmostEqual(
            Transform('HelloWorld', action_name='mod1_filter2', arguments=[Argument('arg1', value='10.3')]).execute(5.4,
                                                                                                                    {}),
            15.7)

    def test_execute_with_args_with_routing(self):
        self.assertAlmostEqual(
            Transform('HelloWorld', action_name='mod1_filter2',
                      arguments=[Argument('arg1', reference="action1")]).execute(5.4, {'action1': 10.3}),
            15.7)

    def test_execute_with_complex_args(self):
        original_filter = Transform('HelloWorld', action_name='sub1_filter1',
                                    arguments=[Argument('arg1', value={'a': '5.4', 'b': 'string_in'})])
        self.assertEqual(original_filter.execute(3, {}), '3.0 5.4 string_in')

    def test_call_with_nested_complex_args(self):
        args = [Argument('arg', value={'a': '4', 'b': 6, 'c': [1, 2, 3]})]
        original_filter = Transform('HelloWorld', action_name='complex', arguments=args)
        self.assertAlmostEqual(original_filter.execute(3, {}), 19.0)

    def test_call_with_args_invalid_input(self):
        self.assertEqual(
            Transform('HelloWorld', action_name='mod1_filter2', arguments=[Argument('arg1', value='10.3')]).execute(
                'invalid', {}),
            'invalid')
