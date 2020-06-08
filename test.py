"""
Alan Liu and Hitesh Boinpally
CSE 163

This file answers test all 3 questions
"""


import question1
import question2
import question3


def test_question1():
    """
    Test question1.py with small test file
    We confirm that question1 plots are correct
    """
    scoring_test = list()
    for year in range(2015, 2020):
        scoring_test.append(question1.avgs_per_year(str(year), test=True))

    off_avgs = []
    def_avgs = []
    st_avgs = []
    for i in range(0, 5):
        off_avgs.append(scoring_test[i][0])
        def_avgs.append(scoring_test[i][1])
        st_avgs.append(scoring_test[i][2])

    question1.plot_avgs(off_avgs, "OffenseTest")
    question1.plot_avgs(def_avgs, "DefenseTest")
    question1.plot_avgs(st_avgs, "SpecialTeamsTest")


def test_question2():
    """
    Test question2.py with small test file
    We confirm that question2 plot is correct
    """
    qb_test = question2.get_qb('2015', test=True)
    question2.plot_qb(qb_test, 'Q2QBRatingsTest')


def test_offense():
    """
    Test the offense data of question3.py with small test file
    We confirm that offense plot is correct
    """
    offensive_test = question3.get_team_data('2015',
                                             'TeamOffense/TestTeamOffense',
                                             ['Tm', 'Y/P', '1stD', 'Yds.3'])
    question3.offensive_plots(offensive_test, 'Q3OffensiveTest')


def test_sp():
    """
    Test the special team data of question3.py with small test file
    We confirm that special team plot is correct
    """
    folder = 'KickAndPuntReturns/TestKickAndPuntReturns'
    special_test = question3.get_team_data('2015', folder,
                                           ['Tm', 'Y/R', 'Y/Rt'])
    question3.special_plots(special_test, 'Q3SpecialTest')


def test_defense():
    """
    Test the defense data of question3.py with small test file
    We confirm that defense plot is correct
    """
    def_test = question3.get_team_defense('2015', test=True)
    question3.defensive_plots(def_test, 'Q3DefensiveTest')


def test_question3():
    """
    Test question3.py with small test file
    We confirm that question3 plots are correct
    """
    test_offense()
    test_sp()
    test_defense()


def main():
    test_question1()
    test_question2()
    test_question3()


if __name__ == "__main__":
    main()
