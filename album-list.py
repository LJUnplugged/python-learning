available_records = ["Countdown to Ecstasy - Steely Dan",
                     "II - Led Zeppelin",
                     "Reject All American - Bikini Kill",
                     "Are You Experienced - Jimmy Hendrix",
                     "Public Enemy - Fear of a Black Planet",
                     "Orc - Thee Oh Sees",
                     "Drunk - Thundercat",
                     "Hot Rats - Frank Zappa",
                     "Fuzz - Fuzz II",
                     "A Love Supreme - John Coltrane",
                     "Fun House - Iggy and The Stooges"]

# valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
record_choices = []
for i in range(1, len(available_records) + 1):
    record_choices.append(str(i))
print(record_choices)
current_choice = "-"
albums = [] # create an empty list

while current_choice != '0':
    if current_choice in record_choices:
        index = int(current_choice) - 1
        chosen_record = available_records[index]
        if chosen_record in available_records:
            # it's already in, so remove it
            print("Removing {}".format(current_choice))
            available_records.remove(chosen_record)
        else:
            print("Adding {}".format(current_choice))
            available_records.append(chosen_record)
        print("Your list now contains: {}".format(available_records))
    else:
        print("Please add options from the list below:")
        for number, record in enumerate(available_records):
            print("{0}: {1}".format(number + 1, record))

    current_choice = input()

print(available_records)
