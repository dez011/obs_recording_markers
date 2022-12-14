import datetime
from unittest import TestCase
from .ObsRecordingMarker import *


class Test(TestCase):
    arguments = ['del', 'mod']
    Data.file_path_from_gui = 'O:/RECORDINGS/devTest.csv'

    def test_cb8_mod(self):
        last_row = cb8(True, '10:00 mod')
        last_row_2 = cb8(True, '10:00 mod')

        start = int(last_row['TYPE'].split(':').pop(0))
        end = int(last_row_2['TYPE'].split(':').pop(0))
        assert (start - end == -10)

    def test_cb_del(self):
        del_row = cb8(True, 'del')
        assert del_row == 'Deleted last row'

    def test_cb_append(self):
        stopwatch.start()
        stopwatch.start_time = datetime.datetime.now()

        Data.is_recording = True
        Data.time = '01:00:01' #get_time_hh_mm_ss(stopwatch.get_elapsed_time_int_for_file())
        Data.date = datetime.datetime.now().strftime(y_m_d_h_m_s)
        Data.status = ''
        Data.link_id = ''
        Data.recording_file = ''

        appended = cb8(True, '10:10')
        assert 'Appended to file' in appended[0]