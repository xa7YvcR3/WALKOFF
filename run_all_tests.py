from scripts.compose_api import compose_api

compose_api()

import unittest
import sys
from tests import suites as test_suites
import logging
import walkoff.server.context
import argparse


def run_tests(arg):
    logging.disable(logging.CRITICAL)

    ret = True
    if arg.all or arg.integration:
        print('Testing Integration:')
        ret &= unittest.TextTestRunner(verbosity=1).run(test_suites.integration_suite).wasSuccessful()

    if arg.all or arg.workflows:
        print('Testing Workflows:')
        ret &= unittest.TextTestRunner(verbosity=1).run(test_suites.workflow_suite).wasSuccessful()

    if arg.all or arg.execution:
        print('\nTesting Execution:')
        ret &= unittest.TextTestRunner(verbosity=1).run(test_suites.execution_suite).wasSuccessful()

    if arg.all or arg.cases:
        print('\nTesting Cases:')
        ret &= unittest.TextTestRunner(verbosity=1).run(test_suites.case_suite).wasSuccessful()

    if arg.all or arg.server:
        print('\nTesting Server:')
        ret &= unittest.TextTestRunner(verbosity=1).run(test_suites.server_suite).wasSuccessful()

    if arg.all or arg.interface:
        print('\nTesting Interface:')
        ret &= unittest.TextTestRunner(verbosity=1).run(test_suites.interface_suite).wasSuccessful()

    return ret


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-a", "--all", action="store_true")
        parser.add_argument("-ig", "--integration", action="store_true")
        parser.add_argument("-w", "--workflows", action="store_true")
        parser.add_argument("-e", "--execution", action="store_true")
        parser.add_argument("-c", "--cases", action="store_true")
        parser.add_argument("-s", "--server", action="store_true")
        parser.add_argument("-if", "--interface", action="store_true")
        args = parser.parse_args()
        if len(sys.argv) == 1:
            args.all = True

        successful = run_tests(args)
    except KeyboardInterrupt:
        print('\nInterrupted! Ending full test')
        successful = False
    finally:
        walkoff.server.context.running_context.controller.shutdown_pool()
        sys.exit(not successful)
