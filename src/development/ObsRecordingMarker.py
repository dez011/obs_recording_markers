import csv
import glob
import os
import pathlib
import re
import sys
from threading import Thread
import time
from pathlib import Path
import datetime
import obspython as S


FILE_EXT = '.mp4'

FILE = 'FILE'

LINK_ID = 'LINK ID'

STATUS = 'STATUS'

DATE = 'DATE'

TYPE = 'TYPE'

TIME = 'TIME'

recording_path = "O:\RECORDINGS"

csv_file_name = "testScriptFile.csv"

file_path = Path(recording_path) / csv_file_name


y_m_d_h_m_s = "%Y-%m-%d %H:%M:%S"


def get_sec(time_str='1:23:45'):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def get_time_hh_mm_ss(seconds=0):
    # get min and seconds first
    mm, ss = divmod(seconds, 60)
    # Get hours
    hh, mm = divmod(mm, 60)

    return f"{hh}:{mm}:{ss}"


file_headers = [('%s' % TIME), ('%s' % TYPE), DATE, STATUS, LINK_ID, FILE]


def append_data_to_file_from(json):
    # list of column names
    # Dictionary that we want to add as a new row
    with open(file_path, 'a') as f_object:
        dictwriter_object = csv.DictWriter(f_object, fieldnames=file_headers, lineterminator='\n')
        dictwriter_object.writerow(json)
        f_object.close()


def create_event_file():
    if 'test' in Data.file_path_from_gui:
        Data.file_path_from_gui = file_path
    file_exists = Path(Data.file_path_from_gui).is_file()

    # creates a new csv file with headers if it doesn't already exist
    with open(Data.file_path_from_gui, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=file_headers)
        if not file_exists:
            writer.writeheader()


def list_files(path_list=[]):
    extensions = ('*.mkv', '*.mov', '*.mp4', '*mkv')
    files = []
    for path in path_list:
        for ext in extensions:
            for file_path in Path(path).glob(ext):
                files.append(file_path)
    return files


def most_recent_file(path_list=[]):
    path_list = list_files(path_list)

    def most_recent(file_time_dict):
        newest_date = datetime.datetime(1999, 1, 1, 22, 50, 50)
        newest_path = ''
        # newest = {'empty': newest_date}
        for k, v in file_time_dict.items():
            if v > newest_date:
                newest_date = v
                newest_path = k
        return newest_path

    file_c_time = {}
    for path in path_list:
        c_timestamp = Path(path).stat().st_ctime
        c_time = datetime.datetime.fromtimestamp(c_timestamp)
        file_c_time.update({path: c_time})
    newest = most_recent(file_c_time)
    name, ext = os.path.splitext(Path(newest).name)
    newest = str(most_recent(file_c_time))
    newest = new_recording_file(newest)
    if e_remux.txt is True:
        newest = newest.replace(ext, FILE_EXT)
    return newest


class StopWatch:
    def __init__(self):
        self.start_time = None
        self.stop_time = None
        self.save_elapsed = 0

    def start(self):
        self.start_time = datetime.datetime.now()
        Data.is_recording = True
        return self.start_time

    def stop(self):
        self.stop_time = datetime.datetime.now()
        self.start_time = None
        self.save_elapsed = 0
        Data.is_recording = False
        return self.stop_time

    def pause(self):
        self.save_elapsed += self.get_elapsed_time_int_for_file()
        Data.is_recording = False
        self.start_time = None
        self.stop_time = None

    def get_elapsed_time_str_not_formatted(self):
        if Data.is_recording is True:
            self.stop_time = datetime.datetime.now()
            elapsed = (self.stop_time - self.start_time).total_seconds()
            elapsed = elapsed + self.save_elapsed
            elapsed_str = str(elapsed).split('.')[0]
            return elapsed_str

    def get_elapsed_time_int_for_file(self):
        if Data.is_recording is True:
            return int(self.get_elapsed_time_str_not_formatted())
        else:
            return None


stopwatch = StopWatch()

print(S)


class Data:
    OutputDir = None
    Extension = None
    ExtensionMask = None
    Remove_MKV = None
    Delay = None

    time = None
    type = None
    date = None
    status = None
    link_id = None
    file = None
    file_path_from_gui = None
    is_recording = False

    def to_json(self):
        clip_data_json = {}
        clip_data_json.update(
            {TIME: self.time, TYPE: self.type, DATE: self.date, STATUS: self.status, LINK_ID: self.link_id,
             FILE: self.file})
        return clip_data_json


def increment_file_counter(file):
    match = re.findall("\((.*?)\)", file)
    if match:
        old = match[0]
        new_index = int(match.pop()) + 1
        file = file.replace(old, str(new_index))
    return file


def new_recording_file(file):
    parenthesis_pattern = "\((.*?)\)"
    capture_paren = "(.\(..*\))"
    date_pattern = "[0-9]*-[0-9]*-[0-9]*"

    match_date = re.findall(date_pattern, file)
    match_paren = re.findall(parenthesis_pattern, file)
    match_to_remove = re.findall(capture_paren, file)
    dte_str = ''
    dte_format = '%m-%d-%y'
    if match_date:
        dte_str = match_date[0]
        dte_match = datetime.datetime.strptime(dte_str, dte_format).strftime(dte_format)
        dte_today = datetime.datetime.now().strftime(dte_format)
        if dte_match != dte_today:
            file = file.replace(dte_str, str(f'{dte_today}'))
            if len(match_to_remove) == 1:  # remove parenthesis if first recording for today and last days has (2)
                file = file.replace(match_to_remove.pop(), '')  # remove " (3)" from file name
        if dte_match == dte_today:  # found a file with todays date should add the "( )"
            # add (2).mkv if file exists
            if len(match_paren) == 0:
                file = file.replace(dte_str, str(f'{dte_today} (2)'))
            if len(match_paren) == 1:
                file = increment_file_counter(file)
        return file


class Application:
    def __init__(self, callback, obs_settings, _id):
        self.obs_data = obs_settings
        self.hotkey_id = S.OBS_INVALID_HOTKEY_ID
        self.hotkey_saved_key = None
        self.callback = callback
        self._id = _id

        self.load_hotkey()
        self.register_hotkey()
        self.save_hotkey()

    def register_hotkey(self):
        description = "Htk " + str(self._id)
        self.hotkey_id = S.obs_hotkey_register_frontend(
            "htk_id" + str(self._id), description, self.callback
        )
        S.obs_hotkey_load(self.hotkey_id, self.hotkey_saved_key)

    def load_hotkey(self):
        self.hotkey_saved_key = S.obs_data_get_array(
            self.obs_data, "htk_id" + str(self._id)
        )
        S.obs_data_array_release(self.hotkey_saved_key)

    def save_hotkey(self):
        self.hotkey_saved_key = S.obs_hotkey_save(self.hotkey_id)
        S.obs_data_set_array(
            self.obs_data, "htk_id" + str(self._id), self.hotkey_saved_key
        )
        S.obs_data_array_release(self.hotkey_saved_key)


class h:
    htk_copy = None  # this attribute will hold instance of Hotkey

#STEP1 CREATE FUNCTION FOR NEW HOTKEY

def cb1(pressed):
    if pressed:
        print("callback1: " + e1.txt, 'recording: ', Data.is_recording, stopwatch.get_elapsed_time_str_not_formatted())
        if Data.is_recording is True:
            Data.time = get_time_hh_mm_ss(stopwatch.get_elapsed_time_int_for_file())
            Data.type = e1.txt
            Data.date = datetime.datetime.now().strftime(y_m_d_h_m_s)
            Data.status = ''
            Data.link_id = ''
            Data.file = ''
            append_data_to_file_from(Data.to_json(Data))

def cb2(pressed):
    if pressed:
        print("callback2: " + e2.txt)

def cb3(pressed):
    if pressed:
        print("callback3: " + e3.txt)

class e:
    txt = "default txt"


