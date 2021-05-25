import time
import pandas as pd
import numpy as np

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}

MONTH_DATA = ["all", "january", "feburary", "march", "april", "may", "june"]

DAY_DATA = ["all", "monday", "tuesday", "wednesday", "friday", "saturday", "sunday"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")

    # Ask users to input city (chicago, new york city, or washington)
    city_name = " "
    while city_name.lower() not in CITY_DATA:
        city_name = input(
            "\nWhat is the name of the city you would like to search? Please choose from followings; chicago, new york city, or washington.\n"
        )
        if city_name.lower() in CITY_DATA:
            # when name of city is inputted correctly;
            city = CITY_DATA[city_name.lower()]
        else:
            # Otherwise, continue looping until to get the correct name
            print(
                "Sorry, we are not able to get the name correctly. Please try again inputting either chicago, new york city or washingon.\n"
            )

    # Asking user to input the name of the month to search;
    month_name = " "
    while month_name.lower() not in MONTH_DATA:
        month_name = input(
            "\nPlease specify which name of the month you would like to search. Type either 'all' or select specific month e.g. all, january, february,..., june \n"
        )
        if month_name.lower() in MONTH_DATA:
            # if we get the correct input;
            month = month_name.lower()
        else:
            # Otherwise, continue looking until we get the correct input.
            print(
                "Sorry, we are not able to get the name correctly. Please try again inputting either 'all' or january, february, ..., june.\n"
            )

    # Asking user to input day of the week to search;
    day_name = " "
    while day_name.lower() not in DAY_DATA:
        day_name = input(
            "\nPlease specify which name of the weekday you would like to search. Type either 'all' or select specific weekdayday e.g. monday, tuesday, ..., sunday.\n"
        )
        if day_name.lower() in DAY_DATA:
            day = day_name.lower()
        else:
            print(
                "Sorry, we are not able to get the name correcly. Please try again inputting either 'all' or specify the name of weekdays e.g. monday, tuesday,..., sunday \n"
            )

    print("-" * 40)
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
    # To load data file into a dataframe
    df = pd.read_csv(city)

    # To convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # To extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour

    # To filter by month
    if month != "all":
        # To use the index of the months list to get the corresponding number
        month = MONTH_DATA.index(month)

        # To filer by day of week to create the new dataframe
        df = df.loc[df["month"] == month]

    # To filter by day of week
    if day != "all":
        # To filer by day of week to create the new dataframe
        df = df.loc[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # TO DO: display the most popularc month
    popular_month = df["month"].mode()[0]
    print(
        "The most popular month given selected data is: "
        + MONTH_DATA[popular_month].title()
    )

    # TO DO: display the most popular day of week
    popular_day_of_week = df["day_of_week"].mode()[0]
    print(
        "The most popular day of the week given selected data is: "
        + popular_day_of_week
    )

    # TO DO: display the most common start hour
    popular_start_hour = df["hour"].mode()[0]
    print(
        "The most popular start hour given selected data is: " + str(popular_start_hour)
    )

    print("\nThis took %.1f seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print(
        "The most popular start station from the selected data is: "
        + popular_start_station
    )

    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]
    print(
        "The most popular end station from the selected data is: " + popular_end_station
    )

    # TO DO: display most popular pair of start- and end-stations
    popular_combination = (df["Start Station"] + "||" + df["End Station"]).mode()[0]
    print(
        "The most popular combination of start- and end-stations is : "
        + str(popular_combination.split("||"))
    )

    print("\nThis took %.1f seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print(
        "The total travel time given the selected city, the month, and the day is: "
        + str(total_travel_time)
    )

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print(
        "The mean travel time given the selected city, the month, and the day is: "
        + str(mean_travel_time)
    )

    print("\nThis took %.1f seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("The count of user type from the selected data is: " + str(user_types))

    # TO DO: Display counts of gender
    if city == "chicago.csv" or city == "new york city.csv":
        gender = df["Gender"].value_counts()
        print("The count of user gender from the selected data is: \n" + str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df["Birth Year"].min()
        most_recent_birth = df["Birth Year"].max()
        most_common_birth = df["Birth Year"].mode()[0]
        print(
            "The earliest birth year from the selected data is: {:.4g}\n".format(earliest_birth)
        )
        print(
            "The most recent birth year from the selected data is: {:.4g}\n".format(
                most_recent_birth
            )
        )
        print(
            "Most common birth year from the selected data is: {:.4g}\n".format(
                most_common_birth
            )
        )

    print("\nThis took %.1f seconds." % (time.time() - start_time))
    print("-" * 40)


def display_raw_data(df):
    print(df.head())
    next = 0
    while True:
        view_raw_data = input(
            "\nWould you like to look at next five rows of raw data? Please enter yes or no.\n"
        )
        if view_raw_data.lower() != "yes":
            return
        next = next + 5
        print(df.iloc[next : next + 5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input(
                "\nWould you like to look at first five rows of raw data? Please enter yes or no.\n"
            )
            if view_raw_data.lower() != "yes":
                break
            display_raw_data(df)
            break

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
