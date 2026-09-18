import datetime

def get_category(contact_number):
    categories = {
        "1234567890": "Spam",
        "9876543210": "Personal",
        "5555555555": "Work",
    }
    return categories.get(contact_number, "Unknown")

def get_current_time():
    return datetime.datetime.now().time()

def office_hours_check(current_time):
    start_time = datetime.time(9, 0)
    end_time = datetime.time(17, 0)
    
    return start_time <= current_time <= end_time

def handle_call(contact_number):
    category = get_category(contact_number)
    current_time = get_current_time()
    in_office_hours = office_hours_check(current_time)

    if category == "Spam":
        if not in_office_hours:
            send_voice_message(contact_number, "This number is recognized as spam.")
        else:
            send_to_voicemail(contact_number)
    elif category == "Unknown":
        send_to_voicemail(contact_number)
    elif category == "Personal":
        ring_normal(contact_number)
    elif category == "Work":
        if in_office_hours:
            ring_normal(contact_number)
        else:
            send_voice_message(contact_number, "Our office hours are over. Please call back during business hours.")
    else:
        ring_normal(contact_number)

def send_voice_message(contact_number, message):
    print(f"Sending voice message to {contact_number}: {message}")

def ring_normal(contact_number):
    print(f"Ringing {contact_number}")

def send_to_voicemail(contact_number):
    print(f"Sending {contact_number} to voicemail")

# Example usage:
handle_call("5555555555")