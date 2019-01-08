import time
from datetime import datetime
import platform
from os import path, system
import csv
from collections import Counter
from operator import itemgetter

'''
This section defines the statistical computation for the data
'''

def popular_month(ordered_data):
    """
    Question: What is the most and least popular month for start time?
    Args:
        ordered_data: Takes in a ordered data of list of dictionaries/wrangled data.
    Returns:
       (tuple) the most popular and least popular month for the city
    """
    list_of_month = []

    for i in range(0, len(ordered_data)):
        temp_var = ordered_data[i]['Month']
        list_of_month.append(temp_var)

    #unique_set

    count_of_trips = dict(Counter(list_of_month))

    max_key = max(count_of_trips, key=lambda k: count_of_trips[k])
    max_value = count_of_trips[max_key]

    min_key = min(count_of_trips, key=lambda k: count_of_trips[k])
    min_value = count_of_trips[min_key]

    return (max_key, max_value, min_key, min_value)

def popular_day(ordered_data):
    """
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    Args:
        ordered_data: Takes in a ordered data of list of dictionaries/wrangled data.
    Returns:
       (tuple) the most popular and least popular day for the city

    """
    list_of_days = []

    for i in range(0, len(ordered_data)):
        temp_var = ordered_data[i]['Day_of_Week']
        list_of_days.append(temp_var)

    count_of_trips = dict(Counter(list_of_days))

    max_key = max(count_of_trips, key=lambda k: count_of_trips[k])
    max_value = count_of_trips[max_key]

    min_key = min(count_of_trips, key=lambda k: count_of_trips[k])
    min_value = count_of_trips[min_key]

    return (max_key, max_value, min_key, min_value)

def popular_hour(ordered_data):
    """
    Question: What is the most popular hour of day for start time?
    Args:
        ordered_data: Takes in a ordered data of list of dictionaries/wrangled data.
    Returns:
       (tuple) the most popular and least popular hour for the city

    """
    list_of_hours = []
    for i in range(0, len(ordered_data)):
        temp_var = ordered_data[i]['Hour_of_Day']
        list_of_hours.append(temp_var)

    count_of_trips = dict(Counter(list_of_hours))

    max_key = max(count_of_trips, key=lambda k: count_of_trips[k])
    max_value = count_of_trips[max_key]

    min_key = min(count_of_trips, key=lambda k: count_of_trips[k])
    min_value = count_of_trips[min_key]

    return (max_key, max_value, min_key, min_value)

def trip_duration(ordered_data):
    """
    Question: What is the total trip duration and average trip duration?
    Args:
        ordered_data: Takes in a ordered data of list of dictionaries/wrangled data.
    Returns:
       (tuple) the total and average trip time for the city

    """
    total_trip_duration = 0

    for i in range(0, len(ordered_data)):
        temp_var = ordered_data[i]['Duration (mins)']
        total_trip_duration += float(temp_var)

    average_trip_duration = float(total_trip_duration/len(ordered_data))
    return (total_trip_duration, average_trip_duration)

def popular_stations(ordered_data):
    """
    Question: What is the most popular start station and most popular end station?
    Args:
        ordered_data: Takes in a ordered data of list of dictionaries/wrangled data.
    Returns:
       (tuple) the most popular start and end station for the city

    """
    list_of_start_stations = []
    list_of_end_stations = []

    for i in range(0, len(ordered_data)):
        temp_var = ordered_data[i]['Start_Station']
        list_of_start_stations.append(temp_var)

    for i in range(0, len(ordered_data)):
        temp_var = ordered_data[i]['End_Station']
        list_of_end_stations.append(temp_var)

    count_of_start_stations = dict(Counter(list_of_start_stations))
    count_of_end_stations = dict(Counter(list_of_end_stations))

    #start station
    s_max_key = max(count_of_start_stations, key=lambda k: count_of_start_stations[k])
    s_max_value = count_of_start_stations[s_max_key]

    #end station
    e_max_key = max(count_of_end_stations, key=lambda k: count_of_end_stations[k])
    e_max_value = count_of_end_stations[e_max_key]

    return (s_max_key, s_max_value, e_max_key, e_max_value)

