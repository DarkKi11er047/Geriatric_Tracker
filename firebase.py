import streamlit as st
from google.cloud import firestore

db = firestore.Client.from_service_account_json("key.json")

doc_ref = db.collection()