def frontend_event_handler(data):
    global is_paused, stopwatch
    global window_start
    global loop_destroy
    # t1 = Thread(most_recent_file, args=(recording_path, '\*'))

    if data == S.OBS_FRONTEND_EVENT_RECORDING_STARTING:
        window_start = True
        is_paused = False
        stopwatch.start()
        file = most_recent_file([recording_path])
        print('Current file ', file)
        Data.time = '00:00:00'
        Data.type = 'SKIP'
        Data.date = datetime.datetime.now().strftime(y_m_d_h_m_s)
        Data.status = ''
        Data.link_id = ''
        Data.file = file
        append_data_to_file_from(Data.to_json(Data))
        Data.is_recording = True
        print('REC started..')

    if data == S.OBS_FRONTEND_EVENT_RECORDING_STOPPED:
        window_start = False
        is_paused = False
        is_recording = False
        stopwatch.stop()
        print('REC stops..')

    if data == S.OBS_FRONTEND_EVENT_RECORDING_PAUSED:
        is_paused = True
        is_recording = False
        stopwatch.get_elapsed_time_str_not_formatted()
        stopwatch.pause()
        print('REC paused..')

    if data == S.OBS_FRONTEND_EVENT_RECORDING_UNPAUSED:
        is_paused = False
        Data.is_recording = True
        stopwatch.start()
        print('REC un-paused..')

#STEP 2 INSTANTIATE THE CLASSES
e1 = e()
e2 = e()
e3 = e()
e_recording_path = e()
e_remux = e()

h1 = h()
h2 = h()
h3 = h()

#STEP3 ADD TO SCRIPT PROPERTIES
def script_properties():
    print('script props')
    props = S.obs_properties_create()
    hotkey_1 = "Hotkey 1"
    hotkey_2 = "Hotkey 2"
    hotkey_3 = "Hotkey 3"

    save_path = "Save Path"
    # name, type, description
    S.obs_properties_add_text(props, "_text", "Recording Path", S.OBS_TEXT_DEFAULT)
    S.obs_properties_add_text(props, "_text1", hotkey_1, S.OBS_TEXT_DEFAULT)
    S.obs_properties_add_text(props, "_text2", hotkey_2, S.OBS_TEXT_DEFAULT)
    S.obs_properties_add_text(props, "_text3", hotkey_3, S.OBS_TEXT_DEFAULT)

    _remux = S.obs_properties_add_bool(props, "_remux", "Remux Yes/No (Check/Uncheck)")

    return props

#STEP 4 ADD TO SCRIPT UPDATE
def script_update(settings):
    _text1 = S.obs_data_get_string(settings, "_text1")
    _text2 = S.obs_data_get_string(settings, "_text2")
    _text3 = S.obs_data_get_string(settings, "_text3")
    _text = S.obs_data_get_string(settings, "_text")
    _remux = S.obs_data_get_bool(settings, "_remux")
    e1.txt = _text1
    e2.txt = _text2
    e3.txt = _text3

    e_recording_path.txt = _text
    e_remux.txt = _remux

#STEP 5 ADD TO SCRIPT LOAD
def script_load(settings):
    Data.file_path_from_gui = S.obs_data_get_string(settings, "_text")
    create_event_file()
    Data.is_recording = False
    h1.htk_copy = Application(cb1, settings, "h1_id")
    h2.htk_copy = Application(cb2, settings, "h2_id")
    h3.htk_copy = Application(cb3, settings, "h3_id")



#STEP 5 ADD TO SCRIPT SAVE
def script_save(settings):
    h1.htk_copy.save_hotkey()
    h2.htk_copy.save_hotkey()
    h3.htk_copy.save_hotkey()

def script_description():
    return ("OBS RECORDING MARKER\n\n"
            "Restart OBS after adding the script\n"
            "You have to select a Python 3.6.X version folder \n"
            "*** File format: the/path/to/fileName 12-01-22.mp4 \n\n"
            "Will have an instructional video on my YouTube channel\n"
            "https://youtube.com/@DEZACTUALDOS\n\n")

S.obs_frontend_add_event_callback(frontend_event_handler)
