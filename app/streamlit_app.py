from datetime import datetime
from utils import *
from PIL import Image


def main():
    """_summary_
    """

    # ask user for input phrase
    phrase = st.text_input(
        'Enter phrase or text to scrape from Twitter', 'Type here...')

    # beware that a large number will result in a slower scrape; minimum of 10
    max_results = st.number_input(
        'Enter maximum number of tweets to search return', min_value=10)

    # enter date range
    # today = datetime.date.today()
    start_date = st.date_input('Enter a start date (less than end date)')
    end_date = st.date_input('Enter end date (greater than start date)')

    # check if end date is greater than today, return error
    if start_date and end_date:
        # search user input
        if phrase and max_results:
            search = get_tweets(phrase, max_results,
                                start=start_date, end=end_date)
            cleaner = data_cleaner(search)
            selection = aggrid_interactive_table(df=cleaner)
           
            # interactive table
            if selection:
                st.write('You selected:')
                st.json(selection['selected_rows'])
                
            csv = to_csv(cleaner)
            
            # download data in csv format
            st.download_button(
                "Download CSV",
                csv,
                "file.csv",
                "text/csv",
                key='download-csv'
            )

    else:
        st.error('Error: End date must be less than todays date.')


if __name__ == '__main__':
    st.set_page_config(layout="wide", page_icon="🤖",
                       page_title="Twitter Scrapper App")

    st.title("🤖 TweetScrape App")
    st.write(
        "This app lets you scrape tweets by searching for keywords present in target tweets..."
    )

    main()