def popular_trip(ordered_data):
    """
    Question: What is the most popular trip?
    Args:
        ordered_data: Takes in a ordered data of list of dictionaries/wrangled data.
    Returns:
       (tuple) the most popular trip for the city

    """
    list_of_pop_stat = []

    for i in range(0, len(ordered_data)):
        temp_var_s = ordered_data[i]['Start_Station']
        temp_var_e = ordered_data[i]['End_Station']
        list_of_pop_stat.append((temp_var_s,temp_var_e))

    count_of_pop_trip = dict(Counter(list_of_pop_stat))

    max_key = max(count_of_pop_trip.items(), key=itemgetter(1))[0]

    max_value = count_of_pop_trip[max_key]

    return (max_key, max_value)

def users(ordered_data):
    """
    Question: What are the counts of each user type?
    """
    list_of_users = []

    for i in range(0, len(ordered_data)):
        temp_var = ordered_data[i]['User_Type']
        list_of_users.append(temp_var)

    count_of_users = dict(Counter(list_of_users))

    return count_of_users

def gender(ordered_data):
    """
    Question: What are the counts of gender?
    """
    list_of_gender = []

    for i in range(0, len(ordered_data)):
        temp_var = ordered_data[i]['Gender']
        list_of_gender.append(temp_var)

    count_of_gender = dict(Counter(list_of_gender))
    
    unknow = int(count_of_gender['N/A'])
    
    del count_of_gender['N/A']
    
    if (not count_of_gender):
        
        return "N/A"
    
    else:
        
        return (count_of_gender, unknow)

def birth_years(ordered_data):
    """
    Question: What are the earliest, most recent, and most popular birth years?
    """
    list_of_birth_years = []

    for i in range(0, len(ordered_data)):
        temp_var = ordered_data[i]['Year_of_Birth']
        list_of_birth_years.append(temp_var)

    count_of_birth_years = dict(Counter(list_of_birth_years))
    
    del count_of_birth_years['N/A']
    
    if (not count_of_birth_years):
        
        return "N/A"
    
    else:
        
        new_list_br_yr = sorted(count_of_birth_years.items())
        
        earliest = new_list_br_yr[0][0], new_list_br_yr[0][1]
        
        recent = new_list_br_yr[-1][0], new_list_br_yr[-1][1]
        
        max_key = max(count_of_birth_years.items(), key=itemgetter(1))[0]
        
        max_value = count_of_birth_years[max_key]
        
        return (earliest, recent, (max_key, max_value))

def display_statistics(stats_data_computation, period):
    """
    Display the statistics to the user
    Args:
        stat_data_computation: holds the ordered data
    Returns:
        None
    """
    months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    
    print("\nA total number of {} trip have been recorded for the city!".format(len(stats_data_computation)))
    
    if (period == "none"):
        
        st1 = popular_month(stats_data_computation)
        print("\nQ. What is the most and least popular month?")
        print("\nA. \tThe most popular month is '{}' with total number of trips: '{}'".format(months_list[int(st1[0])-1],st1[1]))
        print("\n\tThe least popular month is '{}' with total number of trips: '{}'".format(months_list[int(st1[2])-1],st1[3]))
        time.sleep(5)
        
    st2 = popular_day(stats_data_computation)
    st3 = popular_hour(stats_data_computation)
    st4 = trip_duration(stats_data_computation)
    st5 = popular_trip(stats_data_computation)
    st6 = popular_stations(stats_data_computation)
    st7 = users(stats_data_computation)
    st8 = gender(stats_data_computation)
    st9 = birth_years(stats_data_computation)  
    
    print("\nQ. What is the most popular day of week (Monday, Tuesday, etc.)?")
    print("\nA. \tThe most popular day is '{}' with total number of trips: '{}'".format(st2[0],st2[1]))
    print("\n\tThe least popular day is '{}' with total number of trips: '{}'".format(st2[2],st2[3]))

    time.sleep(5)

    print("\nQ. What is the most popular hour of day?")
    print("\nA. \tThe most popular hour is '{}:00' (hrs) with total number of trips: '{}'".format(st3[0],st3[1]))
    print("\n\tThe least popular month is '{}:00' (hrs) with total number of trips: '{}'".format(st3[2],st3[3]))

    time.sleep(5)

    print("\nQ. What is the total trip duration and average trip duration")
    print("\nA. \tThe total trip duration is %.2f (hrs)" % float(st4[0]/60))
    print("\n\tThe average trip duration is %.2f (mins)" %st4[1])

    time.sleep(5)

    print("\nQ. What is the most popular trip?")
    print("\nA. \tThe most popular trip is:")
    print("\n\t>>> From: '{}'".format(st5[0][0]))
    print("\n\t>>> To: '{}'".format(st5[0][1]))
    print("\n\t>>> With total number of trips '{}'".format(st5[1]))

    time.sleep(5)

    print("\nQ. What is the most popular start station and most popular end station?")
    print("\nA. \tThe most popular stations are:")
    print("\n\t>>> Start Station: '{}', Trips: '{}'".format(st6[0], st6[1]))
    print("\n\t>>> End Station: '{}', Trips: '{}'".format(st6[2], st6[3]))

    time.sleep(5)

    print("\nQ. What are the counts of each user type?")
    print("\nA. \tThe counts of each user type are:")
    print("\n\t1. Customers: '{}'".format(st7['Customer']))
    print("\n\t2. Subscribers: '{}'".format(st7['Subscriber']))

    time.sleep(5)

    print("\nQ. What are the counts of gender?")
    if (type(st8) == str):
        print("\nA. \tThis city does not record the gender of its users!")
    else:
        print("\nA. \tThe counts of gender type are:")
        print("\n\t\t1. Male: '{}'".format(st8[0]['Male']))
        print("\n\t\t2. Female: '{}'".format(st8[0]['Female']))
        print("\n\t\t3. Unknown/Un-Registered: '{}'".format(st8[1]))

    time.sleep(5)

    print("\nQ. What are the earliest, most recent, and most popular birth years?")
    if (type(st9) == str):
        print("\nA. \tThis city does not record the birth year(s) of its users!")
    else:
        print("\nA. \tThe earliest, most recent, and most popular birth years are:")
        print("\n\t\t1. Earliest: '{}'".format(st9[0][0]))
        print("\n\t\t2. Most Recent: '{}'".format(st9[1][0]))
        print("\n\t\t3. Popular Birth Year: '{}', with count: '{}'".format(st9[2][0], st9[2][1]))

