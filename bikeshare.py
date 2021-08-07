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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_names = ['chicago', 'new york city','washington']

    # TO DO: get user input for month (all, january, february, ... , june)
    month_names = ['all','january','february','march','april','may','june']


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_names = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    try:
        city = input ('Which city would you like to explore? chicago, new york city or washington? /n> ').lower()
        while (city not in city_names):
            print('You enter',city,'please try again since it is not in option.')
            city = input('Choose a valid city : chicago, new york city or washington? /n> ').lower()
        print('You select',city,'thank you for correct input.')
    except KeyError:
            print('error occurred')
    try:
        month = input('Which month would you like to explore? all, january, february, march, april, may or june? /n>').lower()
        while (month not in month_names):
            print('You enter',month,'please try again since it is not in option.')
            month = input('Choose a month from january to june or all? /n> ').lower()
        print('You select',month,'thank you for correct input.')
    except KeyError:
            print ('error occurred')
    try:
        day = input ('Which day would to like to explore? all, monday, tuesday, wednesday, thursday, friday, saturday, sunday? /n> ')
        while (day not in day_names):
            print('You enter',day,'please try again since it is not in option.')
            day = input('Choose a day like monday, tuesday, wednesday, thursday, friday, saturday, sunday or all? /n> ').lower()
        print('You select',day,'thank you for correct input.')
    except KeyError:
        print('error occurred')

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
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['year']= df['Start Time'].dt.year
    df['month']= df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1
        df=df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most common month of travel: ', common_month)
    
 



    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week of travel: ',common_day_of_week)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour of travel: ',common_hour)


    new_var = time.time() - start_time
    print("\nThis took %s seconds." %round((new_var),3))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(common_end)


    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    common_combination = df ['combination'].mode()[0]
    print(common_combination)


    new_var = time.time() - start_time
    print("\nThis took %s seconds." % round((new_var),3))
    print('-'*40)

import datetime
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time: %s.'%str(datetime.timedelta(seconds = int(total_travel_time))))


    # TO DO: display mean travel time 
    average_travel_time = df['Trip Duration'].mean()
    print('\nThe average travel time: %s.'%str(datetime.timedelta(seconds = int(average_travel_time))))



    new_var = time.time() - start_time
    print("\nThis took %s seconds." % round((new_var),3))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('Number of users by type:{}/n',count_user_types)

    birth_year=int()

    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print('Count of gender: ', count_gender)
    except KeyError:
        print('No data available for the selected city')
    
    


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        earliest_year = int(earliest_birth_year)
        print('The earliest birth by year: ', earliest_year)
        most_recent_year = df['Birth Year'].max()
        recent_year = int(most_recent_year)
        print('The most recent birth by year: ', recent_year)
        most_common_birth = df['Birth Year'].mode()[0]
        common_birth = int(most_common_birth)
        print('The most common birth by year: ', common_birth)
    except KeyError:
        print('Not available data')


    new_var = time.time() - start_time
    print("\nThis took %s seconds." % round((new_var),3))
    print('-'*40)

def display_data(df):
    """Display raw data on bikeshare.py"""

    print('\nDisplay data...\n')
    a = 0
    b = 6
    view_data = input('\nWould you like to view 6 rows of individual trip data? Enter yes or no \n')
    start_loc = 0
    while True:
        if view_data.lower() == 'no':
            break
        else:
            pd.set_option('display.max_columns',200)
            print(df.iloc[a:b])
            start_loc += 6
            view_display = input('Do you wish to continue?:').lower()
            if view_display.lower() != 'yes':
                 break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
        





if __name__ == "__main__":
	main()
