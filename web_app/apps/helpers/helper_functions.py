import numpy as np


def get_random_city():
    cities = ['Mumbai', 'Delhi', 'Jaipur', 'Pune', 'Chennai',
              'Bangalore', 'Mysore', 'Chandigarh', 'Jodhpur']
    r = np.random.randint(0, 10)
    return cities[r]


def get_random_gender():
    gender = ['M', 'F']
    r = np.random.randint(0, 2)
    return gender[r]


def get_random_age():
    age = ['20-25', '25-30', '30-35', '35-40', '40-45',
           '45-50', '50-55', '55-60', '60-65', '65-70']
    r = np.random.randint(0, 10)
    return age[r]


def get_extended_values(value):
    operation = np.random.randint(0, 2)
    extended_values = []
    if operation:
        for i in range(6):
            i = np.random.randint(0, 100)
            extended_values.append(i + value)
    else:
        for i in range(6):
            i = np.random.randint(0, 100)
            extended_values.append(value - i)
    return extended_values


def get_random_segment():
    segments = ['Travel', 'Food', 'Banking', 'War', 'Lifestyle', 'Hacking']
    return segments[np.random.randint(0, 5)]
