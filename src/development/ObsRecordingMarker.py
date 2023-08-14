import csv
import datetime
import os
import platform
import re
import json
from pathlib import Path

try:
    import obspython as S

    print(S)
except:
    pass

FILE_EXT = '.mp4'

FILE = 'FILE'

LINK_ID = 'LINK ID'

STATUS = 'STATUS'

DATE = 'DATE'

TYPE = 'TYPE'

TIME = 'TIME'

y_m_d_h_m_s = "%Y-%m-%d %H:%M:%S"

extensions = ('*.mkv', '*.mov', '*.mp4', '*mkv')

stable = False

# Define path to the configuration file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_PATH = os.path.join(SCRIPT_DIR, 'config.json')


def save_config():
    config_data = {}

    # Check if file exists, if yes then load existing values
    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, 'r') as file:
            config_data = json.load(file)

    # For each hotkey, only update its value if the new value is not blank
    if e1.txt.strip():
        config_data['e1'] = e1.txt
    if e2.txt.strip():
        config_data['e2'] = e2.txt
    if e3.txt.strip():
        config_data['e3'] = e3.txt
    if e4.txt.strip():
        config_data['e4'] = e4.txt
    if e5.txt.strip():
        config_data['e5'] = e5.txt
    if e6.txt.strip():
        config_data['e6'] = e6.txt
    if e7.txt.strip():
        config_data['e7'] = e7.txt
    if e8.txt.strip():
        config_data['e8'] = e8.txt

    # Now save the updated configuration data
    with open(CONFIG_FILE_PATH, 'w') as file:
        print('saving config')
        print(config_data)
        json.dump(config_data, file)


def load_config():
    print('opening config')

    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, 'r') as file:
            config_data = json.load(file)
            print(config_data)
            e1.txt = config_data.get('e1', e1.txt)
            e2.txt = config_data.get('e2', e2.txt)
            e3.txt = config_data.get('e3', e3.txt)
            e4.txt = config_data.get('e4', e4.txt)
            e5.txt = config_data.get('e5', e5.txt)
            e6.txt = config_data.get('e6', e6.txt)
            e7.txt = config_data.get('e7', e7.txt)
            e8.txt = config_data.get('e8', e8.txt)



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


def append_data_to_file_from(json={TYPE: '00:00', TIME: '00:10:00'}):
    # list of column names
    # Dictionary that we want to add as a new row
    if Data.testing is True:
        return 'Appended to file test ', json
    if Data.events_path_from_gui is None or Data.events_path_from_gui == '':
        print('Csv file is not set in script settings: ', Data.events_path_from_gui)
        return
    with open(Data.events_path_from_gui, 'a') as f_object:
        # with open(file_path, 'a') as f_object:
        dictwriter_object = csv.DictWriter(f_object, fieldnames=file_headers, lineterminator='\n')
        dictwriter_object.writerow(json)
        f_object.close()
    return 'Appended to file ', json


def create_event_file():
    os_ = platform.system()
    if Data.testing is True and stable is False:
        if os_ == 'Darwin':
            mac_path = str(Path('/Users/miguelhernandez/Documents/testObsScript') / Data.file_path_from_gui_name())
            Data.events_path_from_gui = mac_path
        if os_ == 'Windows':
            win_path = str(Path("O:\RECORDINGS\TESTS") / 'devTest.csv')
            Data.events_path_from_gui = win_path
            print('Created event file windows test ', Data.events_path_from_gui)
    file_exists = Path(Data.events_path_from_gui).is_file()
    print('Event file ', Data.events_path_from_gui, ' Recording path ', Data.recording_path_from_gui, ' Testing: ',
          Data.testing)
    if Data.events_path_from_gui is None or Data.events_path_from_gui == '':
        print('Csv file not valid: ', Data.events_path_from_gui)
        return
    # creates a new csv file with headers if it doesn't already exist
    print('Creating new Csv File: ', file_exists)
    with open(Data.events_path_from_gui, 'a') as csvfile:
        print(Path(str(csvfile)).absolute())
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=file_headers)
        if not file_exists:
            writer.writeheader()


