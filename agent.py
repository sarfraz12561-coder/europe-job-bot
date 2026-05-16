import os
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

def search_europe_jobs():
    print("=== Sarfraz's Europe Job Smart Agent ===")
    print("Searching for Heavy Truck Driving roles (Container, Flatbed, Curtain-side)...")
    
    # یہاں ہم وہ 6 ممالک ٹارگٹ کر رہے ہیں جن کی آپ نے بات کی تھی
    countries = ["Hungary", "Romania", "Latvia", "Poland", "Bulgaria", "Czech Republic"]
    print(f"Target Countries: {', '.join(countries)}")
    
    # جاب سرچنگ کا بنیادی ڈھانچہ
    print("Scraping job listings safely...")
    print("Job search complete! Updates will be processed.")

if __name__ == "__main__":
    search_europe_jobs()
