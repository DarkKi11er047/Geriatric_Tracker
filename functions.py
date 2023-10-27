import pandas
import streamlit as st

FILENAME = "patient1.csv"


def sleep_check(filename=FILENAME):
    df = pandas.read_csv(filename, sep=";")

    sleep = []

    for index, row in df[:len(df)].iterrows():
        sleep.append(float(row["Sleep"]))

    ls = len(sleep)
    avg_sleep = sum(sleep[:ls - 3]) / (ls - 3)
    sleep_3days = sum(sleep[ls:ls - 4:-1]) / 3

    if sleep_3days > 8 or sleep_3days < avg_sleep:
        st.info("Patient requires attention with regards to sleep. Contact Caretaker at 9246115674")
    else:
        with st.expander("Sleep"):
            st.info("Sleep is good")



def activity_check(filename=FILENAME):
    df = pandas.read_csv(filename, sep=";")

    activity = []

    for index, row in df[:len(df)].iterrows():
        activity.append(float(row["Activity"]))

    ls = len(activity)
    avg_activity = sum(activity[:ls - 3]) / ls - 3
    activity_3days = sum(activity[ls:ls - 4:-1]) / 3

    if activity_3days < avg_activity:
        st.info("Patient requires attention with regards to activity. Contact Caretaker at 9246115674")
    else:
        with st.expander("Activity"):
            st.info("Patient is active")



def meds_check(filename=FILENAME):
    df = pandas.read_csv(filename, sep=";")

    meds = []

    for index, row in df[:len(df)].iterrows():
        meds.append(bool(row["Medication"]))

    ls = len(meds)

    if not meds[ls + 1:ls]:
        st.info("Medicines not taken! Contact Caretaker at 9246115674")


    else:
        with st.expander("Medicines status"):
            st.info("Medicines taken")

def hygiene_check(filename=FILENAME):
    df = pandas.read_csv(filename, sep=";")

    hygiene = []

    for index, row in df[:len(df)].iterrows():
        hygiene.append(str(row["Hygiene"]))

    ls = len(hygiene)

    with st.expander("Hygiene status"):
            st.info(hygiene[-1])

def mental_check(filename=FILENAME):
    df = pandas.read_csv(filename, sep=";")

    mental = []

    for index, row in df[:len(df)].iterrows():
        mental.append(str(row["Mental State"]))

    ls = len(mental)

    with st.expander("Mental State"):
            st.info(mental[-1])
