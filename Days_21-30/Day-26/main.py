

import pandas




# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()

#TODO 1. Create a dictionary in this format:
nato_data_frame=pandas.read_csv("nato.csv")

mydict={row.letter:row.code for (key,row) in nato_data_frame.iterrows()}
while True:
    name=input("what is your name: ").strip().upper()
    try:
        result=[mydict[letter] for letter in name]

    except KeyError:
        print("only letters in alphabet are allowed")
    except ValueError:
        print("only letters in alphabet are allowed")
    except Exception as e:
        print(e)
    else:
        print(result)
        break









#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


