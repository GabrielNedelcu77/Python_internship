import re
from datetime import datetime

def extract_lines_between_timestamps(file_path, start_timestamp, end_timestamp):
    list_words = []
    with open(file_path, 'r') as file:
        for line in file:
            timestamp_match = re.search(r'(\d{2}:\d{2}:\d{2}\.\d{3})', line)
            if timestamp_match:
                timestamp = timestamp_match.group(1)
                time = datetime.strptime(timestamp,"%H:%M:%S.%f")
                start_time = datetime.strptime(start_timestamp,"%H:%M:%S.%f")
                end_time = datetime.strptime(end_timestamp, "%H:%M:%S.%f")

                if start_time<= time <= end_time:
                    words = line.split()
                    list_words.append(words[-1])
    return list_words



if __name__ == "__main__":
    file_path = 'logcat_applications.txt'
    start_timestamp = '17:56:07.996'
    end_timestamp = '17:56:08.357'

    extracted_lines = extract_lines_between_timestamps(file_path, start_timestamp, end_timestamp)
    print(extracted_lines)
    print(len(extracted_lines))
