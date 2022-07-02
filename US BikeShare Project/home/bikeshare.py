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
    
    cities=('chicago','new york city', 'washington','all')
    
    city=input('which city would you like to explore? chicago, new york city, washington or all?').lower()
    
    while city not in cities:
        print('Sorry invalid entry, try again')
        city=input('which city would you like to explore? chicago, new york city, washington or all?').lower()
                 
    # TO DO: get user input for month (all, january, february, ... , june)
    months=('january', 'february', 'march', 'april', 'may', 'june','all')
    
    month=input('which month would you like to explore? january, february, march, april, may,june or all?').lower()
    
    while month not in months:
            print('Sorry invalid entry, try again')
            month=input('which month would you like to explore? january, february, march, april, may,june or all?').lower()
                
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days=('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' ,'all')
    
    day=input('which day would you like to explore? monday, tuesday, wednesday, thursday,friday, saturday, sunday or all?').lower()
    
    while day not in days:
            print('Sorry invalid entry, try again')
            day=input('which day would you like to explore? monday, tuesday, wednesday, thursday,friday, saturday, sunday or all?').lower()
             
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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time']) 

    # extract month and day of week from Start Time to create new columns
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]    
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
             
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    df['day'] =pd.DatetimeIndex(df['Start Time']).day_name()
    popular_day = df['day'].mode()[0]
    print('Most Common Day:', popular_day)

    # TO DO: display the most common start hour

    df['Start Time'] =pd.to_datetime(df['Start Time'])
    df['hour'] =pd.DatetimeIndex(df['Start Time']).hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].mode()
    print('most common start station:',start_station)
    
    # TO DO: display most commonly used end station
    end_station=df['End Station'].mode()
    print('most common end station:',end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['combination_station']=df['Start Station'] +'And'+ df['End Station']
    most_common_trip=df['combination_station'].mode()[0]
    print('most common combination stations:',most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time =',(total_travel_time/3600),'hours' )
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time =',(mean_travel_time/60),'minutes' )
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print('User Types:\n',user_type)

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender_type=df['Gender'].value_counts()
        print('Genders:\n',gender_type)
    else:
        print("The Genders column does not exist")
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_birth=df['Birth Year'].min()
        recent_birth=df['Birth Year'].max()
        most_common_birth=df['Birth Year'].mode()
        print('Earliest Birth Year = ',int(earliest_birth))
        print('Most Recent Birth Year = ',int(recent_birth))
        print('Most Common Birth Year = ',int(most_common_birth))
    else:
        print("The birth year column does not exist")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_stats(df):
    res=input('would you like to display raw data?(yes/no)').lower()
    
    while res=='yes':
        print(df.sample(5))
        
        res=input('would you like to display raw data?(yes/no)').lower()
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_stats(df)
        
  

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
