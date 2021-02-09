import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input(
            'Please choose a city to get the data from (Chicago, New york city, Washington): ').lower().strip()
        cities = ['chicago', 'new york city', 'washington']
        if city in cities:
            break
        else:
            print('Please enter a valid city')

    while True:
        month = input(
            'Please choose a month for the data (all,january,february,...,june): ').title().strip()
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'Augest', 'September', 'October', 'November', 'December', 'All']
        if month in months:
            break
        else:
            print('Please enter a valid input')

    while True:
        day = input('Please choose a day for the data (all, monday, tuesday, ... sunday): ').title().strip()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']
        if day in days:
            break
        else:
            print('Please enter a valid input')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'], infer_datetime_format=True)
    df['End Time'] = pd.to_datetime(df['End Time'], infer_datetime_format=True)

    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour

    if month != 'All':
        df = df[df['Month'] == month]

    if day != 'All':

        df = df[df['Day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('The most common month of the year is: {}'.format(df['Month'].mode()[0]))

    print('The most common day of the week is: {}'.format(df['Day'].mode()[0]))

    print('The most common starting hour is: {}'.format(df['Hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('The most used start station is: {}'.format(df['Start Station'].mode()[0]))

    print('The most used end station is: {}'.format(df['End Station'].mode()[0]))

    df['Start End'] = 'From' + df['Start Station'] + 'To' + df['End Station']

    print('The most frequent combination of stations is: {}'.format(df['Start End'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_time = df['Trip Duration'].sum()
    print('The total travel time is: {} minutes'.format(total_time))

    print('The average duration for a trip is: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('The counts of user types: {}'.format(df['User Type'].value_counts()))

    try:
        counts_gender = df['Gender'].value_counts()
        early = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print('The counts of genders: {}'.format(counts_gender))
        print('The earliest birth year is: {}'.format(early))
        print('The most recent birth year is: {}'.format(recent))
        print('The most common birth year is: {}'.format(common))

    except:
        print('These values aren\' available for the city you chose')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df, start, end, hop):
    answer = input('Would you like to see 5 rows of raw data ? (yes, no): ')
    answers = ['yes', 'no']
    while answer not in answer:
        answer = input('please enter a valid input (yes, no): ')

    while answer.lower().strip() == 'yes':

        print(df.iloc[start: end])
        start = start + hop
        end = end + hop
        answer = input('Would you like to see 5 more rows ? (yes, no): ').lower().strip()
        while answer not in answer:
            answer = inpiut('please enter a valid input (yes, no): ')


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df, 0, 5, 5)

        print('\n\n LET THE CALCULATION START !!!!!!\n\n')

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
