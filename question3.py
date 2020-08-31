"""
Alan Liu and Hitesh Boinpally
CSE 163

This file answers research question #3, plotting miscellaneous data for each
category of Offense, Defense, and Special Teams, separated between playoff and
non-playoff teams from the past five years.
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from central import playoff_year

sns.set()


def get_team_defense(year, test=False):
    """
    Generates and returns a pandas DataFrame containing miscellaneous defensive
    data for the given year. Returned DataFrame also has columns for Year and
    whether or not the team was a playoff team that year. Assumes year is a
    string representing a year between 2015-2019.
    """
    test_str = ""
    if test:
        test_str = "Test"

    conversions = get_team_data(year, 'ConversionsAgainst/' + test_str +
                                'ConversionsAgainst', ['Tm', '3D%'])
    conversions['3D%'] = conversions['3D%'].apply(lambda s: float(s[0:-1]))

    drives = get_team_data(year, 'DriveAvgsAgainst/' + test_str +
                           'DriveAvgsAgainst', ['Tm', 'TO%'])

    merge_cols = ['Tm', 'Is Playoff', 'Year']
    all_defense = conversions.merge(drives, left_on=merge_cols,
                                    right_on=merge_cols)

    return all_defense


def get_team_data(year, folder, cols):
    """
    Generates and returns a pandas DataFrame containing miscellaneous data
    based on the givne folder for the given year using the given cols. Returned
    DataFrame also has columns for Year and whether or not the team was a
    playoff team that year. Assumes year is a string representing a year
    between 2015-2019. Assumes that folder is a valid file path as a string.
    Assumes that cols is a valid list of columns for the specified dataset.
    """
    main_path = 'cse-163-final-project/CSVs/'
    file_path = main_path + folder + year + '.csv'

    team_data = pd.read_csv(file_path, skiprows=1)
    team_data = team_data.loc[0:31, cols]

    is_playoffs = team_data['Tm'].isin(playoff_year(year))
    team_data['Is Playoff'] = is_playoffs
    team_data['Year'] = int(year)

    return team_data


def combine_defense():
    """
    Combines and returns a pandas DataFrame containing miscellaneous defensive
    data from the past five years.
    """
    team = list()
    for year in range(2015, 2020):
        team.append(get_team_defense(str(year)))
    all_team = pd.concat(team)
    return all_team


def combine_team(folder, cols):
    """
    Combines and returns a pandas DataFrame containing miscellaneous NFL data
    from the past five years based on the given folder and cols. Assumes that
    folder is a vaild file path represented as a string. Assumes that cols is
    a valid list of columns for the specified dataset.
    """
    team = list()
    for year in range(2015, 2020):
        team.append(get_team_data(str(year), folder, cols))
    all_team = pd.concat(team)
    return all_team


def offensive_plots(off_data, title):
    """
    Plots and saves miscellaneous offensive data from the past five years
    based on the given off_data. Assumes that off_data is a pandas DataFrame
    containing 'Year', 'Is Playoff', 'Y/P', '1stD', 'Yds.3' columns. Saves the
    plot as 'Q3OffensiveData.png'.
    """
    fig, [ax1, ax2, ax3] = plt.subplots(3, figsize=(20, 15))

    sns.boxplot(x='Year', y='Y/P', hue='Is Playoff', data=off_data, ax=ax1)
    ax1.set_title('Offensive Yards per Play by Year', fontsize=16)
    adjust_size(ax1, 'Yards per Play')

    sns.boxplot(x='Year', y='1stD', hue='Is Playoff', data=off_data, ax=ax2)
    ax2.set_title('Offensive 1st Down by Year', fontsize=16)
    adjust_size(ax2, '1st Downs')

    sns.boxplot(x='Year', y='Yds.3', hue='Is Playoff', data=off_data, ax=ax3)
    ax3.set_title('Offensive Penatly Yards by Year', fontsize=16)
    adjust_size(ax3, 'Penalty Yards')

    fig.suptitle('Miscellaneous Offensive Stats by Year', fontsize=20)
    plt.subplots_adjust(hspace=0.3)

    fig.savefig('plots/' + title + '.png')


def special_plots(sp_data, title):
    """
    Plots and saves miscellaneous special teams data from the past five years
    based on the given sp_data. Assumes that sp_data is a pandas DataFrame
    containing 'Year', 'Is Playoff', 'Y/R', 'Y/Rt' columns. Saves the
    plot as 'Q3SpecialTeamsData.png'.
    """
    fig, [ax1, ax2] = plt.subplots(2, figsize=(20, 15))

    sns.boxplot(x='Year', y='Y/R', hue='Is Playoff', data=sp_data, ax=ax1)
    ax1.set_title('Yards per Punt Returns by Year', fontsize=16)
    adjust_size(ax1, 'Yards per Punt Returns')

    sns.boxplot(x='Year', y='Y/Rt', hue='Is Playoff', data=sp_data, ax=ax2)
    ax2.set_title('Yards per Kick-Off Returns by Year', fontsize=16)
    adjust_size(ax2, 'Yards per Kick-Off Returns')

    fig.suptitle('Miscellaneous Special Team Stats by Year', fontsize=20)
    plt.subplots_adjust(hspace=0.3)

    fig.savefig('plots/' + title + '.png')


def defensive_plots(def_data, title):
    """
    Plots and saves miscellaneous defensive data from the past five years
    based on the given def_data. Assumes that def_data is a pandas DataFrame
    containing 'Year', 'Is Playoff', '3D%', 'TO%' columns. Saves the
    plot as 'Q3DefensiveData.png'.
    """
    fig, [ax1, ax2] = plt.subplots(2, figsize=(20, 15))

    sns.boxplot(x='Year', y='3D%', hue='Is Playoff', data=def_data, ax=ax1)
    ax1.set_title('3rd Down Conversions Against Percentage by Year',
                  fontsize=16)
    adjust_size(ax1, '3rd Down Percentage')

    sns.boxplot(x='Year', y='TO%', hue='Is Playoff', data=def_data, ax=ax2)
    ax2.set_title('Defensive Turnover Percentage by Year', fontsize=16)
    adjust_size(ax2, 'Turnover Percentage')

    fig.suptitle('Miscellaneous Defensive Stats by Year', fontsize=20)
    plt.subplots_adjust(hspace=0.3)

    fig.savefig('plots/' + title + '.png')


def adjust_size(ax, ylabel, xlabel='Year'):
    """
    Adjusts the fontsize of the ticks and axis labels for the given ax. Assumes
    that ax is an axis. Assumes that ylabel is a string. Assumes that xlabel is
    a string and defaults to 'Year'.
    """
    ax.set_xlabel(xlabel, fontsize=16)
    ax.set_ylabel(ylabel, fontsize=16)
    ax.tick_params(labelsize=16)


def main():
    offensive_data = combine_team('TeamOffense/TeamOffense',
                                  ['Tm', 'Y/P', '1stD', 'Yds.3'])
    offensive_plots(offensive_data, 'Q3OffensiveData')
    print('finished offensive plot')

    sp_data = combine_team('KickAndPuntReturns/KickAndPuntReturns',
                           ['Tm', 'Y/R', 'Y/Rt'])
    special_plots(sp_data, 'Q3SpecialTeamsData')
    print('finished special teams plot')

    def_data = combine_defense()
    defensive_plots(def_data, 'Q3DefensiveData')
    print('finished defensive plot')


if __name__ == '__main__':
    main()
