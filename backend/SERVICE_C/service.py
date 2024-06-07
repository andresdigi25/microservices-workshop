from datetime import date


def process_output(input):
    for i, (key, value) in enumerate(input.items(), start=1):
        value['id'] = i
        value['date'] = str(date.today())
    return input