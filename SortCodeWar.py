import pandas as pd
import numpy as np
import csv
import re


def main():
    #funtions that pass around targeted data
    new_string = base()
    #base()
    sortcatch = Sorting(new_string)
    List_Details_Cleanup_Ineraction(sortcatch)

def base():
    new_string = []

    users_email = input("provide your email address")
    my_string = input("Provide a sentence.")
    while len(my_string)>=1:
        try:
            my_string = re.sub('[".,?:;]', '', my_string)  # replaces punctuation with whitespace
            my_string = re.sub("[']", '', my_string)

            for word in my_string.split():
                new_string.append(word)
#Todo if file exist move curser to first empty row
            with open('users_sentence_contactinfo.csv', 'w', newline='') as csvfile:
                fieldnames = ['users_email', 'users_entry']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerow({'users_email': users_email,'users_entry': new_string})
                #writer.writerow({})


        except:
            if len(new_string)<1:
                print("Your sentence must be at least 1 word long")
        else:
            return new_string

def Sorting(new_string):

    new_string.sort() #puts list in abc order
    sortcatch = sorted(new_string, key=len) #sort from least to greatest by string length
    print(sortcatch)
    List_Details_Cleanup_Ineraction(sortcatch)
    return sortcatch

def List_Details_Cleanup_Ineraction(sortcatch): #count list length print

    list_length = len(sortcatch)#count list length print

    counter = []
    count = 0
    for c in range (list_length):
        count +=1
        counter.append(count) #counts lenght original string provided by user


    length_catch = []
    for word in sortcatch:
        word_length = len(word)
        length_catch.append(word_length)

    fact_rundown = np.column_stack((sortcatch, length_catch)) #offered as column stack for readability ###NUMPY output###
    pd.DataFrame(fact_rundown).to_csv("filetest.csv") #writes df to csv.
    print (pd.DataFrame(fact_rundown))

    #ToDo: (1) pass fact rundown to padas.
    #ToDo: (2) Save dataframe to CSV

    first_item = sortcatch[0]
    shortest_len = (len(first_item))  #save shortest entry to varriable
    last_index = (int(list_length))
    last_item = sortcatch.pop() #saving longest entry to varriable

    ###exporting DF to csv
    #export_df_csv

    print(fact_rundown)   ###NUMPY output###
    print(list_length)
    print(counter)  # glue to sortcatch to make a matrix
    print ("PLACEHOLDERS The shortest word in the list is: ", first_item)
    print ("PLACEHOLDERS The lenght of the shortest word is: ", shortest_len)
    print( '\n' * 4, '**PLACEHOLDER***', '\n' * 4)
    print("this is the last item: ", last_item)
    print("this is the index of the last item: ", last_index)


   #ToDo. Merge out of order legnth based sentence into one string with spanish punctiation ? enclosing the sentence

    input()
if __name__ == "__main__":
    main()
