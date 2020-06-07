import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from central import playoff_year

sns.set()


def get_team_defense(year):
    conversions = get_team(year, 'ConversionsAgainst/ConversionsAgainst',
                           ['Tm', '3D%'])
    conversions['3D%'] = conversions['3D%'].apply(lambda s: float(s[0:-1]))

    drives = get_team(year, 'DriveAvgsAgainst/DriveAvgsAgainst', ['Tm', 'TO%'])
    merge_cols = ['Tm', 'Is Playoff', 'Year']
    all_defense = conversions.merge(drives, left_on=merge_cols,
                                    right_on=merge_cols)
    return all_defense


def get_team(year, folder, cols):
    main_path = 'cse-163-final-project/CSVs/'
    file_path = main_path + folder \
        + year + '.csv'
    team = pd.read_csv(file_path, skiprows=1)
    team = team.loc[0:31, cols]

    is_playoffs = team['Tm'].isin(playoff_year(year))
    team['Is Playoff'] = is_playoffs
    team['Year'] = int(year)

    return team


def combine_defense():
    team = list()
    for year in range(2015, 2020):
        team.append(get_team_defense(str(year)))
    all_team = pd.concat(team)
    return all_team


def combine_team(folder, cols):
    team = list()
    for year in range(2015, 2020):
        team.append(get_team(str(year), folder, cols))
    all_team = pd.concat(team)
    return all_team


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


def special_plots(sp_data):
    fig, [ax1, ax2] = plt.subplots(2, figsize=(20, 15))

    sns.boxplot(x="Year", y="Y/R", hue="Is Playoff", data=sp_data, ax=ax1)
    ax1.set_title('Yards per Punt Returns by Year', fontsize=16)
    adjust_size(ax1, 'Yards per Punt Returns')

    sns.boxplot(x="Year", y="Y/Rt", hue="Is Playoff", data=sp_data, ax=ax2)
    ax2.set_title('Yards per Kick-Off Returns by Year', fontsize=16)
    adjust_size(ax2, 'Yards per Kick-Off Returns')

    fig.suptitle('Miscellaneous Special Team Stats by Year', fontsize=20)
    plt.subplots_adjust(hspace=0.3)

    fig.savefig('question3SpecialData.png')


def defensive_plots(def_data):
    fig, [ax1, ax2] = plt.subplots(2, figsize=(20, 15))

    sns.boxplot(x="Year", y="3D%", hue="Is Playoff", data=def_data, ax=ax1)
    ax1.set_title('3rd Down Conversions Against Percentage by Year',
                  fontsize=16)
    adjust_size(ax1, '3rd Down Percentage')

    sns.boxplot(x="Year", y='TO%', hue="Is Playoff", data=def_data, ax=ax2)
    ax2.set_title('Defensive Turnover Percentage by Year', fontsize=16)
    adjust_size(ax2, 'Turnover Percentage')

    fig.suptitle('Miscellaneous Defensive Stats by Year', fontsize=20)
    plt.subplots_adjust(hspace=0.3)

    fig.savefig('question3DefensiveData.png')


def adjust_size(ax, ylabel, xlabel='Year'):
    ax.set_xlabel(xlabel, fontsize=16)
    ax.set_ylabel(ylabel, fontsize=16)
    ax.tick_params(labelsize=16)


def main():
    offensive_data = combine_team('TeamOffense/TeamOffense',
                                  ['Tm', 'Y/P', '1stD', 'Yds.3'])
    offensive_plots(offensive_data)
    print('finished offensive plot')

    sp_data = combine_team('KickAndPuntReturns/KickAndPuntReturns',
                           ['Tm', 'Y/R', 'Y/Rt'])
    special_plots(sp_data)
    print('finished special teams plot')

    def_data = combine_defense()
    defensive_plots(def_data)
    print('finished defensive plot')


if __name__ == '__main__':
    main()
