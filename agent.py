import os
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# اب تک پروفائل کا ڈیٹا جو جیمنائ ہینڈل کر رہا ہے کا ہے
SARFRAZ_PROFILE = """
Candidate Name: Sarfraz Ahmed
Experience: 6+ Years as a Heavy Truck Driver
Specialties: Driving Container, Flatbed, and Curtain-side trailers.
Target Roles: Long-haul heavy truck driving, international logistics transport.
"""

def send_telegram_message(message):
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    if not bot_token or not chat_id:
        print("Error: Telegram credentials missing!")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Telegram Error: {e}")

def check_job_with_gemini(job_title, job_description):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Gemini API Key missing! Skipping AI matching.")
        return "NO_MATCH"

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

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

    try:
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

    # یہاں اب ڈیٹا ٹائپ اور اسپیسنگ بالکل درست ہے
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
