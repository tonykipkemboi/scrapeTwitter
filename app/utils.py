from datetime import date
import pandas as pd
import streamlit as st

from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

import snscrape.modules.twitter as sntwitter


@st.cache
def get_tweets(phrase: str, max: int,  start: date, end: date) -> list:
    """Returns a list of tweets that contain the phrase and the time range specified by user.

    Args:
        phrase (str): a word--keyword--or phrase that you would like to scrape from tweets
        start (date): start of date range to search
        end (date): end date for range to perform search

    Returns:
        list: tweets within the specified time range
    """

    output = []

    try:
        for all, tweet in enumerate(sntwitter.TwitterSearchScraper('{} since:{} until:{}'.format(phrase, start, end)).get_items()):
            if all > max:
                break
            output.append([tweet.date, tweet.content,
                          tweet.username, tweet.id])
    except Exception as e:
        print(e)

    return output


@st.cache
def data_cleaner(payload: list) -> pd.DataFrame:
    """Takes in a list of tweets and converts them into a dataframe.

    The dataframe is renamed to the following column names ['date', 'content', 'username', 'tweet_id'].
    A column with links to individual tweets is created usinf status url(https://twitter.com/i/web/status/) + tweet_id.

    Args:
        payload (list): a list containing tweets (date, content, username and tweet_id)

    Returns:
        pd.DataFrame: a DataFrame with the data
    """

    # create dataframe from payload
    df = pd.DataFrame(payload, columns=[
                      'date', 'content', 'username', 'tweet_id'])

    # create a column with links to the tweet using url + tweet_id
    df['tweet_url'] = [
        f'https://twitter.com/i/web/status/{id}' for id in df['tweet_id']]
    
    # add @ before usernames
    df['username'] = ['@'+name for name in df['username']]

    # set date as index
#     df = df.set_index('date')

    return df


@st.cache
def to_csv(df):
    """Convert df to csv"""
    
    return df.to_csv().encode('utf-8')


def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.

    Args:
        df (pd.DataFrame]): Source dataframe

    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection
