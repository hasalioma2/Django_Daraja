from datetime import datetime

def get_timestamp():
    formatted_time = datetime.now().strftime("%Y%m%d%H%M%S")

    return formatted_time