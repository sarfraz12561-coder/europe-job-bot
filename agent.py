import os
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# 🎯 آپ کا جیمنائ اے پی آئی اور ٹیلی گرام ٹوکن بالکل ریڈی ہے
GEMINI_API_KEY = "AIzaSyC94U3meMYZImhNedVy8ycvawoAD8wGmu8"
TELEGRAM_BOT_TOKEN = "8929044021:AAG-_qvCX1kRRRTZ0sQKphpbP0acmhnYHn0"
TELEGRAM_CHAT_ID = "8699175083"  # آپ کی کنفرم چیٹ آئی ڈی

SARFRAZ_PROFILE = """
Candidate Name: Sarfraz Ahmed
Experience: 6+ Years as a Heavy Truck Driver
Specialties: Driving Container, Flatbed, and Curtain-side trailers.
Target Roles: Long-haul heavy truck driving, international logistics transport.
"""

def send_telegram_message(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Error: Telegram credentials missing!")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    try:
        r = requests.post(url, json=payload)
        print(f"Telegram Response: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"Telegram Error: {e}")

def check_job_with_gemini(job_title, job_description):
    if not GEMINI_API_KEY:
        print("Gemini API Key missing! Skipping AI matching.")
        return "NO_MATCH"

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # 🟢 یہاں بالکل نیا اور ایکٹو ماڈل 'gemini-1.5-flash' سیٹ کر دیا ہے
        model = genai.GenerativeModel('gemini-1.5-flash')

        prompt = f"""
You are an AI Job Watching Assistant for Sarfraz Ahmed.

Sarfraz's Profile:
{SARFRAZ_PROFILE}

Analyze this Job Listing:
Title: {job_title}
Description: {job_description}

Task:
Determine if this job is a 100% match for Sarfraz's experience in Heavy Truck Driving (specifically Container, Flatbed, Curtain-side).
Respond with EXACTLY 'MATCH' or 'NO_MATCH' followed by a 1-sentence reason in Urdu.
"""
        response = model.generate_content(prompt)
        result = response.text.strip()
        return result
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "NO_MATCH"

def search_europe_jobs():
    print("=== Sarfraz's Europe Job Smart Agent ===")

    sample_job_title = "International Heavy Truck Driver (CE License)"
    sample_job_desc = "Looking for an experienced driver for European routes driving curtain-side and container trailers. Minimum 5 years experience required."

    print("Analyzing job with Gemini AI...")
    ai_decision = check_job_with_gemini(sample_job_title, sample_job_desc)
    print(f"AI Decision: {ai_decision}")

    if isinstance(ai_decision, str) and "MATCH" in ai_decision:
        print("Perfect Match Found!")
        alert_text = (
            "🎯 *New Perfect Job Match Found!* 🌍\n\n"
            f"💼 *Job:* {sample_job_title}\n"
            f"🤖 *AI Analysis:* جیمنائ نے اس جاب کو آپ کی پروفائل کے لیے بالکل درست پایا ہے۔\n"
            "📩 *اگلا سٹیپ:* ای میل آٹومیشن کی تیاری کی جا رہی ہے۔"
        )
        send_telegram_message(alert_text)
    else:
        print("Job did not match Sarfraz's profile or invalid response received.")

if __name__ == "__main__":
    search_europe_jobs()
