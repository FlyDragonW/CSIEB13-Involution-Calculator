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
    #Updated on 2024/09/09
    database = [10, 3, 25, 6, 30, 12, 23, 35, 16, 28, 11, 11, 35, 4, 25, 15, 9, 21, 29, 14, 12, 27, 25, 2, 34, 4, 18, 10, 13, 16, 8, 22, 3, 6, 20, 72, 19, 7, 10, 23, 3, 9, 7, 1, 12, 1, 15, 71, 8, 13, 23, 5, 9, 26, 7, 74, 28, 19, 26, 38, 38, 24, 9, 15, 28, 27, 16, 34, 24, 17, 26, 22, 18, 20, 16, 19, 15, 25, 25, 21, 7, 19, 3, 17, 1, 2, 29, 4, 3, 6, 9, 1, 10, 2, 26, 11, 17, 11, 19, 27, 11, 8, 38, 12, 23, 8, 21, 28, 22, 16, 16, 37, 1, 28, 25, 12, 14, 11, 22, 11, 6, 11, 14, 35]
    if(input("Do you want to update the data? (Y/N)").upper() == 'Y'):
        for i in range(3193, 3344):
            database = []
            print(f'\rUpdating data {i}/3344', end='')
            try:
                data = get_data(i)
                database.append(data)
            except:
                print("\nError")
                return
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