def display_data(sorted_data):
    """
    Displays entries from the data 5 at a time
    Args:
        sorted_data: holds the filtered data
    Returns:
        None
    """
    temp_list = []
    
    header_list = "| Duration (mins) | Month | Day of Month | Day of Week | Hour of Day | Start Station                                            | End Station                                              | User Type   | Gender  | Year of Birth |"
    
    initial  = 0
    final = 10
    
    #infinite loop until user enters a valid input
    while True:
        try:
            choice = input('\nWould you like to see ten entries at time?\n\n\t1. Yes.\n\t2. No.'
                         '\n\nPlease input valid number: ')

            next_five = int(choice)

        except ValueError:
            print("\nSorry, I\'m are expecting a number! and not {}!".format(choice.title()))
            continue

        if ( next_five <= 0 or next_five > 3 ):
            print("\nSorry, your response must not be negative or greater than 2.")
            continue

        if (next_five == 1):

            #clearing console
            if(platform.system() == "Windows"):
                system('cls')
            else:
                system('clear')

            for i in range(initial, final):

                temp_var = sorted_data[i]
                temp_list.append(temp_var)
            
            print("\n")
            
            print("-"*len(header_list))
                
            print(header_list)
            
            print("-"*len(header_list))
            
            for a,b,c,d,e,f,g,h,i,j in temp_list:
                print("|",a," "*(14-len(str(a))),
                      "|",b," "*(4-len(b)),
                      "|",c," "*(11-len(c)),
                      "|",d," "*(10-len(d)),
                      "|",e," "*(10-len(e)),
                      "|",f," "*(55-len(f)),
                      "|",g," "*(55-len(g)),
                      "|",h," "*(10-len(h)),
                      "|",i," "*(6-len(i)),
                      "|",j," "*(12-len(j)),
                      "|")
            
            print("-"*len(header_list))

            initial = final
            
            final += 10
            
            continue

        else:
            
            break

    #give back control to the caller
    return

'''
This section defines the process for cleaning the data
'''

def duration_in_mins(datum):
    """
    Takes as input a dictionary containing info about a single trip (datum)
    and returns the trip duration in units of minutes.
    """
    time = float(datum.get("Trip Duration"))
    duration = (time/60)

    return duration

def time_of_trip(datum):
    """
    Takes as input a dictionary containing info about a single trip (datum)
    and returns the month, hour, and day of the week in which the trip was made.
    """

    date = datetime.strptime(datum.get("Start Time"), "%Y-%m-%d %H:%M:%S" )

    day_of_month = int(date.strftime('%d'))

    month, hour, day_of_week = int(date.strftime('%m')), int(date.strftime('%H')), str(date.strftime('%A'))

    return (month, hour, day_of_week, day_of_month)

