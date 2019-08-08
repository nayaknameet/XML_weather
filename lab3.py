'''' Name: Nameet Mahendra Nayak
Student_id: 1001308637''''
import requests                                                         #import to get URL
from bs4 import BeautifulSoup                                           #To parse the values
url = "http://w1.weather.gov/xml/current_obs/index.xml"                 # saving link to variable name url
response = requests.get(url)                                            # Saving the response from the url
user_latitude = input("Enter uder_latitiude(for Arlington 32.65829): ") #asking user to enter latitude
user_longitude = input("Enter uder_longitude(for Arlington -97.09509): ")   #asking user to enter longitude
invalid_input = 0                                                                       # variable for invalid input
to_parse = BeautifulSoup(response.text, 'html.parser')                  #convert everything to parse
station_name = to_parse.find_all('station')                             #find all the tuples as station

def display(current_station):                                           # function to display all the information
        to_fetch_data = current_station.xml_url.text                    # fetching data for requested values
        response = requests.get(to_fetch_data)                          #get url information
        to_parse = BeautifulSoup(response.text, 'html.parser')         
        print("Maximum Temperature: "+to_parse.temp_f.text)
        print("Minimum Temperature: "+to_parse.temp_c.text)                 # Display the values
        print("Maximum dewpoint: "+to_parse.dewpoint_f.text)            
        print("Minimum dewpoint: "+to_parse.dewpoint_c.text)
        print("Wind Direction: "+to_parse.wind_dir.text)                 
        print("Wind speed: "+to_parse.wind_mph.text)
        try:
            print("Weather: "+to_parse.weather.text)                        #Because not all the places conains this value
        except:
            print("No weather information(i.e how cloudy )")
            
while(True):

    for names in station_name:                                              # to iterate over the items in stations
        if names.latitude.text==user_latitude and names.longitude.text==user_longitude:         #to check if the user inputs match with values in xml file
            display(names)                                                      #calling display the function
            invalid_input = 1                                                       # this states that the input were correct
            break                                                                   # job of the function is done
    if invalid_input==0:                                                            # if the values are not found the station then it's invalid
        print("Wrong Input(s), please restart the program.")                        # print invalid inputs and ask user to restart
        break                                                                       # break the function
    
    user_wish = input("Do you want to refresh with same values:(y/n)").lower()          # ask user if he/she wants to refresh with same inputs, and convert it to lower
    if user_wish == 'y':                                                            # if the answer is yes 
        continue                                                                    # continue to resend the request and fetch
    else:
        print("\nThank you for using this service.")                                #If user want to discontinue, terminate the program.
        break


    
