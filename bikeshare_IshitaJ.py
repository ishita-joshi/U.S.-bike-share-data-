import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities =['chicago', 'new york city', 'washington']
    cond = 0
    while cond != 1:
        city = input ("Which city would you like? ")
        city = city.lower()
        if city in cities:
            cond = 1
        else:
            cond = 0

    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city


def main():
    while True:
         city = get_filters()
#         df = load_data(city, month, day)
#         time_stats(df)
#         station_stats(df)
#         trip_duration_stats(df)
#         user_stats(df)
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
        




    if __name__ == "__main__":
	main()