def type_of_user(datum):
    """
    Takes as input a dictionary containing info about a single trip (datum)
    and returns the type of system user that made the trip.
    """

    if(datum.get("User Type") == "Subscriber"):

        user_type = "Subscriber"

    else:

        user_type = "Customer"

    return user_type

def get_stations(datum):
    """
    Takes as input a dictionary containing info about a single trip (datum)
    and returns the start and end stations
    """

    start = datum.get("Start Station")

    end = datum.get("End Station")

    return (start, end)

def genyr(datum):
    """
    Takes as input a dictionary containing info about a single trip (datum)
    and returns the gender of a user and his/her birth year
    """

    if( (datum.get("Gender") == None or datum.get("Gender") == '') or (datum.get("Birth Year") == '' or datum.get("Birth Year") == None)):

        gender = "N/A"
        birth_yr = "N/A"
        return(str(gender), str(birth_yr))

    else:

        gender = datum.get("Gender")
        birth_yr = datum.get("Birth Year")
        return(str(gender), int(float(birth_yr)))

def wrangle_data(in_file):
    """
    This function takes full data from the specified input file
    and writes the condensed data to a specified output file. The city
    argument determines how the input file will be parsed.
    """

    city = in_file.split('.')[0].title().replace("_", "")

    out_file = str(city)+"-Summary.csv"

    with open(out_file, 'w', newline='') as f_out, open(in_file, 'r') as f_in:

        # set up csv DictWriter object - writer requires column names for the
        # first row as the "field names" argument
        out_colnames = ['Duration (mins)', 'Month', 'Day_of_Month',
                        'Hour_of_Day', 'Day_of_Week', 'Start_Station',
                        'End_Station','User_Type', 'Gender','Year_of_Birth']

        trip_writer = csv.DictWriter(f_out, fieldnames = out_colnames)
        trip_writer.writeheader()

        trip_reader = csv.DictReader(f_in)
        new_point = {}

        # collect data from and process each row
        for row in trip_reader:

            # set up a dictionary to hold the values for the cleaned and trimmed
            # data point
            new_point[city] = row

            ## using the helper functions to get the cleaned data from      ##
            ## the original data dictionaries.                              ##

            duration = duration_in_mins(new_point[city])
            month, hour, day_of_week, day_of_month = time_of_trip(new_point[city])
            user_type = type_of_user(new_point[city])
            start_station, end_station = get_stations(new_point[city])
            gender, birth_yr = genyr(new_point[city])

            trip_writer.writerow({'Duration (mins)': duration,
            'Month': month, 'Day_of_Month': day_of_month, 'Hour_of_Day': hour,
            'Day_of_Week': day_of_week, 'Start_Station': start_station,
            'End_Station': end_station, 'User_Type': user_type,
            'Gender': gender,'Year_of_Birth': birth_yr})

'''
This section defines the helper functions for bike share
'''
            
#Welcome message
text="""
     _______________________________________________________________
    |                                                               |
    |***************************************************************|
    |***************************************************************|
    |** \        /  __  |    __   ___   _  _   __   _______       **|
    |**  \      /  |__| |   |    |   | | \/ | |__|     |   __     **|
    |**   \_/\_/   |__  |__ |__  |___| |    | |__      |  |__|    **|
    |**     _____                  _____                          **|
    |**    |     |     |   /      |       |                       **|
    |**    |_____|  @  |__/   __  |_____  |__   ___    __   __    **|
    |**    |     |  |  |  \  |__|       | |  |  ___|  |    |__|   **|
    |**    |_____|  |  |   \ |__   _____| |  | |___|  |    |__    **|
    |**             _____    _____           _____                **|
    |**                  )  |     |    /|        /                **|
    |**              ( )    |     |   / |       /                 **|
    |**            (_____   |_____|   __|__    /  .               **|
    |***************************************************************|
    |***************************************************************|
    |_______________________________________________________________|

    """
print(text)
print('\nHello! Let\'s explore some US Bike Share data!\n')

## Filenames

chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

## Year 2017 and months

