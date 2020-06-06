import pandas as pd


def playoff_year(year):
    # filter the data
    afc_path = 'CSVs/AFCPlayoffs/AFCPlayoffStandings' + year + '.csv'
    nfc_path = 'CSVs/NFCPlayoffs/NFCPlayoffStandings' + year + '.csv'

    afc = pd.read_csv(afc_path)
    nfc = pd.read_csv(nfc_path)

    playoffs_afc = afc.loc[0:5, 'Tm'].apply(lambda name: name[0:-4])
    playoffs_nfc = nfc.loc[0:5, 'Tm'].apply(lambda name: name[0:-4])
    playoffs = list(pd.concat([playoffs_afc, playoffs_nfc]))
    return playoffs


def get_nfl_clean():
    nfl_teams = pd.read_csv('CSVs/nfl_teams.csv')
    # Select only relevant columns
    nfl_teams = nfl_teams[['Name','Abbreviation']]
    # Fix name
    nfl_teams.loc[20, 'Name'] = 'New York Giants'
    nfl_teams.loc[21, 'Name'] = 'New York Jets'
    # Append team not in the dataframe
    new_rows = list()
    new_rows.append({'Name': 'San Diego Chargers', 'Abbreviation': 'SDG'})
    new_rows.append({'Name': 'St. Louis Rams', 'Abbreviation': 'STL'})
    for r in new_rows:
        nfl_teams = nfl_teams.append(r, ignore_index=True)
    # Fix abbreviation
    nfl_teams.loc[11, 'Abbreviation'] = 'GNB'
    nfl_teams.loc[15, 'Abbreviation'] = 'KAN'
    nfl_teams.loc[19, 'Abbreviation'] = 'NOR'
    nfl_teams.loc[22, 'Name'] = 'Oakland Raiders'
    nfl_teams.loc[22, 'Abbreviation'] = 'OAK'
    nfl_teams.loc[26, 'Abbreviation'] = 'SFO'
    nfl_teams.loc[29, 'Abbreviation'] = 'TAM'
    nfl_teams.loc[18, 'Abbreviation'] = 'NWE'
    nfl_teams.rename({'Abbreviation': 'Abbrev'}, axis=1, inplace=True)
    return nfl_teams

#if __name__ == '__main__':
