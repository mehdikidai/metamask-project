import csv
import time
import os
from dotenv import load_dotenv


if not load_dotenv():
    print(".env file not found")
    exit()

password = os.getenv('PASSWORD','123')


with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['first_name'] + " your password " + password) 
        time.sleep(1)

# file = open('data.csv', mode='r', newline='', encoding='utf-8')
# reader = csv.DictReader(file)
# for row in reader:
#     print(row['first_name'] + " your password " + password) 
#     time.sleep(1)
    
# file.close()