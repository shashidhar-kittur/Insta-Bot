import random
import schedule
import time
from datetime import datetime, timedelta
from instabot import Bot

# Initialize the bot
bot = Bot()

# Login credentials
USERNAME = "your_username"
PASSWORD = "your_password"

# Messages for different times of day
greetings = {
    "morning": ["Good morning!", "Rise and shine!", "Morning! Have a great day!"],
    "afternoon": ["Good afternoon!", "Hope you're having a nice afternoon!"],
    "evening": ["Good evening!", "Hope you had a great day!", "Evening!"],
    "night": ["Good night!", "Sweet dreams!", "Goodnight!"]
}

# Times ranges for greetings
time_ranges = {
    "morning": ("06:00", "09:00"),
    "afternoon": ("12:00", "14:00"),
    "evening": ("17:00", "19:00"),
    "night": ("21:00", "23:00")
}

# Track last sent times
last_sent = {
    "morning": None,
    "afternoon": None,
    "evening": None,
    "night": None
}


# Function to choose a random time within a range
def choose_random_time(start, end):
    start_time = datetime.strptime(start, "%H:%M")
    end_time = datetime.strptime(end, "%H:%M")
    random_time = start_time + timedelta(
        minutes=random.randint(0, int((end_time - start_time).total_seconds() / 60))
    )
    return random_time.strftime("%H:%M")

# Function to send a greeting
def send_greeting(greeting_type):
    if greeting_type in greetings:
        message = random.choice(greetings[greeting_type])
        # Here you should put the user ID or username of the recipient
        recipient = "recipient_username"
        bot.send_message(message, [recipient])
        print(f"Sent '{message}' to {recipient}")
        last_sent[greeting_type] = datetime.now()


# Function to schedule a single greeting
def schedule_single_greeting(greeting_type):
    start, end = time_ranges[greeting_type]
    send_time = choose_random_time(start, end)
    schedule.every().day.at(send_time).do(send_greeting, greeting_type=greeting_type)
    print(f"Scheduled '{greeting_type}' greeting at {send_time}")


# Function to schedule all greetings
def schedule_greetings():
    for greeting_type in greetings.keys():
        schedule_single_greeting(greeting_type)


if __name__ == "__main__":
    bot.login(username=USERNAME, password=PASSWORD)
    schedule_greetings()

    while True:
        now = datetime.now()
        # Check if a day has passed since the last greeting was sent and reschedule
        for greeting_type, last_time in last_sent.items():
            if last_time and (now - last_time).hour >= 12:
                schedule.clear(greeting_type)
                schedule_single_greeting(greeting_type)
        schedule.run_pending()
        time.sleep(1)
