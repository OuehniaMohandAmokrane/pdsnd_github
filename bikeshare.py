import time
import pandas as pd
import numpy as np
"""
Our code is intended to provide the following information:

		# 1 Popular times of travel (i.e., occurs most often in the start time)

		most common month
		most common day of week
		most common hour of day
		# 2 Popular stations and trip

		most common start station
		most common end station
		most common trip from start to end (i.e., most frequent combination of start station and end station)
		# 3 Trip duration

		total travel time
		average travel time
		# 4 User info

		counts of each user type
		counts of each gender (only available for NYC and Chicago)
		earliest, most recent, most common year of birth (only available for NYC and Chicago)

"""
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
    print()
    print('------------------------------SELCTING THE CITY---------------------------------------------')
    print()
    city = input('Look for the data of Chicago, New York, or Washington?').lower()

    while  city not in ['chicago', 'new york city', 'washington']:
        city = input('{} data doesn\'t exist,please select from this [chicago, new york city, washington]'.format(city)).lower()

    print()
    print('The {} city has been selected successfully'.format(city))
    print()
    print('------------------------------SELCTING THE MONTH--------------------------------------------')
    print()
    month = input('For {} city, please chose whether to look at : \n All months data by taping -all \n Or chose from the this list [january, february, march, april, may, june]. \n'.format(city)).lower()
    while  month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('{} doesn\'t exist, please select from this [january, february, march, april, may, june] \n\n'.format(month)).lower()
    print()
    print('You have selected to look for {} data'.format(month))
    print()
    print('------------------------------SELCTING THE DAY----------------------------------------------')
    print()
    day = input('For {} city and the {} month(s), please chose whether to look at : \n All days data by taping -all \n Or chose from the this list [saturday, sunday, monday, thuesday, wednesday, thursday, friday]. \n'.format(city,month)).lower()
    while  day not in ['all', 'saturday', 'sunday', 'monday', 'thuesday', 'wednesday', 'thursday', 'friday']:
        day = input('{} doesn\'t exist,we believe that you\'ve made a clerical error please select :\n Either all \n Or chose from the this list [saturday, sunday, monday, thuesday, wednesday, thursday, friday] \n\n'.format(day)).lower()
    print()
    print('You have selected to look for {} data'.format(day))
    print()
    return city, month, day

def progress_animation():
    print()
    for i in range(0, 105,5):
        print("{} % ".format(i), end='')
        time.sleep(0.15)
    print()
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
        # load data file into a dataframe
    print('------------------------------LOADING THE DATA----------------------------------------------')
    progress_animation()

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print()
    print('------------------------------MOST FREQUENT TRAVEL TIME-------------------------------------')
    print()
    start_time = time.time()
    month_list = ['January', 'February', 'March', 'April', 'May', 'June']
    # TO DO: display the most common month
    print('The most common month is {}.'.format(month_list[df['month'].mode()[0]-1]))


    # TO DO: display the most common day of week
    print('The most common day is {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common hour is {} H'.format(df['hour'].mode()[0]))


    print("\nThis took %.3f seconds." % (time.time() - start_time))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print()
    print('------------------------------MOST POPULAR STATIONS-----------------------------------------')
    print()
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common comonly start station is \n{}\n'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common comonly end station is \n{}\n'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('The most common comonly combination of start station and end station trip is \n{}'.format((df['Start Station'] + ' ' + df['End Station']).mode()[0]))

    print("\nThis took %.3f seconds." % (time.time() - start_time))


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print()
    print('-----------------------------------TRIP DURATION--------------------------------------------')
    print()
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time  is equal to {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('mean travel time  is equal to %.2f' % (df['Trip Duration'].mean()))

    print("\nThis took %.3f seconds." % (time.time() - start_time))


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print()
    print('---------------------------------USERS STATISTICS-------------------------------------------')
    print()
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types  is:\n{}\n'.format(df['User Type'].value_counts().to_frame()))

    # TO DO: Display counts of gender
    try:
        print('counts of user types  is:\n {}\n'.format(df['Gender'].value_counts().to_frame()))
    except KeyError:
        print("For washington data we can not find the gender column")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The earliest year of birth {}\n'.format(int(df['Birth Year'].min())))
        print('The most recent year of birth {}\n'.format(int(df['Birth Year'].max())))
        print('The most common year of birth {}\n'.format(int(df['Birth Year'].mode()[0])))
    except KeyError:
        print("For washington data we can not find the Birth Year column")

    print("\nThis took %.3f seconds." % (time.time() - start_time))


def main():
    display = input('Would you Like to see raw data or apply filters :\n Tape 1 to look for raw data.\n Tape 2 to apply filters\n')
    while display not in ['1','2']:
        display = input('Would you Like to see raw data or apply filters :\n Tape 1 to look for raw data.\n Tape 2 to apply filters.\n')

    if display == '1':
        city = input('Would you like to see data for Chicago, New York, or Washington?').lower()
        print()
        while  city not in ['chicago', 'new york city', 'washington']:
            city = input('{} data doesn\'t exist,we believe that you\'ve made a clerical error please select :\n Either chicago \n Or new york city \n Or washington \n\n'.format(city)).lower()
        print()
        df = pd.read_csv(CITY_DATA[city])
        i = 0
        while (i <= df.shape[0]-5) and (display == '1'):
            print(df.iloc[i:i+5])
            i += 5
            restart = input('\nWould you like to see more data? Enter yes or no.\n')
            if restart.lower() != 'yes':
                display = input('Would you Like to apply the filter for the data:\n Tape 2 to see the data with filters.\n Tape other key to end the program.\n')
                if display == '2':
                    while True:
                        city, month, day = get_filters()
                        df = load_data(city, month, day)

                        time_stats(df)
                        station_stats(df)
                        trip_duration_stats(df)
                        user_stats(df)

                        restart = input('\nWould you like to restart? Enter yes or no.\n')
                        if restart.lower() != 'yes':
                            break
    elif display == '2':
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()
