import re
from datetime import datetime,timedelta

filename = 'C:\\Users\\40030149\\OneDrive - LTTS\\Desktop\\test.txt'
pause = '[AAMPCLI] Enter cmd: pause'
paused = '[AAMPCLI] AAMP_EVENT_STATE_CHANGED: PAUSED (6)'

play='[AAMPCLI] Enter cmd: play'
playing='AAMP_EVENT_SPEED_CHANGED current rate=1.000000'

seekFW='[AAMPCLI] Enter cmd: seek 120'
seeked='[AAMPCLI] AAMP_EVENT_SEEKED: new positionMs 120000.000000'

seekRW='[AAMPCLI] Enter cmd: seek 30'
seekedRW='[AAMPCLI] AAMP_EVENT_SEEKED: new positionMs 30000.000000'

ScheduledPause='[AAMPCLI] Enter cmd: pause 60'
ScheduledPaused='aamp_PauseAt position=60.000000'

slow='slow'
slowoutput='[AAMPCLI] AAMP_EVENT_SPEED_CHANGED current rate=0.500000'

stop='[AAMPCLI] Enter cmd: stop'
stopoutput='[StopInternal][2855]aamp_stop PlayerState=8'

stream = '[AAMPCLI] Enter cmd: 1002'
streamoutput='[AAMPCLI] AAMP_EVENT_TUNED'

streamfailure = '[AAMPCLI] Enter cmd: 1002'
streamfailureoutput = '[AAMPCLI] AAMP_EVENT_TUNE_FAILED reason=AAMP: fragment download failures : Http Error Code 404'


def ExtractTimeStampspause():   

    timestamps = []

    with open(filename,'r') as file:
        for line in file:
            if pause in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value1=timestamps

    with open(filename,'r') as file:
        for line in file:
            if paused in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value2=timestamps
    print(value2)  

    timestamps = [datetime.strptime(''.join(match), "%H:%M:%S") for match in value1]
    differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]
    results= [diff <= timedelta(seconds=5) for diff in differences]

    print("Extracted timestamps for Pause:")
    for timestamp in timestamps:
        print(timestamp.strftime("%H:%M:%S"))
    print("Time differences:")
    for difference in differences:
        print(str(difference))
    print("result:")
    for result in results:
         print(result)
    return timestamps

def ExtractTimeStampsplay():
    timestamps = []
    with open(filename,'r') as file:
        for line in file:
            if play in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value1=timestamps

    with open(filename,'r') as file:
        for line in file:
            if playing in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value2=timestamps
    print(value2)  

    timestamps = [datetime.strptime(''.join(match), "%H:%M:%S") for match in value1]
    differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]
    results= [diff <= timedelta(seconds=5) for diff in differences]

    print("Extracted timestamps for Play:")
    for timestamp in timestamps:
        print(timestamp.strftime("%H:%M:%S"))
    print("Time differences:")
    for difference in differences:
        print(str(difference))
    print("result:")
    for result in results:
         print(result)
    return timestamps

def ExtractTimeStampsSeekFW():
    timestamps = []
    with open(filename,'r') as file:
        for line in file:
            if seekFW in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value1=timestamps

    with open(filename,'r') as file:
        for line in file:
            if seeked in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value2=timestamps
    print(value2)  

    timestamps = [datetime.strptime(''.join(match), "%H:%M:%S") for match in value1]
    differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]
    results= [diff <= timedelta(seconds=5) for diff in differences]

    print("Extracted timestamps for seekfw:")
    for timestamp in timestamps:
        print(timestamp.strftime("%H:%M:%S"))
    print("Time differences:")
    for difference in differences:
        print(str(difference))
    print("result:")
    for result in results:
         print(result)
    return timestamps