year = 2017
months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
              'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def get_month(month_data):
    """Asks the user for a month and returns the specified month.
    Args:
        month_data: holds the raw data, list of dictionaries.
    Returns:
        (int) the number associated with the month as per calendar
    """
    months = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
                'Jun':6, 'Jul':7, 'Augt':8, 'Sep':9,
                'Oct':10, 'Nov':11, 'Dec':12}

    temp_month_list_1 = []
    temp_month_list_2 = []

    for i in range(0, len(month_data)):

        temp_var = month_data[i]['Month']
        temp_month_list_1.append(temp_var)

    temp_var = sorted(set(temp_month_list_1))

    for i in range(0, len(temp_var)):

        temp_var = months_list[i]
        temp_month_list_2.append(temp_var)

    #An infinite loop until user enters a valid input
    while True:
        try:
            month = input('\nWhich month? Data has been recorded for the following months...:'
                          '\n\n\t"{}"\n\nPlease input valid month\'s name: '.format("----".join(temp_month_list_2)))

            #reducing the character limit to 3
            month = month[:3].title()

            #testing whether user enters a number or a name that is not a
            #month's name
            if(month.isnumeric() or month not in temp_month_list_2):
                raise TypeError
                continue

            else:
                break

        except TypeError:
            print("\nPlease enter a valid month's name from the list!")
            continue

        else:
            break

    return int(months[month])

def get_day(month, day_data):
    """Asks the user for a day and returns the specified day.
    Args:
        month: particular month.
    Returns:
        (int, int) particular day for the user specified month for the year 2017
    """
    temp_date_list = []

    for i in range(0, len(day_data)):

        if(month == int(day_data[i]['Month'])):

            temp_var = day_data[i]['Day_of_Month']
            temp_date_list.append(int(temp_var))

    month_cal = sorted(set(temp_date_list))

    print("\nData for the month: '{}' has been recored.".format(months_list[month-1]))
    print("\nPlease enter a valid date from the below list.\n")
    print(month_cal)

    while True:
        try:
            #user input date
            entered_day = input("\nPlease enter a date/day: ")

            #check if number or other characters are passed
            if(entered_day.isnumeric()):

                if(int(entered_day) <= 0 or int(entered_day) not in month_cal):
                    raise ValueError
                    continue
                else:
                    break
            else:
                raise TypeError

        except (TypeError, ValueError):
            print("\nPlease enter a valid date from the list!")
        else:
            break

    return (month, int(entered_day))

def load_data(filename):
    """
    Loads the wrangled data set into an dictionary
    Args:
        filename: name of the wrangled dataset/.csv file_exists
    Returns:
        (list) list of dictionary is returned
    """

    with open(filename, mode='r') as f_in:

        data_reader = csv.DictReader(f_in)

        list_of_entries = [{k: v for k, v in row.items()}
                for row in data_reader]

    return list_of_entries

def get_city():
    """Asks the user for a city and returns the filename for that city's bike share data.
    Args:
        none.
    Returns:
        (str) Filename for a city's bike share data.
    """
    #A infinite loop that runs until user enters a valid input
    while True:
        try:
            city = input('\nWould you like to see data for:\n\n\t1. Chicago?\n\t2. New York?'
                         '\n\t3. Washington?\n\t4. Quit?\n\nPlease input valid number: ')

            # converting string into integer to get options
            option = int(city)

        except ValueError:
            print("\nSorry, I\'m are expecting a number! and not {}!".format(city.title()))
            continue

        if( option <= 0 or option > 5 ):
            print("\nSorry, your response must not be negative or greater than 4.")
            continue

        #A valid input
        else:
            break

    if (option == 1):
        city = chicago
    elif (option == 2):
        city = new_york_city
    elif (option == 3):
        city = washington
    else:
        print("\nThank you! Have a nice day! :)")
        if(platform.system() == "Windows"):
            system('cls')
        else:
            system('clear')
        exit()

    return city

