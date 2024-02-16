import requests
import schedule
import time
import json


def check_github_username_availability(username):
    url = f"https://github.com/{username}"
    response = requests.get(url)
    return response.status_code == 404


def send_discord_notification(username, webhook_url):
    data = {
        "content": f"The GitHub username '{username}' is available!",
        "username": "GitHub Username Checker",
    }
    result = requests.post(webhook_url, json=data)
    print(f"Notification sent: {result.status_code}")


def job():
    username = "junta57"  # Replace with the GitHub username you want to check
    webhook_url = "https://discord.com/api/webhooks/1203385423401975940/69XB-Eo_B6CIapsKNmoXRzx82B6Z934K8dTRyq5Z_-qqGyp2rlf54viU4XhJMb-2kW7E"  # Replace with your Discord webhook URL

    if check_github_username_availability(username):
        send_discord_notification(username, webhook_url)
    else:
        print(f"{username} is not available.")


# Schedule the job to run every other hour
schedule.every(0.1).hours.do(job)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
