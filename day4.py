import datetime

EVENT_WAKE_UP = "wakes up"
EVENT_FALL_ASLEEP = "falls asleep"
EVENT_START_SHIFT = "begins shift"


class Event:
    date_time = None
    guard_id = None
    event_type = None


def parse_guard_event(event_string):
    event = Event()
    strings = event_string.split(' ')
    event.date_time = datetime.datetime.strptime(event_string[1:17], '%Y-%m-%d %H:%M')
    if strings[2][0] == 'G':
        event.guard_id = strings[3][1:]
        event.event_type = strings[4] + ' ' + strings[5][:-1]
    else:
        event.event_type = strings[2] + ' ' + strings[3][:-1]
    return event


def get_input():
    return map(parse_guard_event, open("day4.txt"))


events = sorted(get_input(), key=lambda ev: ev.date_time)
id = None
guards = {}
time_of_asleep = 0
time_of_wake_up = 0

for ev in events:
    if ev.event_type == EVENT_START_SHIFT:
        id = ev.guard_id
    if ev.event_type == EVENT_FALL_ASLEEP:
        time_of_asleep = ev.date_time.minute
    if ev.event_type == EVENT_WAKE_UP:
        time_of_wake_up = ev.date_time.minute
        if id in guards:
            guards[id] = (guards[id][0] + (time_of_wake_up - time_of_asleep), guards[id][1])
        else:
            guards[id] = (time_of_wake_up - time_of_asleep, [0 for i in range(0, 59)])
        for minute in range(time_of_asleep, time_of_wake_up):
            guards[id][1][minute] += 1
[print(g) for g in guards]
print(guards)
most_sleeping_guard_id = max(guards, key=lambda g: guards[g][0])
most_sleep_guard = guards[most_sleeping_guard_id]
print("Most sleeping guard id %s. He was sleeping most often at minute: %i" % (
    most_sleeping_guard_id, most_sleep_guard[1].index(max(most_sleep_guard[1]))))

part2_guard = max([(g, max(guards[g][1]), guards[g][1].index(max(guards[g][1]))) for g in guards], key=lambda x: x[1])
print("For all guards guard %s was sleeping most at minute %i" % (part2_guard[0], part2_guard[2]))
