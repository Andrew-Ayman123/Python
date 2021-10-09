import time
import pandas as pd
import numpy as np
from pandas import DataFrame

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']


def get_filters() :
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Using a while loop and try except block to handle invalid input
    while True:
        try:
            # Using the lower method make the input all lower case and make it insensitive case
            # Using the strip nethod to handle extra spaces
            city = input(
                'Enter City of your choice (chicago, new york city, washington) : ').lower().strip()
            if city not in CITY_DATA:
                raise ValueError(f'Invalid City Value of {city}')

            month = input(
                'Enter Month of your choice (all, january, february, march, april, may, june) : ').lower().strip()
            if month not in MONTHS and month != 'all':
                raise ValueError(f'Invalid Month Value of {month}')

            day = input(
                'Enter day of your choice (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday) : ').lower().strip()
            if day not in DAYS and day != 'all':
                raise ValueError(f'Invalid Day Value of {day}')

        except ValueError as e:
            # Printing that the user entered an invalid input
            print('-'*40 + f'\n{e}\nPlease Try Again\n' + '-'*40)
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city: str, month: str, day: str) -> DataFrame:
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Reading from the csv based on the city entered using the pandas library function "read_csv(file_name)"
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Making the Month and Day columns from the Start Time column using the apply method and passing lambda function to get the day and month
    df['Month'] = df['Start Time'].apply(lambda x: MONTHS[x.month-1])
    df['Day'] = df['Start Time'].apply(lambda x: DAYS[x.weekday()])

    # to check that the user wanted a filter or not
    if month != 'all':
        df = df[df['Month'] == month]
    if day != 'all':
        df = df[df['Day'] == day]
    return df


def time_stats(df: DataFrame) -> None:
    """
    Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - The table of the filtered data
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Using the mode method to find the most common object within a column and make it index 0 to get a hold of the value
    common_month = df['Month'].mode()[0]
    print(f'The most Common Month : {common_month}')

    common_day = df['Day'].mode()[0]
    print(f'The most Common Day : {common_day}')

    # Using dt.hour to get hold of the data type then the hour attribute because it's a datetime object
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print(f'The most Common hour : {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df: DataFrame) -> None:
    """
    Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - The table of the filtered data
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Using the mode method to find the most common object within a column and make it index 0 to get a hold of the value
    common_start = df['Start Station'].mode()[0]
    print(f'The most Common Start Station : {common_start}')

    common_end = df['End Station'].mode()[0]
    print(f'The most Common End Station : {common_end}')

    # Combineing the 'Start Station' and 'End Station' columns to generate a column finding the most common trip using the mode method
    common_begin_end = (df['Start Station']+df['End Station']).mode()[0]
    print(f'The most Common Trip : {common_begin_end}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df: DataFrame) -> None:
    """
    Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - The table of the filtered data
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Using the sum method to calculate the sum of all Trip Duration Column
    total_time = df['Trip Duration'].sum()
    print(f'Total Travel Time : {total_time}')

    # Using the mean method to calculate the average of all Trip Duration Column
    mean_time = df['Trip Duration'].mean()
    print(f'Average Travel Time : {mean_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df: DataFrame) -> None:
    """
    Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - The table of the filtered data
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Using the value_counts function to count how many users per User Type
    user_count = pd.value_counts(df['User Type'])
    print(f'The User Type counts : \n{user_count}')

    # Using the try except bloc to catch errors when dealing with Washington data because missing columns
    try:
        gender_count = pd.value_counts(df['Gender'])
        print(f'\nThe Gender counts : \n{gender_count}\n')

        # Using the min to find the earlist time cause earlist means smallest
        # Using the max to find the recent time cause recent means biggest
        # Using the mode to find the common time cause common means the most repeated value
        earliest_time = int(df['Birth Year'].min())
        recent_time = int(df['Birth Year'].max())
        common_time = int(df['Birth Year'].mode()[0])
        print(f'Earliest Birth Year : {earliest_time}')
        print(f'Most Recent Birth Year : {recent_time}')
        print(f'Most Common Birth Year : {common_time}')
    except:
        # Do nothing if there were any missing columns
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def prompt_user(df: DataFrame) -> None:
    """
    Displays raw data 5 rows at a time based on user input.
    Args:
        (DataFrame) df - The table of the filtered data
    """

    # initialize the row variable to zero to start at row 0
    row = 0
    while True:
        # to prompt the user if he wants to print raw data 5 rows each time
        prompt_choice = input(
            'Would you like to see raw data ? 5 rows at a time\n"Yes" or "No" : ').lower().strip()
        if prompt_choice == 'yes':
            print(f'Showing data from rows {row}:{row+4}...\n')

            # Checking if the row variable will exceed the end of the list or not
            if row+5 <= len(df):
                # using slicing to select the 5 rows begining at the rows variable and ending 5 rows later
                print(df[row:row+5])
                row += 5
            else:
                print(df[row:])
                print('-'*40)
                break
        else:
            print('-'*40)
            break


def main() -> None:
    # Using a while loop to always repeat unless a break
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        prompt_user(df)

        # to check if the user want to exit or restart
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('GoodBye 👋👋')
            break


# To make the program run if only it was the main like (python bikeshare.py)
if __name__ == "__main__":
    main()
