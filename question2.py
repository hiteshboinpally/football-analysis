import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from central import playoff_year, get_nfl_clean

sns.set()


def get_qb(year):
    # Get data
    main_path = 'cse-163-final-project/CSVs/'
    qb = pd.read_csv(main_path + '/QuarterbackPassing/QuaterbackPassing'
                     + year + '.csv')
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
    qb = list()
    for year in range(2015, 2020):
        qb.append(get_qb(str(year)))
    qb_all = pd.concat(qb)
    return qb_all


def plot_qb(qb_data):
    sns.boxplot(x='year', y='Rate', hue='is_playoff', data=qb_data)
    plt.title('Quarterback Ratings for Playoff and NonPlayoff Team by Year')
    plt.savefig('Q2QBRatings.png')


def main():
    data = get_combine()
    plot_qb(data)


if __name__ == "__main__":
    main()
