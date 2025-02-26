# %%
import datetime as dt
import pytz
time_zone_list = list(pytz.all_timezones)

# %%
test_1 = "03/23/21"
parsed_test_1 = dt.datetime.strptime(test_1, "%m/%d/%y")
print(f"1. The parsed version of custom datetime format {test_1} is {parsed_test_1}")

test_2 = "23/03/2021"
parsed_test_2 = dt.datetime.strptime(test_2, "%d/%m/%Y")
print(f"2. The parsed version of custom datetime format {test_2} is {parsed_test_2}")

test_3 = "March 23rd, 2021 13:01 US/Pacific"
separator = " "
split_test_3 = test_3.split(sep=separator)
for thing in split_test_3:
    if thing in time_zone_list:
        time_zone = pytz.timezone(thing)
        split_test_3.remove(thing)
        test_3 = separator.join(split_test_3)
try:
    parsed_test_3 = dt.datetime.strptime(test_3, "%B %dst, %Y %H:%M").astimezone(time_zone)
except:
    try:
        parsed_test_3 = dt.datetime.strptime(test_3, "%B %dnd, %Y %H:%M").astimezone(time_zone)
    except:
        try:
            parsed_test_3 = dt.datetime.strptime(test_3, "%B %drd, %Y %H:%M").astimezone(time_zone)
        except:
            try:
                parsed_test_3 = dt.datetime.strptime(test_3, "%B %dth, %Y %H:%M").astimezone(time_zone)
            except:
                pass
print(f"3. The parsed version of custom datetime format {test_3} is {parsed_test_3}")

test_4 = "1:01pm 23rd March, 2021 Europe/London"
separator = " "
split_test_4 = test_4.split(sep=separator)
for thing in split_test_4:
    if thing in time_zone_list:
        time_zone = pytz.timezone(thing)
        split_test_4.remove(thing)
        test_4 = separator.join(split_test_4)

for ordinal in ["st", "nd", "rd", "th"]:
    try:
     parsed_test_4 = dt.datetime.strptime(test_4, "%I:%M%p %d{ordinal} %B, %Y").astimezone(time_zone)
    except:
        pass
print(f"4. The parsed version of custom datetime format {test_4} is {parsed_test_4}")

test_5 = "1616482800"
parsed_test_5 = dt.datetime.fromtimestamp(int(test_5))
print(f"5. The parsed version of custom datetime format {test_5} is {parsed_test_5}")

test_6 = "2021-03-23T12:00:53.034-07:00"
parsed_test_6 = dt.datetime.fromisoformat(test_6)
print(f"6. The parsed version of custom datetime format {test_6} is {parsed_test_6}")


# %%



