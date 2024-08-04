import pywhatkit
import pandas as pd
from datetime import datetime

df = pd.read_excel('RSVP for Wedding.xlsx')

current_time = datetime.now()
current_hour = current_time.hour
upcoming_minute = current_time.minute+1


wait_time = 10 # time to wait before sending the message (second)
close_tab = True # close the browser tab
close_time = 3 # time to close the tab (minute)

url = 'https://fredwrecked.github.io/wedding-website/'

messages = []

for i,invite in df.iterrows():
    try:
        name = invite['Nick Name']
        contact_no = invite['Contact Number'].replace(' ','')
        print(f'Sending message to {name} ({contact_no})')
        contact_no = '+27609384819'

        no_guest_invite = f"""
Dear {name}

We would like to invite you to celebrate our wedding with us on the 15th of February 2025 at Kleinood farm.

Please RSVP for you and only you (we’ve taken the liberty of inviting your partners ourselves). To RSVP, follow this link: {url}. If you get stuck or have any questions please let us know.

Dust off your dancing shoes for a midsummer night’s dream in the forest.

Love
Fred and Katharien
        """

        guest_invite = f"""
Dear {name}

We would like to invite you to celebrate our wedding with us on the 15th of February 2025 at Kleinood farm.

Please RSVP for yourself and, if you’d like, your plus one to share the evening with. To RSVP, follow this link {url}. To add your plus one please just type their name after you’ve successfully RSVP’d. If you get stuck or have any questions please let us know.

Dust off your dancing shoes for a midsummer night’s dream in the forest.

Love
Fred and Katharien
        """

        if invite['Has Plus One']:
            messages.append(guest_invite)
            pywhatkit.sendwhatmsg(contact_no, guest_invite, current_hour,
                                  upcoming_minute, wait_time, close_tab, close_time)
        else:
            messages.append(no_guest_invite)
            pywhatkit.sendwhatmsg(contact_no, no_guest_invite, current_hour,
                          upcoming_minute, wait_time, close_tab, close_time)

        upcoming_minute += 1
        print("Successfully Sent!")

    except:
        messages.append("Did not send.")
        print("An Unexpected Error!")

    print()
    if i == 0:
        break

df['Message'] = messages
df.to_excel('RSVP for Wedding (Invite outcome).xlsx', index = False)