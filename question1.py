import pandas as pd
import matplotlib.pyplot as plt
from central import playoff_year


def avgs_per_year(year):
    """
    Calculates and returns a list of three dictionaries for the given year of
    the average touchdowns on offense, defense, and special teams for playoff
    and non-playoff teams from that year. First dictionary is offense, second
    is defense, third is special teams. Assumes given year is a string.
    """
    # filter the data
    main_path = 'cse-163-final-project/CSVs/'
    scoring_path = main_path + 'ScoringOffense/ScoringOffense' + year + '.csv'

    scoring = pd.read_csv(scoring_path)
    scoring = scoring.loc[0:31, :]

    playoffs = playoff_year(year)
    is_playoffs = scoring['Tm'].isin(playoffs)

    playoffs_scoring = scoring[is_playoffs].fillna(0)
    non_playoffs_scoring = scoring[~is_playoffs].fillna(0)

    # find the avgs in each category
    playoffs_off_avg, non_playoffs_off_avg = get_avgs('RshTD', 'RecTD',
                                                      playoffs_scoring,
                                                      non_playoffs_scoring)

    playoffs_def_avg, non_playoffs_def_avg = get_avgs('IntTD', 'FblTD',
                                                      playoffs_scoring,
                                                      non_playoffs_scoring)

    playoffs_st_avg, non_playoffs_st_avg = get_avgs('PR TD', 'KR TD',
                                                    playoffs_scoring,
                                                    non_playoffs_scoring)
    # return the avgs
    return [
             {'Year': year, 'Playoff Teams': playoffs_off_avg,
              'Non-Playoff Teams': non_playoffs_off_avg},
             {'Year': year, 'Playoff Teams': playoffs_def_avg,
              'Non-Playoff Teams': non_playoffs_def_avg},
             {'Year': year, 'Playoff Teams': playoffs_st_avg,
              'Non-Playoff Teams': non_playoffs_st_avg},
           ]


def get_avgs(category1, category2, playoffs, non_playoffs):
    """
    Calculates and returns the total average scoring in the given category1
    and category2 for each of the given playoffs and non_playoffs as a tuple
    of two elements. Assumes that given categories are strings and valid
    columns of given playoffs and non_playoffs. Assumes that given playoffs
    and non_playoffs are pandas DataFrames.
    """
    playoffs_avg = playoffs[category1].mean() + \
        playoffs[category2].mean()
    non_playoffs_avg = non_playoffs[category1].mean() + \
        non_playoffs[category2].mean()
    return playoffs_avg, non_playoffs_avg


def plot_avgs(avgs, title):
    """
    Plots and saves the given avgs with the x-axis as Years and y-axis as
    scoring. Titles the graph and saved file based on given category. Assumes
    that given category is a string. Assumes that given avgs is a list of
    dictionaries containing 'Year' and playoff team vs non-playoff team data.
    """
    avgs_df = pd.DataFrame(data=avgs)
    avgs_df.plot(x='Year')
    plt.ylabel('Average Touchdowns')
    plt.title('Average Touchdowns in ' + title + ' per Year')
    plt.savefig(title + 'Averages.png')


def main():
    print("Start")
    avgs_2015 = avgs_per_year('2015')
    avgs_2016 = avgs_per_year('2016')
    avgs_2017 = avgs_per_year('2017')
    avgs_2018 = avgs_per_year('2018')
    avgs_2019 = avgs_per_year('2019')

    off_avgs = [avgs_2015[0], avgs_2016[0], avgs_2017[0], avgs_2018[0],
                avgs_2019[0]]
    def_avgs = [avgs_2015[1], avgs_2016[1], avgs_2017[1], avgs_2018[1],
                avgs_2019[1]]
    st_avgs = [avgs_2015[2], avgs_2016[2], avgs_2017[2], avgs_2018[2],
               avgs_2019[2]]
    plot_avgs(off_avgs, "Offense")
    plot_avgs(def_avgs, "Defense")
    plot_avgs(st_avgs, "Special Teams")
    print('completed')


if __name__ == "__main__":
    main()
