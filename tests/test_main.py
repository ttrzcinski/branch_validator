from unittest import TestCase

import main


class BranchValidatorTest(TestCase):

    def test_check_entered_param_with_None(self):
        # Given
        test_object = None
        test_result = False

        # When
        with self.assertRaises(SystemExit) as cm:
            test_result = main.check_entered_param(test_object)

        # Then
        self.assertEqual(cm.exception.code, 'Mandatory param name was not given.')
