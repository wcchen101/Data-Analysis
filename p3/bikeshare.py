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
    city, month, day = '', '', ''
    while True:
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city_input = input('\nWhich city would you like to choose? Enter chicago, new york city or washington.\n').lower()
        valid_city = ['chicago', 'new york city', 'washington']
        if city_input in valid_city:
            city = city_input
            print(city)
            break
        else:
            print('invalid input, please enter again')

    while True:
        # TO DO: get user input for month (all, january, february, ... , june)
        month_input = input('\nWhich month would you like to choose? Enter all, january, february,..., june.\n')
        valid_month = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        if month_input in valid_month:
            month = month_input
            print(month)
            break
        else:
            print('invalid input, please enter again')

    while True:
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        week_input = input('\nWhich week would you like to choose? Enter all, monday, tuesday, ... sunday.\n')
        valid_week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if week_input in valid_week:
            day = week_input
            print(day)
            break

        else:
            print('invalid input, please enter again')

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
    try: 
        # filter by city
        df = None
        if (city == 'washington'):
            df = pd.read_csv('washington.csv')
        if (city == 'new york city'):
            df = pd.read_csv('new_york_city.csv')
        if (city == 'chicago'):
            df = pd.read_csv('chicago.csv')

        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour

        df['Start-End Station'] = df['Start Station'] + ':' + df['End Station']
        # filter by month if applicable
        if month != 'all':
            # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
            month = months.index(month) + 1

            # filter by month to create the new dataframe
            df = df[df['month'] == month]

        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day]

        return df

    except Exception:
        print('错误: ', str(Exception)) 


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_week = df['day_of_week'].mode()[0]


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('\npopular month is {}, week is {}, hour is {}\n'.format(popular_month, popular_week, popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df['Start-End Station'].mode()[0]

    print('\npopular start station is {},\n popular end station is {},\n popular start-end station is {}\n'.format(popular_start_station, popular_end_station, popular_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    import datetime

    # TO DO: display total travel time
    time_diff = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    total_travel_time = time_diff.sum()
    print('\ntotal travel time:{}\n'.format(time_diff.sum()))

    # TO DO: display mean travel time
    time_diff_mean = time_diff.mean()
    print('\ntravel time mean: {}\n'.format(time_diff_mean))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df:
        user_type_counts = df['User Type'].dropna(0).value_counts()
        print('\ncounts of user types:{}\n'.format(user_type_counts))
    else:
        print('\n no user type stats in this dataset\n')

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].dropna(0).value_counts()
        print('\ncounts of gender: {}\n'.format(gender_counts))
    else:
        print('\n no gender stats in this dataset\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_most_common_birth_year = int(df['Birth Year'].dropna(0).mode()[0])
        print('\nearliest, most recent, and most common year of birth: {}\n'.format(earliest_most_common_birth_year))

    else:
        print('\n no birth year stats in this dataset\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        try:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        except:
            print('There is an error occur in the process!')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
