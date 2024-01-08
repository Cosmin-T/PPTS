# History.py

import streamlit as st
from logic.search import *
from logic.webdriver import *
from logic.data_track import *
from logic.history import *
from logic.settings import *
import datetime

def hist():
    dashboard()

if __name__ == "__main__":
    apply_settings('eMag Product History', WIDE)
    hist()