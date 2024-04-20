# Task 1 
import csv

# Task 12 
import json

# Task 2
compromised_users = []

# Task 3
with open('passwords.csv') as password_file: 

  # Task 4
  password_csv = csv.DictReader(password_file)

  # Task 5
  for password_row in password_csv: 

    # Task 6
    #print(password_row['Username'])

    # Task 7
    compromised_users.append(password_row['Username'])
print(compromised_users)

# Task 8
with open('compromised_users.txt', 'w') as compromised_user_file:

  # Task 9
  for compromised_user in compromised_users: 

    # Task 10 and 11
    compromised_user_file.write(compromised_user)

# Task 13
with open('boss_message.json', 'w') as boss_message:

  # Task 14
  boss_message_dict = {
  "recipient": "The Boss",
  "message": "Mission Success"
  }
  
# Task 15
  json.dump(boss_message_dict, boss_message)

# Task 16
with open('new_passwords.csv', 'w') as new_passwords_obj: 

# Task 17
  slash_null_sig = """
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

  """

# Task 18 
  new_passwords_obj.write(slash_null_sig)
print(slash_null_sig)