def most_recent_file(path_list=[]):
    def most_recent(file_time_dict):
        newest_date = datetime.datetime(1999, 1, 1, 22, 50, 50)
        newest_path = ''
        # newest_not_processing_file = {'empty': newest_date}
        for k, v in file_time_dict.items():
            if v > newest_date:
                newest_date = v
                newest_path = k
        return newest_path

    def list_files(_path_list=[]):
        files = []
        for path in _path_list:
            for ext in extensions:
                for file_path in Path(path).glob(ext):
                    files.append(file_path)
        return files

    path_list = list_files(path_list)

    file_c_time = {}
    print("Looking for most recent file\nMake sure you dont have any other video files that dont match\nthe"
          "expected format for the script")
    for path in path_list:
        c_timestamp = Path(path).stat().st_ctime
        c_time = datetime.datetime.fromtimestamp(c_timestamp)
        file_c_time.update({path: c_time})

    newest_not_processing_file = most_recent(file_c_time)
    name, ext = os.path.splitext(Path(newest_not_processing_file).name)
    newest_not_processing_file = str(most_recent(file_c_time))
    assumed_newest_file = get_processing_new_filename(newest_not_processing_file)
    if e_remux.txt is True:
        assumed_newest_file = assumed_newest_file.replace(ext, FILE_EXT)
    return assumed_newest_file


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
            tme = int(self.get_elapsed_time_str_not_formatted())
            return tme
        else:
            return None


stopwatch = StopWatch()


class Data:
    testing = None
    Remove_MKV = None
    time = None
    type = None
    date = None
    status = ''
    link_id = None
    recording_file = None
    events_path_from_gui = None
    recording_path_from_gui = None
    is_recording = False

    def file_path_from_gui_name(self):
        return Path(self.events_path_from_gui).name

    def to_json(self):
        clip_data_json = {}
        clip_data_json.update(
            {TIME: self.time, TYPE: self.type, DATE: self.date, STATUS: self.status, LINK_ID: self.link_id,
             FILE: self.recording_file})
        return clip_data_json


def get_processing_new_filename(found_newest_file):
    # windows doesn't recognize the newest file until the obs thread
    # finishes.  Implement thread to hopefully not need this
    file_counter_pattern = "\(.*\)"

    def increment_file_counter(file_to_increment):
        match = re.compile(file_counter_pattern).search(file_to_increment)
        if match:
            old_paren = match[0]
            temp_file_num = old_paren.replace('(', '').replace(')', '')
            new_index = int(temp_file_num) + 1
            file_to_increment = file_to_increment.replace(old_paren, str(f'({new_index})'))
        print('Incremented file ', file_to_increment)
        return file_to_increment

    capture_paren = "(.\(..*\))"
    date_pattern = "[0-9]*-[0-9]*-[0-9]*"

    match_date = re.findall(date_pattern, found_newest_file)
    match_paren = re.findall(file_counter_pattern, found_newest_file)
    match_to_remove = re.findall(capture_paren, found_newest_file)
    dte_str = ''
    dte_format = '%m-%d-%y'

    if match_date:
        dte_str = match_date[0]
        dte_match = datetime.datetime.strptime(dte_str, dte_format).strftime(dte_format)
        dte_today = datetime.datetime.now().strftime(dte_format)
        if dte_match != dte_today:
            found_newest_file = found_newest_file.replace(dte_str, str(f'{dte_today}'))
            if len(match_to_remove) == 1:  # remove parenthesis if first recording for today and last days has (2)
                found_newest_file = found_newest_file.replace(match_to_remove.pop(), '')  # remove " (3)" from file name
        if dte_match == dte_today:  # found a file with todays date should add the "( )"
            # add (2).mkv if file exists
            if not match_paren:
                found_newest_file = found_newest_file.replace(dte_str, str(f'{dte_today} (2)'))
            if match_paren:
                found_newest_file = increment_file_counter(found_newest_file)
        print('Returning new found file ', found_newest_file)
        return found_newest_file


def data_for_file(_e):
    data = None
    if Data.is_recording:
        Data.time = get_time_hh_mm_ss(stopwatch.get_elapsed_time_int_for_file())
        Data.type = _e.txt
        Data.date = datetime.datetime.now().strftime(y_m_d_h_m_s)
        Data.status = ''
        Data.link_id = ''
        Data.recording_file = ''
        data = append_data_to_file_from(Data.to_json(Data))
    elif Data.testing and stable is False:
        Data.time = '00:00:00'
        Data.type = _e.txt
        Data.date = datetime.datetime.now().strftime(y_m_d_h_m_s)
        Data.status = ''
        Data.link_id = ''
        Data.recording_file = ''
        data = append_data_to_file_from(Data.to_json(Data))

    return data


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
        description = "Recording Marker " + str(self._id)
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


