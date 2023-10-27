import pandas
import streamlit as st

FILENAME = "patient1.csv"


def sleep_check(filename=FILENAME):
    df = pandas.read_csv(filename, sep=";")

    sleep = []

    for index, row in df[:len(df)].iterrows():
        sleep.append(float(row["sleep"]))

    ls = len(sleep)
    avg_sleep = sum(sleep[:ls - 3]) / (ls - 3)
    sleep_3days = sum(sleep[ls:ls - 4:-1]) / 3

    if sleep_3days > avg_sleep or sleep_3days < avg_sleep:
        st.
        print("Patient requires attention with regards to sleep")
    else:
        print("Sleep is good")


def activity_check(filename=FILENAME):
    df = pandas.read_csv(filename, sep=";")

    activity = []

    for index, row in df[:len(df)].iterrows():
        activity.append(float(row["activity"]))

    ls = len(activity)
    avg_activity = sum(activity[:ls - 3]) / ls - 3
    activity_3days = sum(activity[ls:ls - 4:-1]) / 3

    if activity_3days < avg_activity:
        print("Patient requires attention with regards to activity")
    else:
        print("Patient is active")


def meds_check(filename=FILENAME):
    df = pandas.read_csv(filename, sep=";")

    meds = []

    for index, row in df[:len(df)].iterrows():
        meds.append(bool(row["medication"]))

    ls = len(meds)

    if not meds[ls + 1:ls]:
        print("Medicines not taken")
