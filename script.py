#!/usr/bin/env python3

import requests
import re

def average_ac(data):
    return sum(data) / len(data)

def standard_deviation(data):
    mean = average_ac(data)
    return (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5

def get_data(user):
    response = requests.get(f'https://judgegirl.csie.org/user/{user}')
    ac_matches = re.findall(r'''<span class="pricing-table-price">\s*(.*[0-9])\s*<\/span>''', response.text, re.DOTALL)
    ac = int(ac_matches[0])
    return ac

def calc_level(mean, sd, ac):
    z_score = (ac - mean) / sd
    if z_score >= 2:
        return 'S'
    elif z_score >= 1.3:
        return 'A'
    elif z_score >= -0.5:
        return 'B'
    else:
        return 'C'


def main():
    #Updated on 2024/09/11
    database = [1, 16, 3, 27, 6, 34, 12, 24, 36, 18, 30, 12, 16, 37, 4, 32, 15, 10, 22, 34, 16, 15, 29, 0, 27, 2, 38, 4, 18, 11, 13, 18, 8, 28, 3, 0, 6, 20, 79, 20, 10, 15, 23, 16, 14, 10, 1, 13, 1, 17, 73, 0, 8, 15, 26, 6, 9, 27, 7, 0, 77, 29, 20, 26, 46, 39, 24, 12, 20, 35, 39, 26, 39, 25, 17, 28, 24, 20, 21, 16, 21, 16, 28, 26, 21, 0, 0, 3, 0, 0, 11, 0, 0, 0, 0, 0, 0, 20, 3, 0, 17, 0, 1, 3, 29, 4, 0, 0, 0, 0, 3, 6, 9, 1, 0, 13, 2, 0, 26, 12, 17, 12, 19, 28, 14, 12, 38, 14, 23, 0, 8, 27, 38, 24, 23, 18, 38, 1, 33, 29, 12, 16, 12, 0, 23, 13, 9, 12, 15, 35, 0]
    if(input("Do you want to update the data? (Y/N)").upper() == 'Y'):
        database = []
        for i in range(3193, 3344):
            print(f'\rUpdating data {i}/3344', end='')
            try:
                data = get_data(i)
                database.append(data)
            except:
                print("\nError")
                return
        #print(database)
        print("\nUpdate complete")
    try:
        your_ac = int(input("Please enter your AC: "))
        print(f"B13 average AC: {average_ac(database)}")
        print(f"B13 standard deviation: {standard_deviation(database)}")
        print(f"Your level: {calc_level(average_ac(database), standard_deviation(database), your_ac)}")
    except:
        print("Error")

if __name__ == '__main__':
    main()
