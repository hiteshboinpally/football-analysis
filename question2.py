"""
Alan Liu and Hitesh Boinpally

A python module that wrangles the quarterback data
from 2015 to 2019 and creates a visualization to
compare playoff and nonplayoff teams
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from central import playoff_year, get_nfl_clean

sns.set()


def get_qb(year, test=False):
    """
    Return a dataframe of quarterback stats from the given year
    Each row represents a quarterback of that team, his
    quarterback rating, the year for later merging.
    Note that this dataframe only contains relevant quarterbacks
    with more than 100 throwing attempts
    """
    test_str = ""
    if test:
        test_str = "Test"

    # Get data
    main_path = 'cse-163-final-project/CSVs/'
    qb = pd.read_csv(main_path + '/QuarterbackPassing/' + test_str +
                     'QuaterbackPassing' + year + '.csv')
    playoff = playoff_year(year)
    # Filter for qb with at least 100 attempts and only for relevant columns
    attempt = (qb['Att'] > 100)
    qb = qb[attempt]
    qb = qb[['Tm', 'Rate']]
    # Get NFL team abbreviation and merge qb and team data
    nfl_teams = get_nfl_clean()
    qb = qb.merge(nfl_teams, how='inner', left_on='Tm', right_on='Abbrev')
    # Distinguish playoff and non-playoff team
    is_playoffs = qb['Name'].isin(playoff)
    qb.loc[:, 'is_playoff'] = is_playoffs
    # Add a new column for year
    qb['year'] = int(year)
    return qb


def get_combine():
    """
    Combine the dataframes of quarterback stats from
    2015 to 2019
    """
    # Create a list of dataframe that stores the
    # quarterback stats for each year
    qb = list()
    for year in range(2015, 2020):
        qb.append(get_qb(str(year)))
    # Concat the dataframes by rows
    qb_all = pd.concat(qb)
    return qb_all


def plot_qb(qb_data, title):
    """
    Plot and save a boxplot that compares the quarterback rating
    between playoff and nonplayoff teams for all five years
    """
    sns.boxplot(x='year', y='Rate', hue='is_playoff', data=qb_data)
    plt.title('Quarterback Ratings for Playoff and NonPlayoff Team by Year')
    plt.savefig('plots/' + title + '.png')


def main():
    data = get_combine()
    plot_qb(data, 'Q2QBRatings')


if __name__ == "__main__":
    main()
