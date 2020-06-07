import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from central import playoff_year

sns.set()


def get_team_offense(year):
    file_path = 'cse-163-final-project/CSVs/TeamOffense/TeamOffense' \
        + year + '.csv'
    team_offense = pd.read_csv(file_path, skiprows=1)
    team_offense = team_offense.loc[0:31, ['Tm', 'Y/P', '1stD', 'Yds.3']]

    is_playoffs = team_offense['Tm'].isin(playoff_year(year))
    team_offense['Is Playoff'] = is_playoffs
    team_offense['Year'] = int(year)

    return team_offense


def combine_team_offense():
    team_offenses = list()
    for year in range(2015, 2020):
        team_offenses.append(get_team_offense(str(year)))
    all_team_offenses = pd.concat(team_offenses)
    return all_team_offenses


def offensive_plots(off_data):
    fig, [ax1, ax2, ax3] = plt.subplots(3, figsize=(20, 15))

    sns.boxplot(x="Year", y="Y/P", hue="Is Playoff", data=off_data, ax=ax1)
    ax1.set_title('Offensive Yards per Play by Year', fontsize=16)
    adjust_size(ax1, 'Yards per Play')

    sns.boxplot(x="Year", y="1stD", hue="Is Playoff", data=off_data, ax=ax2)
    ax2.set_title('Offensive 1st Down by Year', fontsize=16)
    adjust_size(ax2, '1st Downs')

    sns.boxplot(x="Year", y="Yds.3", hue="Is Playoff", data=off_data, ax=ax3)
    ax3.set_title('Offensive Penatly Yards by Year', fontsize=16)
    adjust_size(ax3, 'Penalty Yards')

    fig.suptitle('Miscellaneous Offensive Stats by Year', fontsize=20)
    plt.subplots_adjust(hspace=0.3)

    fig.savefig('question3OffensiveData.png')


def adjust_size(ax, ylabel, xlabel='Year'):
    ax.set_xlabel(xlabel, fontsize=16)
    ax.set_ylabel(ylabel, fontsize=16)
    ax.tick_params(labelsize=16)


def main():
    offensive_data = combine_team_offense()
    offensive_plots(offensive_data)
    print('finished offensive plot')


if __name__ == '__main__':
    main()
