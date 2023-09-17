import os
import json
import logging

class JsonLogHandler(logging.Handler):
    def __init__(self, filename, *args, **kwargs):
        super(JsonLogHandler, self).__init__(*args, **kwargs)
        self.filename = filename

        # Initialize the log file with an empty JSON list []
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                file.write('[]')

    def emit(self, record):
        try:
            msg = self.format(record)
            log_data = {
                'level': record.levelname,
                'timestamp': record.created,
                'message': msg,
                'logger_name': record.name,
            }
            log_json = json.dumps(log_data)

            # Read the existing JSON list from the log file
            with open(self.filename, 'r') as file:
                log_entries = json.load(file)

            # Append the new log entry to the list
            log_entries.append(log_json)

            # Write back the updated list to the log file
            with open(self.filename, 'w') as file:
                json.dump(log_entries, file)

        except Exception as e:
            print(f"Error in emitting log record: {str(e)}")
