import datetime
from unittest import TestCase
from .ObsRecordingMarker import *


class Test(TestCase):
    arguments = ['del', 'mod']
    Data.file_path_from_gui = 'O:/RECORDINGS/devTest.csv'

    def test_cb8_mod(self):
        self.set_up_testing_env()
        last_row = cb8(True, '10:00 mod')
        last_row_2 = cb8(True, '10:00 mod')
        # set default for test to '10:200'
        start = int(last_row.split(':').pop(0))
        end = int(last_row.split(':').pop(1))
        assert (start + end == 220)

    # def test_cb_del(self):
    #     self.set_up_testing_env()
    #     Data.events_path_from_gui = 'Events.csv'
    #     del_row = cb8(True, 'del')
    #     assert del_row == 'Deleted last row'

    # def test_cb_append(self):
    #     stopwatch.start()
    #     stopwatch.start_time = datetime.datetime.now()
    #
    #     Data.is_recording = True
    #     Data.time = '01:00:01' #get_time_hh_mm_ss(stopwatch.get_elapsed_time_int_for_file())
    #     Data.date = datetime.datetime.now().strftime(y_m_d_h_m_s)
    #     Data.status = ''
    #     Data.link_id = ''
    #     Data.recording_file = ''
    #
    #     appended = cb8(True, '10:10')
    #     assert 'Appended to file' in appended[0]

    def test_most_recent_file(self):
        most_recent = most_recent_file(['O:\RECORDINGS'])

    def test_three_digit_hk(self):
        self.set_up_testing_env()
        last_row = cb8(True, e_text_test='600:100')
        assert last_row == '600:100' #added correctly
        mod_row = cb8(True, e_text_test='mod 180:10')
        assert last_row == '190:210' #modified correctly. set default for test to '10:200'

    def set_up_testing_env(self):
        Data.testing = True
        Data.events_path_from_gui = 'testing.csv'