def delete_last_row():
    with open(Data.events_path_from_gui, 'r') as input_file:
        # Create a CSV reader
        reader = csv.DictReader(input_file)

        # Read all the rows of the input file into a list
        rows = list(reader)
        start = len(rows)

        removed_row = rows[:-1]

    # Open the input CSV file in write mode
    with open(Data.events_path_from_gui, 'w') as output_file:
        # Create a CSV writer
        writer = csv.DictWriter(output_file, fieldnames=file_headers, lineterminator='\n')

        # Write the header row
        writer.writeheader()

        # Write all the rows (except the last one) to the output file
        end = 0
        for row in removed_row:
            end += 1
            writer.writerow(row)

    if end < start:
        return 'Deleted last row'
    else:
        return 'Could not delete'


def update_last_row(times_str='10:10 mod'):
    # also can subtract '-10:10'
    def get_times(times_as_str):
        times_list = times_as_str.split(':')
        if len(times_list) < 2:
            return None, None
        start = int(times_list[0])
        end = int(times_list[1])
        return start, end

    def to_string(type_left, type_right):
        return f'{type_left}:{type_right}'

    if Data.testing and Data.events_path_from_gui == 'testing.csv':
        start_time, end_time = get_times(times_str)

        start_diff = 10
        end_diff = 200

        start_diff += start_time
        end_diff += end_time

        return to_string(start_diff, end_diff)

    # Open the input CSV file in read mode
    with open(Data.events_path_from_gui, 'r') as input_file:
        # Create a CSV reader
        reader = csv.DictReader(input_file)

        # Read all the rows of the input file into a list
        rows = list(reader)

        # Remove the last row from the list
        last_row = rows[-1]

        start_time, end_time = get_times(times_str)
        if start_time is None or end_time is None:
            return None
        start_diff, end_diff = get_times(last_row[TYPE])

        if start_time != 0:
            start_diff += start_time
        if end_time != 0:
            end_diff += end_time

        new_row_val = to_string(start_diff, end_diff)
        last_row[TYPE] = new_row_val

    # Open the input CSV file in write mode
    with open(Data.events_path_from_gui, 'w') as output_file:
        # Create a CSV writer
        writer = csv.DictWriter(output_file, fieldnames=file_headers, lineterminator='\n')

        # Write the header row
        writer.writeheader()

        # Write all the rows (except the last one) to the output file
        end = 0
        for row in rows:
            end += 1
            writer.writerow(row)
    return last_row


class h:
    htk_copy = None  # this attribute will hold instance of Hotkey


# STEP1 CREATE FUNCTION FOR NEW HOTKEY
def cb1(pressed):
    if pressed:
        print('\nPressed CB1')
        return cb_effects(e1)


def cb2(pressed):
    if pressed:
        print('\nPressed CB2')
        return cb_effects(e2)


def cb3(pressed):
    if pressed:
        print('\nPressed CB3')
        return cb_effects(e3)


def cb4(pressed):
    if pressed:
        print('\nPressed CB4')
        return cb_effects(e4)


def cb5(pressed):
    if pressed:
        print('\nPressed CB5')
        return cb_effects(e5)


def cb6(pressed):
    if pressed:
        print('\nPressed CB6')
        return cb_effects(e6)


def cb7(pressed):
    if pressed:
        print('\nPressed CB7')
        return cb_effects(e7)


def cb8(pressed, e_text_test='ONLY FOR TESTS'):
    if Data.testing:
        text_test(e_text_test)
    if pressed:
        print('\nPressed CB8')
        return cb_effects(e8)


def text_test(e8_text_test):
    if e8_text_test is not None:
        e8.txt = e8_text_test


def cb_effects(_e):
    print('CB Effects ', Data.recording_path_from_gui, Data.events_path_from_gui, Data.testing)
    if _e.txt is None:
        return 'Hotkey has no text ', _e.txt
    if Data.is_recording or Data.testing is True and stable is False:
        print(f"Callback: {_e}" + _e.txt, 'recording: ', stopwatch.get_elapsed_time_str_not_formatted())
        if 'mod' in _e.txt:
            print('Modifying...')
            mod = _e.txt
            s_e_pattern = r"([-][0-9]*:[0-9]*|[0-9]*:[0-9]*)"
            match_s_e_mod = re.findall(':', mod)
            if len(match_s_e_mod) > 1 or len(match_s_e_mod) == 0:
                return 'Invalid mod. Should be "10:00 mod" startSeconds:endSeconds modArg'
            match_s_e_mod = re.search(s_e_pattern, mod)
            if match_s_e_mod:
                # last_row = update_last_row(match_s_e_mod[0])
                x = _e.txt.split(" ")
                for item in _e.txt.split(" "):
                    if ':' in item:
                        x = item
                last_row = update_last_row(x)
                return last_row
            else:
                return 'No match for pattern "10:00 mod" startSeconds:endSeconds modArg when modifying last row'
        elif 'del' in _e.txt:
            print('Deleting...')
            return delete_last_row()
        else:
            print(f'Apending to {Data.events_path_from_gui}...')
            appended_data = data_for_file(_e)
            print(f'Data appended {appended_data}')
            return appended_data
    else:
        return 'Not recording'


