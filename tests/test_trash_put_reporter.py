import unittest

from mock import Mock, call
from trashcli.put.reporter import TrashPutReporter


class TestTrashPutReporter(unittest.TestCase):
    def setUp(self):
        self.logger = Mock(['warning2'])
        describer = Mock()
        describer.describe.return_value = "file-description"
        self.reporter = TrashPutReporter(self.logger, describer)

    def test_it_should_record_failures(self):
        self.reporter.unable_to_trash_file('a file', 'trash-put')

        assert [call('cannot trash file-description \'a file\'', 'trash-put')] == \
               self.logger.warning2.mock_calls
