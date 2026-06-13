import os
import requests
from datetime import date

# ==========================================
# FUNCTION 1: Fetch Live Weather Details
# ==========================================
def get_weather(city="Thiruvananthapuram"):
    """Fetch today's weather as a one-line text summary."""
    url = f"https://wttr.in/{city}?format=3"
    try:
        # Give up trying to connect after 10 seconds so the script doesn't hang forever
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"Weather unavailable ({e})"

# ==========================================
# FUNCTION 2: Fetch a Motivational Quote
# ==========================================
def get_quote():
    """Fetch a random motivational quote from ZenQuotes API."""
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # ZenQuotes returns a list containing a dict: [{"q": "text", "a": "author"}]
        quote = data[0]['q']
        author = data[0]['a']
        return f'"{quote}" — {author}'
    except Exception as e:
        return f"Quote unavailable ({e})"

# ==========================================
# FUNCTION 3: Build the Text Block Summary
# ==========================================
def build_summary():
    """Assemble the final daily summary text block using a clean f-string."""
    today = date.today().strftime("%A, %d %B %Y")
    weather = get_weather()
    quote = get_quote()
    
    summary = f"""
====================================
PULSE — Daily Summary
{today}
====================================

WEATHER
{weather}

TODAY'S QUOTE
{quote}
====================================
"""
    return summary

# ==========================================
# FUNCTION 4: Run & Export the Artifact
# ==========================================
def run():
    """Main entry point to execute the bot and save the artifact file."""
    summary = build_summary()
    print(summary) # Shows up beautifully in our GitHub Actions execution log
    
    # Save it to a downloadable text file
    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    print("Pulse ran successfully: daily_summary.txt generated.")

# The entry guard ensures this code only runs when executed directly
if __name__ == "__main__":
    run()
