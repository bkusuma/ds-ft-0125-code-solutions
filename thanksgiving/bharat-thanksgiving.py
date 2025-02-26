# %%
import datetime as dt

timedelta_until_tgivs = dt.date(2025, 11, 27)-dt.date.today() # calculate the timedelta between November 27, 2025 (Thanksgiving Day) and today
days_until_tgivs = timedelta_until_tgivs.days # call the attribute "days" from the timedelta

print(f"There are {days_until_tgivs} days until Thanksgiving!")