class e:
    txt = "Default txt"


# def set_stream_delay_buffer_volume_to_zero():
#   # Get the current live stream
#   stream = S.get_current_service().get_preview_stream()
#
#   # Set the stream delay buffer volume to 0
#   stream.set_delay_buffer_volume(0)
#   print('set the buffer to 0')


def frontend_event_handler(data):
    global is_paused, stopwatch
    global window_start
    global loop_destroy
    # t1 = Thread(most_recent_file, args=(recording_path, '\*'))

    if data == S.OBS_FRONTEND_EVENT_RECORDING_STARTING:
        window_start = True
        is_paused = False
        stopwatch.start()
        file = most_recent_file([Data.recording_path_from_gui])
        Data.time = '00:00:00'
        Data.type = 'SKIP'
        Data.date = datetime.datetime.now().strftime(y_m_d_h_m_s)
        Data.status = ''
        Data.link_id = ''
        Data.recording_file = file
        append_data_to_file_from(Data.to_json(Data))
        print('REC started..')

    if data == S.OBS_FRONTEND_EVENT_RECORDING_STOPPED:
        window_start = False
        is_paused = False
        stopwatch.stop()
        print('REC stops..')

    if data == S.OBS_FRONTEND_EVENT_RECORDING_PAUSED:
        is_paused = True
        stopwatch.get_elapsed_time_str_not_formatted()
        stopwatch.pause()
        print('REC paused..')

    if data == S.OBS_FRONTEND_EVENT_RECORDING_UNPAUSED:
        is_paused = False
        Data.is_recording = True
        stopwatch.start()
        print('REC un-paused..')


# STEP 2 INSTANTIATE THE CLASSES
e1 = e()
e2 = e()
e3 = e()
e4 = e()
e5 = e()
e6 = e()
e7 = e()
e8 = e()

e_testing = e()
e_recording_path = e()
e_events_path = e()
e_remux = e()

# STEP 2.1 INSTANTIATHE THE HOTKEY HOLDER
h1 = h()
h2 = h()
h3 = h()
h4 = h()
h5 = h()
h6 = h()
h7 = h()
h8 = h()


# STEP3 ADD TO SCRIPT PROPERTIES
def script_properties():
    props = S.obs_properties_create()
    hotkey_1 = "Hotkey 1"
    hotkey_2 = "Hotkey 2"
    hotkey_3 = "Hotkey 3"
    hotkey_4 = "Hotkey 4"
    hotkey_5 = "Hotkey 5"
    hotkey_6 = "Hotkey 6"
    hotkey_7 = "Hotkey 7"
    hotkey_8 = "Hotkey 8"

    S.obs_properties_add_text(props, "_text1", hotkey_1, S.OBS_TEXT_DEFAULT)
    S.obs_properties_add_text(props, "_text2", hotkey_2, S.OBS_TEXT_DEFAULT)
    S.obs_properties_add_text(props, "_text3", hotkey_3, S.OBS_TEXT_DEFAULT)
    S.obs_properties_add_text(props, "_text4", hotkey_4, S.OBS_TEXT_DEFAULT)
    S.obs_properties_add_text(props, "_text5", hotkey_5, S.OBS_TEXT_DEFAULT)
    S.obs_properties_add_text(props, "_text6", hotkey_6, S.OBS_TEXT_DEFAULT)
    S.obs_properties_add_text(props, "_text7", hotkey_7, S.OBS_TEXT_DEFAULT)
    S.obs_properties_add_text(props, "_text8", hotkey_8, S.OBS_TEXT_DEFAULT)
    #                                                propt   name      display
    if stable is False: e_testing = S.obs_properties_add_bool(props, "_testing", "Testing Yes/No (Check/Uncheck)")
    e_recording_path = S.obs_properties_add_text(props, "_rec_path", "Recording Path", S.OBS_TEXT_DEFAULT)
    e_events_path = S.obs_properties_add_text(props, "_events_path", "Events Path", S.OBS_TEXT_DEFAULT)
    _remux = S.obs_properties_add_bool(props, "_remux", "Remux Yes/No (Check/Uncheck)")

    return props


