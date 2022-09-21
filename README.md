# Scrape Tweets by Searching Keywords using Snspcrape 
This is a simple Tweet Search App built with `python` + `snscrape module` + `Streamlit`.

I got tired of searching tweets using `Twitter` search and decided to build out a standalone app that I can query for `keywords/phrases/hashtags/usernames...e.t.c.` and subsequently download the data into a `csv` file for further custom analysis

`FYI: This is roughly put together but does the job for what I needed.`

### Usage

- The app is deployed on Streamlit [here](https://tonykipkemboi-scrapetwitter-appdriver-qevmgf.streamlitapp.com/).

###### If you would like to customize it for your development purposes follow these steps(these are windows commands):
- Clone this repo to your folder of choice:
```
  git clone https://github.com/tonykipkemboi/scrapeTwitter.git
```
- Change directory into the folder:
```
cd scrapeTwitter
```
- Create a python virtual environment:
```
python -m venv env
```
- Activate virtual environment:
```
.\env\Script\activate
```
- Install dependecies which are in the `requirements.txt` file:
```
python -m pip install -r requirements.txt
```
- Now you are ready top run the program in your localhost:
```
cd app
```
```
streamlit run driver.py
```
- The app will open in your browser. Feel free to play with the code and as you save changes, the app will update in real-time.

### What Next?
- Maybe make it a bit robust by adding unit tests and refactoring some of the code.
- Add a page for querying tweets by user.
- Create a dashboard after doing some analysis on mined tweets.

You can dm me on [Twitter](https://twitter.com/ynot_kip) for collaboration or just holla!