def ExtractTimeStampsSeekRW():
    timestamps = []
    with open(filename,'r') as file:
        for line in file:
            if seekRW in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value1=timestamps

    with open(filename,'r') as file:
        for line in file:
            if seekedRW in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value2=timestamps
    print(value2)  

    timestamps = [datetime.strptime(''.join(match), "%H:%M:%S") for match in value1]
    differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]
    results= [diff <= timedelta(seconds=5) for diff in differences]

    print("Extracted timestamps for seekrw:")
    for timestamp in timestamps:
        print(timestamp.strftime("%H:%M:%S"))
    print("Time differences:")
    for difference in differences:
        print(str(difference))
    print("result:")
    for result in results:
         print(result)
    return timestamps

def ExtractTimeStampsScheduledPause():
    timestamps = []
    with open(filename,'r') as file:
        for line in file:
            if ScheduledPause in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value1=timestamps

    with open(filename,'r') as file:
        for line in file:
            if ScheduledPaused in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value2=timestamps
    print(value2)  

    timestamps = [datetime.strptime(''.join(match), "%H:%M:%S") for match in value1]
    differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]
    results= [diff <= timedelta(seconds=5) for diff in differences]

    print("Extracted timestamps for schedulePause:")
    for timestamp in timestamps:
        print(timestamp.strftime("%H:%M:%S"))
    print("Time differences:")
    for difference in differences:
        print(str(difference))
    print("result:")
    for result in results:
         print(result)
    return timestamps

def ExtractTimeStampsSlow():
    timestamps = []
    with open(filename,'r') as file:
        for line in file:
            if slow in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value1=timestamps

    with open(filename,'r') as file:
        for line in file:
            if slowoutput in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value2=timestamps
    print(value2)  

    timestamps = [datetime.strptime(''.join(match), "%H:%M:%S") for match in value1]
    differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]
    results= [diff <= timedelta(seconds=5) for diff in differences]

    print("Extracted timestamps for slow:")
    for timestamp in timestamps:
        print(timestamp.strftime("%H:%M:%S"))
    print("Time differences:")
    for difference in differences:
        print(str(difference))
    print("result:")
    for result in results:
         print(result)
    return timestamps

def ExtractTimeStampsSTOP():
    timestamps = []
    with open(filename,'r') as file:
        for line in file:
            if stop in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value1=timestamps

    with open(filename,'r') as file:

        for line in file:
            if stopoutput in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value2=timestamps
    print(value2)  

    timestamps = [datetime.strptime(''.join(match), "%H:%M:%S") for match in value1]
    differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]
    results= [diff <= timedelta(seconds=5) for diff in differences]

    print("Extracted timestamps for stop:")
    for timestamp in timestamps:
        print(timestamp.strftime("%H:%M:%S"))
    print("Time differences:")
    for difference in differences:
        print(str(difference))
    print("result:")
    for result in results:
         print(result)
    return timestamps


def streamplayback():
    timestamps = []
    with open(filename,'r') as file:
        for line in file:
            if stream in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value1=timestamps

    with open(filename,'r') as file:

        for line in file:
            if streamoutput in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value2=timestamps
    print(value2)  

    timestamps = [datetime.strptime(''.join(match), "%H:%M:%S") for match in value1]
    differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]
    results= [diff <= timedelta(seconds=15) for diff in differences]

   
    if len(timestamps) >= 2:
        time_diff = timestamps[1] - timestamps[0]
        print("StreamPlayback:",time_diff)
    else:
        print("StreamPlayback:",False)
    for result in results:
         print(result)
    return timestamps
    


def ExtractTimeStampsstreamfailure():
    timestamps = []
    with open(filename,'r') as file:
        for line in file:
            if streamfailure in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value1=timestamps
    with open(filename,'r') as file:
       for line in file:
            if streamfailureoutput in line:
                    timestamp = re.search(r'\d{2}:\d{2}:\d{2}', line)
                    if timestamp:
                       timestamps.append(timestamp.group())
    value2=timestamps
    print(value2)  
    timestamps = [datetime.strptime(''.join(match), "%H:%M:%S") for match in value1]
    differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]

    results= [diff <= timedelta(seconds=20) for diff in differences]
    if len(timestamps) >= 2:
        time_diff = timestamps[1] - timestamps[0]
        print("StreamFailure:",time_diff)
    else:
        print("StreamFailure:",False)
    for result in results:
         print(result)
    return timestamps

