#convert GMT time to unix time
from datetime import datetime, timezone

# Function to convert GMT time to Unix time
def convert_gmt_to_unix(gmt_time):
    # Parse the GMT time string into a datetime object
    dt = datetime.strptime(gmt_time, '%Y-%m-%d %H:%M:%S')
    # Set the timezone to UTC
    dt = dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp())