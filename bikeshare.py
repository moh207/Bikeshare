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
    
    try:
      city = str(input('Please type name of city out of (chicago, new york city, washington)\n').lower())
      while( city not in list(CITY_DATA.keys())):  
        city = str(input('Please enter one of cities provided\n').lower())
        
    except:
      print('Invalid input entry')
    

    # TO DO: get user input for month (all, january, february, ... , june)
    try:
        month = str(input('Please type name of month from (january to june) or type all\n').lower())
        while( month not in ['january', 'february', 'march', 'april', 'may', 'june','all']):
          month = str(input('Please enter one of months provided\n').lower())
          
    except:
     print('Invalid input entry')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    try:
        day = str(input('Please type name of the day or type all\n').lower())  
        while( day not in ['sunday', 'monday', 'friday', 'saturday', 'tuesday', 'wednesday','thursday','all']):
          day = str(input('Please enter valid day name\n').lower()) 
        
    except:
      print('Invalid input entry')

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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    try:
      df = pd.read_csv(CITY_DATA[city])
    except:
      print('Wrong city')
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name.str.lower()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        try:
          df = df.loc[df['month']==month]
        except:
          print('month not found')
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        try:
          df = df.loc[df['day_of_week']==day]
        except:
          print('day not found')
    
    return df


def time_stats(df):
    #Displays statistics on the most frequent times of travel.
    #df = pd.read_csv(CITY_DATA[city.lower()])
    print('\nCalculating The Most Frequent Times of Travel for chosen city, month and day .. \n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month: " + str(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("Most common day: " + str(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("Most common start hour: " + str(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    #Displays statistics on the most popular stations and trip.
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most common start station: " + str(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("Most common end station: " + str(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print("Most common start and end station: " + str((df['Start Station']+df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    #Displays statistics on the total and average trip duration.

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time in seconds: " + str(df['Trip Duration'].sum())) 

    # TO DO: display mean travel time
    print("Mean travel time in seconds: " + str(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df,city):
    #Displays statistics on bikeshare users.py

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().sort_values(ascending=False))
    if city in ['chicago','new york city']:
    # TO DO: Display counts of gender
      print(df['Gender'].value_counts().sort_values(ascending=False))

    # TO DO: Display earliest, most recent, and most common year of birth
    
      print("most recent birth year: " + str(df['Birth Year'].max()))
      print("most early birth year: " + str(df['Birth Year'].min()))
      print("most common birth year: " + str(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
  
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data == 'yes'):
      if len(df.index) - start_loc >= 5:  
        print(df.iloc[start_loc: start_loc + 5 ])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
      else:
        print(df.iloc[start_loc : start_loc + (len(df.index) - start_loc) ])
        print('Data finished\n')
        break

def main():
    while True:
        
        try:
          print(pd.__version__)
          city, month, day = get_filters()
          df = load_data(city, month, day)
          print(df)
        except:
          print('Failed')
        

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
