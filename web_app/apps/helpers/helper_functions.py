import numpy as np
import pandas as pd

df = pd.read_csv(r"D:\Events\VIL Codefest\CustomDash\web_app\appdata\sample_plotting.csv")


def get_location(customer):
    return df.iloc[customer]['Location']


def get_gender(customer):
    return df.iloc[customer]['Gender']


def get_age(customer):
    return df.iloc[customer]['Age']


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


def get_segment(customer):
    return df.iloc[customer]['Customer Segment']


def get_churn(customer):
    return str(df.iloc[customer]['Churn']) + "%"
