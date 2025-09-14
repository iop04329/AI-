import streamlit as st
from dashboard import dashboard_page
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    dashboard_page()


if __name__ == "__main__":
    main()
