#######Counting the no 0f types in a list. Here an excel sheet with N rows and columns with data about mobile apps. Here I am checking the Content rating column and identify no: of types of ratings exists in it.

AppleStore=open('AppleStore.csv') # Import the data
from csv import reader 
reading_data=reader(AppleStore) #Read the data
app_data=list(reading_data) # Covert it to a list
content_ratings=[] #decalre a new list
for row in app_data[1:]: #Itirate through all rows except the header row
    cr=row[-6] # read the content rating from the col
    if cr in content_ratings: # if the value exist in the list , pass
        continue
    else: 
        content_ratings.append(cr) # Add the rating if its not present in the list
print(content_ratings) # print the list