def filter_data(ordered_data, period):
    #filter data by none/ no filter has been applied to the data
    if (period == "none"):

        filter_none = []

        #compiling data with no filter into a list, so that it can be used for printing
        for i in range(0, len(ordered_data)):

            filter_none.append((round(float(ordered_data[i]['Duration (mins)']), 2), ordered_data[i]['Month'], ordered_data[i]['Day_of_Month'],
                                ordered_data[i]['Day_of_Week'], ordered_data[i]['Hour_of_Day'], ordered_data[i]['Start_Station'],
                                ordered_data[i]['End_Station'], ordered_data[i]['User_Type'], ordered_data[i]['Gender'],
                                ordered_data[i]['Year_of_Birth']))
        
        return (filter_none, ordered_data)
    
    elif (type(period) == int and period in range(1, 13)):

        filter_month = []
        
        month_filter = []
        
        #filter data by month
        for i in range(0, len(ordered_data)):

            if(period == int(ordered_data[i]['Month'])):

                temp_var = ordered_data[i]

                month_filter.append(temp_var)

        #compiling a list of month filtered data
        for i in range(0, len(month_filter)):

            filter_month.append((round(float(month_filter[i]['Duration (mins)']), 2), month_filter[i]['Month'], month_filter[i]['Day_of_Month'],
                                 month_filter[i]['Day_of_Week'], month_filter[i]['Hour_of_Day'], month_filter[i]['Start_Station'],
                                 month_filter[i]['End_Station'],month_filter[i]['User_Type'], month_filter[i]['Gender'],
                                 month_filter[i]['Year_of_Birth']))
            
        
        return (filter_month, month_filter)
    
    elif (type(period) == tuple):

        filter_by_day = []
        day_filter = []

        #filter data by specified day of the month
        for i in range(0, len(ordered_data)):

            if(period[0] == int(ordered_data[i]['Month'])):

                if(period[1] == int(ordered_data[i]['Day_of_Month'])):

                    temp_var = ordered_data[i]

                    day_filter.append(temp_var)

        #compiling a list of month and day filtered data
        for i in range(0, len(day_filter)):

            filter_by_day.append((round(float(day_filter[i]['Duration (mins)']), 2), day_filter[i]['Month'], day_filter[i]['Day_of_Month'],
                                  day_filter[i]['Day_of_Week'], day_filter[i]['Hour_of_Day'], day_filter[i]['Start_Station'],
                                  day_filter[i]['End_Station'], day_filter[i]['User_Type'], day_filter[i]['Gender'],
                                  day_filter[i]['Year_of_Birth']))
            
        
        return (filter_by_day, day_filter)
    
    else:
        #do nothing and return the control
        return

'''
This is the main section/point where the execution begins
'''

def bike_share_analysis():
    """Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    """

    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    new_city = city.split('.')[0].title().replace("_", "")
    file_exists = new_city+"-Summary.csv"

    #Checking if the wrangled file already exists
    while True:
        if(path.exists(file_exists)):
            #do nothing
            break
        else:
            print("\n\nPlease wait while we clean some data...: ")
            start_time = time.time()
            wrangle_data(city)
            print("\nThat took %s seconds." % (time.time() - start_time))
            break

    #loading data into a dictionary
    print("\n\nPlease wait while we load the data...: ")
    start_time = time.time()
    stats_data = load_data(file_exists)
    print("\nThat took %s seconds." % (time.time() - start_time))
    
    #display data or statistics/raw data
    #A infinite loop that runs until user enters a valid input
    while True:
        try:
            time_period = input('\nWould you like to filter the data by:\n\n\t'
                                '1. Month\n\t2. Day\n\t3. None\n\nPlease input valid number: ')
            # converting string into integer to get options
            option = int(time_period)

        except ValueError:
            print("\nSorry, I\'m are expecting a number! and not {}!\n".format(time_period))
            continue

        if(option <= 0 or option > 3 ):
            print("\nSorry, your response must not be negative or greater than 3.")
            continue

        #A valid input
        else:
            break

    if (option == 1):
        #we'll get the number of the month
        time_period = get_month(stats_data)
        filtered_data = filter_data(stats_data, time_period)
        display_statistics(filtered_data[1], time_period)
        display_data(filtered_data[0])

    elif (option == 2):
        #for a particular month, we'll get the day
        month = get_month(stats_data)
        time_period = get_day(month, stats_data)
        filtered_data = filter_data(stats_data, time_period)
        display_statistics(filtered_data[1], time_period)
        display_data(filtered_data[0])

    else:
        # return none
        time_period = "none"
        filtered_data = filter_data(stats_data, time_period)
        display_statistics(filtered_data[1], time_period)
        display_data(filtered_data[0])

    #restart
    while True:
        try:
            restart = input("\nWould you like to continue\n\n\t1. Yes\n\t2. No"
                            "\n\nEnter the number associated with the options: ")
            option = int(restart)

        except ValueError:
            print("\nSorry, I\'m are expecting a number! and not {}!".format(restart.title()))
            continue

        if( option <= 0 or option > 3):
            print("\nSorry, your response must not be negative or greater than 2.")
            continue

        #A valid input
        else:
            break

    if(option == 1):

        #clearing the screen/console if user wants to give it another go
        if(platform.system() == "Windows"):
            system('cls')
        else:
            system('clear')
        bike_share_analysis()

    else:

        #Exiting the application
        if(platform.system() == "Windows"):
            system('cls')
        else:
            system('clear')
        exit()

if __name__ == "__main__":
    bike_share_analysis()
