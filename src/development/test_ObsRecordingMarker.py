import csv
import os
import pytest

from src.development.ObsRecordingMarker import append_data_to_file_from


@pytest.fixture
def setup_csv_file(tmpdir):
    # create a temporary CSV file
    file_path = os.path.join(tmpdir, 'test.csv')
    with open(file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['TYPE', 'TIME'])

    yield file_path

    # remove the temporary file
    os.remove(file_path)

def test_append_data_to_file_from(setup_csv_file):
    # define test data
    events_csv = 'O:\\RECORDINGS\\SCRIPTS\\Events.csv'
    json_data = {'TYPE': '00:00', 'TIME': '00:10:00'}
    startingRows = 0
    with open(events_csv) as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
        startingRows = len(rows)

    # append data to the CSV file
    result = append_data_to_file_from(json=json_data, dataPathForTest=events_csv)

    # assert that the data was appended to the file
    assert result == ('Appended to file ', json_data)

    with open(events_csv) as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]

    assert len(rows) == startingRows + 1
    assert rows[-1]['TYPE'] == '00:00'
    assert rows[-1]['TIME'] == '00:10:00'

def test_append_data_5_min_as_secondsto_file_from(setup_csv_file):
    # define test data
    events_csv = 'O:\\RECORDINGS\\SCRIPTS\\Events.csv'
    json_data = {'TYPE': '300:00', 'TIME': '00:10:00'}
    startingRows = 0
    with open(events_csv) as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
        startingRows = len(rows)

    # append data to the CSV file
    result = append_data_to_file_from(json=json_data, dataPathForTest=events_csv)

    # assert that the data was appended to the file
    assert result == ('Appended to file ', json_data)

    with open(events_csv) as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]

    assert len(rows) == startingRows + 1
    assert rows[-1]['TYPE'] == '300:00'
    assert rows[-1]['TIME'] == '00:10:00'
