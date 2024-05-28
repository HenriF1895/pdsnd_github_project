import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': pd.read_csv('/Users/henri/Library/Mobile Documents/com~apple~CloudDocs/Programmieren/Nanodegree Python/Daten/all-project-files/chicago.csv'),
              'new york city': pd.read_csv('/Users/henri/Library/Mobile Documents/com~apple~CloudDocs/Programmieren/Nanodegree Python/Daten/all-project-files/new_york_city.csv'),
              'washington': pd.read_csv('/Users/henri/Library/Mobile Documents/com~apple~CloudDocs/Programmieren/Nanodegree Python/Daten/all-project-files/washington.csv')}




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
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Which city do you want to analyze? Choose between Chicago, New York City, Washington. Enter the name of the city: ").lower()
        if city not in cities:
            print("Invalid input! Please enter a valid city name.")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Which month do you want to analyze? Choose between January, February, March, April or May. You can also analyze the data for all time periods. To do that just enter 'all'. Enter the month or all: ").lower()
        if month not in months:
            print("Invalid input! Please enter a valid month.")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Which day of the week do you want to analyze? You can also analyze the data for all days of the week. To do that just enter 'all'. Enter the day or all: ").lower()
        if day not in days:
            print("Invalid input! Please enter a valid day of the week.")
        else:
            break

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
    df = pd.DataFrame(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

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
    
    # ask user if user wants to display the first 5 rows of the loaded data
    while True:
        display_data = input("Do you want to display the first 5 rows of the loaded data? Enter yes or no: ")
        if display_data.lower() in ['yes', 'no']:
            break
        else:
            print("Invalid Input! Please enter either 'yes' or 'no'!")
    if display_data.lower() == 'yes':
        display_data = True
        print("The first 5 rows of the loaded data: \n", df.head())
        
    # ask user if user wants to display the next 5 rows until user says no
    i = 5
    total_rows = len(df)
    while display_data == True:
        more_rows = input("Do you want to display the next 5 rows of the loaded data? Enter yes or no: ")
        if more_rows.lower() in ['yes', 'no']:
            if more_rows.lower() == 'yes' and i < total_rows:
                print("The next 5 rows of the loaded data: \n", df[i:i + 5])
                i += 5
            else:
                break
        else:
            print("Invalid input! Please enter either 'yes' or 'no'")
    
    if display_data == True:
        print('-'*40)
    
    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month: ", popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of the week: ", popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End_Combination'] = df['Start Station'] + ' to ' + df['End Station']
    popular_start_end_station = df['Start_End_Combination'].mode()[0]
    print("The most frequent combination of start station and end station: ", popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # TO DO: display total travel time
    total_travel_time = (df['End Time'] - df['Start Time']).sum().total_seconds()

    # convert total_seconds to days, hours, minutes, and seconds
    days, remainder = divmod(total_travel_time, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    print("The total travel time: {} days {} hours {} minutes {} seconds".format(int(days), int(hours), int(minutes), int(seconds)))

    # TO DO: display mean travel time
    mean_travel_time = (df['End Time']- df['Start Time']).mean().total_seconds()

    # convert total_seconds to days, hours, minutes, and seconds
    mean_days, remainder = divmod(mean_travel_time, 86400)
    mean_hours, remainder = divmod(remainder, 3600)
    mean_minutes, mean_seconds = divmod(remainder, 60)

    print("The average travel time: {} days {} hours {} minutes {} seconds".format(int(mean_days), int(mean_hours), int(mean_minutes), int(mean_seconds)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print("The count of user types: \n", user_types)
    except:
        print("The dataset does not contain the column 'User Type'")

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print("The count of genders: \n", gender_counts)
    except:
        print("The dataset does not contain the column 'Gender'")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earlist_birth = int(df['Birth Year'].min())
        print("The earlist year of birth: ", earlist_birth)
        recent_birth = int(df['Birth Year'].max())
        print("The most recent year of birth: ", recent_birth)
        common_birth = int(df['Birth Year'].mode()[0])
        print("The most common year of birth: ", common_birth)
    except:
        print("The dataset does not contain the column 'Birth Year'")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() in ['yes', 'no']:
                break
            else:
                print("Invalid input! Please enter either 'yes' or 'no'!")
        if restart.lower() == 'no':
            break




if __name__ == "__main__":
	main()