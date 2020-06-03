import pandas as pd
import matplotlib.pyplot as plt


def avgs_per_year(year):
    # filter the data
    afc_path = 'CSVs/AFCPlayoffs/AFCPlayoffStandings' + year + '.csv'
    nfc_path = 'CSVs/NFCPlayoffs/NFCPlayoffStandings' + year + '.csv'
    scoring_path = 'CSVs/ScoringOffense/ScoringOffense' + year + '.csv'

    afc = pd.read_csv(afc_path)
    nfc = pd.read_csv(nfc_path)
    scoring = pd.read_csv(scoring_path)
    scoring = scoring.loc[0:31, :]

    playoffs_afc = afc.loc[0:5, 'Tm'].apply(lambda name: name[0:-4])
    playoffs_nfc = nfc.loc[0:5, 'Tm'].apply(lambda name: name[0:-4])
    playoffs = list(pd.concat([playoffs_afc, playoffs_nfc]))
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
    # return the avgs somehow
    return [
             {'Year': year, 'Playoff Teams': playoffs_off_avg,
              'Non-Playoff Teams': non_playoffs_off_avg},
             {'Year': year, 'Playoff Teams': playoffs_def_avg,
              'Non-Playoff Teams': non_playoffs_def_avg},
             {'Year': year, 'Playoff Teams': playoffs_st_avg,
              'Non-Playoff Teams': non_playoffs_st_avg},
           ]


def get_avgs(category1, category2, playoffs, non_playoffs):
    playoffs_avg = playoffs[category1].mean() + \
        playoffs[category2].mean()
    non_playoffs_avg = non_playoffs[category1].mean() + \
        non_playoffs[category2].mean()
    return playoffs_avg, non_playoffs_avg


def plot_avgs(avgs, title):
    avgs_df = pd.DataFrame(data=avgs)
    avgs_df.plot(x='Year')
    plt.ylabel('Average Touchdowns')
    plt.title('Average Touchdowns in ' + title + ' per Year')
    plt.savefig(title + 'Averages.png')


def main():
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