# STEP 4 ADD TO SCRIPT UPDATE
def script_update(settings):
    _text1 = S.obs_data_get_string(settings, "_text1")
    _text2 = S.obs_data_get_string(settings, "_text2")
    _text3 = S.obs_data_get_string(settings, "_text3")
    _text4 = S.obs_data_get_string(settings, "_text4")
    _text5 = S.obs_data_get_string(settings, "_text5")
    _text6 = S.obs_data_get_string(settings, "_text6")
    _text7 = S.obs_data_get_string(settings, "_text7")
    _text8 = S.obs_data_get_string(settings, "_text8")

    e1.txt = _text1
    e2.txt = _text2
    e3.txt = _text3
    e4.txt = _text4
    e5.txt = _text5
    e6.txt = _text6
    e7.txt = _text7
    e8.txt = _text8

    _rec_path = S.obs_data_get_string(settings, "_rec_path")
    _events_path = S.obs_data_get_string(settings, "_events_path")

    _remux = S.obs_data_get_bool(settings, "_remux")
    _testing = S.obs_data_get_bool(settings, "_testing")

    e_recording_path.txt = _rec_path
    e_events_path.txt = _events_path
    e_remux.txt = _remux
    e_testing.txt = _testing
    save_config()


# STEP 5 ADD TO SCRIPT LOAD
def script_load(settings):
    Data.recording_path_from_gui = S.obs_data_get_string(settings, "_rec_path")
    Data.events_path_from_gui = S.obs_data_get_string(settings, "_events_path")
    Data.testing = S.obs_data_get_bool(settings, "_testing")
    create_event_file()
    Data.is_recording = False
    h1.htk_copy = Application(cb1, settings, "Htk_1")
    h2.htk_copy = Application(cb2, settings, "Htk_2")
    h3.htk_copy = Application(cb3, settings, "Htk_3")
    h4.htk_copy = Application(cb4, settings, "Htk_4")
    h5.htk_copy = Application(cb5, settings, "Htk_5")
    h6.htk_copy = Application(cb6, settings, "Htk_6")
    h7.htk_copy = Application(cb7, settings, "Htk_7")
    h8.htk_copy = Application(cb8, settings, "Htk_8")
    load_config()
    # S.obs_data_set_string(settings, "_text3", e1.txt)
    if not S.obs_data_get_string(settings, "_text1"):
        S.obs_data_set_string(settings, "_text1", e1.txt)
    if not S.obs_data_get_string(settings, "_text2"):
        S.obs_data_set_string(settings, "_text2", e2.txt)
    if not S.obs_data_get_string(settings, "_text3"):
        S.obs_data_set_string(settings, "_text3", e3.txt)
    if not S.obs_data_get_string(settings, "_text4"):
        S.obs_data_set_string(settings, "_text4", e4.txt)
    if not S.obs_data_get_string(settings, "_text5"):
        S.obs_data_set_string(settings, "_text5", e5.txt)
    if not S.obs_data_get_string(settings, "_text6"):
        S.obs_data_set_string(settings, "_text6", e6.txt)
    if not S.obs_data_get_string(settings, "_text7"):
        S.obs_data_set_string(settings, "_text7", e7.txt)
    if not S.obs_data_get_string(settings, "_text8"):
        S.obs_data_set_string(settings, "_text8", e8.txt)



# STEP 5 ADD TO SCRIPT SAVE
def script_save(settings):
    h1.htk_copy.save_hotkey()
    h2.htk_copy.save_hotkey()
    h3.htk_copy.save_hotkey()
    h4.htk_copy.save_hotkey()
    h5.htk_copy.save_hotkey()
    h6.htk_copy.save_hotkey()
    h7.htk_copy.save_hotkey()
    h8.htk_copy.save_hotkey()


def script_description():
    description = ("OBS RECORDING MARKER will add hotkey events to a file\n"
                   "Which will later be used to automatically clip the VOD\n"
                   "OBS VOD Clipper and Manager coming soon!\n"
                   "\nVOD Clipper: Clips automatically from markers, \n\tcrop cam and stack for vertical videos"
                   "\nManager: Automatically upload videos and organize\n\n"

                   "Go to this link for examples:\n"
                   "https://github.com/dez011/obs_recording_markers/blob/master/README.md\n\n"

                   "Restart OBS after adding the script\n"
                   "You have to select a Python 3.6.X version folder \n\n"
                   "*** OBS Filename Formatting: STREAM %MM-%DD-%YY \n"
                   "*** Copy the OBS Recording Path to the script Recording Path field \n"
                   "*** Script Events path recommendation: \n\tUse/recording/path/SCRIPTS/Events.csv\n\n"

                   "Will  have an instructional video on my YouTube channel!\n"
                   "https://youtube.com/@DEZACTUALDOS\n\n")
    return description


try:
    S.obs_frontend_add_event_callback(frontend_event_handler)
except:
    pass
