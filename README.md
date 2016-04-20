# TwitterBot

Let's make a Twitter bot (or two!)

### Setup in Terminal

  1. Fork this repository to your GitHub account
  2. Clone the forked repository on your computer's Desktop
  3. cd into that directory (`cd twitterbot`)
  4. `virtualenv bot`
  5. OSX: `source bot/bin/activate` | Windows:
  6. `pip install -r requirements.txt`
  7. open your tweetbot folder in a text editor (TextWrangler/Notepad++)

### Twitter

  1. Create a new Twitter account (give it your mobile phone number - sorry.)
  2. Create a [Twitter app](https://apps.twitter.com/) by clicking on "Create New App"
  3. Fill out the necessary details for your bot’s name, description, and website (use your repo URL) and don’t worry about "Callback URL".
  4. Agree to the checkbox for “Terms of Service” and click on "Create Your Twitter Application."
  5. Click on the "Keys and Access Tokens" tab.
  6. Modify the app permissions to have it be able to read and write.
  7. Click the button that says "Regenerate Consumer Key and Secret"
  8. Click the "Create my access token" button
  9. Switch back to your text editor

### Text Editor

  1. Copy your Consumer Key, Consumer Secret, Access Token and Access Token Secret in that order to the places in `tweetbot.py` and `tweetbot2.py`.
  2. In `tweetbot2.py`, change `propublica` to a search term you'd prefer.
  2. Save both files.

### Terminal

  1. Run `python tweetbot.py`
  2. Check your twitter page
  3. Run `python tweetbot2.py`
  4. Open `data.csv` in the same directory.
