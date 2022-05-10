import pandas as pd


# provides the total budget in a specific year
def total_year_budget(year: int) -> int:
    total_budget = pd.read_csv("national-budget.csv", index_col=["שנה"])
    total_budget = total_budget.loc[year]
    total = total_budget['הוצאה נטו'].sum()
    return total


# provides the office budget in a specific year
def total_office_budget(year: int, office: str) -> int:
    specific_budget = pd.read_csv("national-budget.csv", index_col=["שנה", "שם רמה 2"])
    specific_budget = specific_budget.loc[year, office]
    total_specific_budget = specific_budget['הוצאה נטו'].sum()
    return total_specific_budget


# provides the ratio of the office's budget from total budget in a given year
def year_office_budget_ratio(year: int, office: str) -> float:
    total_specific_budget = total_office_budget(year, office)
    total = total_year_budget(year)
    return total_specific_budget / total


def education_budget(year: int) -> int:
    return total_office_budget(year, 'חינוך')


def security_budget_ratio(year: int) -> float:
    return year_office_budget_ratio(year, "בטחון")


def largest_budget_ratio(office: str) -> int:
    df = pd.read_csv("national-budget.csv")
    max_budget = 0
    max_year = 0
    for year in df["שנה"].unique():
        curr_budget = year_office_budget_ratio(year, office)
        if curr_budget > max_budget:
            max_budget = curr_budget
            max_year = year
    return max_year


# my original question:
# which office spent the most on shopping abroad in a given year?
def shopping_abroad(year: int) -> int:
    budget = pd.read_csv("national-budget.csv", index_col=["שנה", "שם מיון רמה 2"])
    budget = budget.loc[year, 'קניות בחו"ל'].groupby(["שם רמה 2"])['הוצאה נטו'].sum()
    return budget.idxmax()


if __name__ == '__main__':
    # notes: "PerformanceWarning: indexing past lexsort depth may impact performance." warning appears due to an open
    # bug: https://github.com/pandas-dev/pandas/issues/19771, https://github.com/pandas-dev/pandas/issues/17931
    print(education_budget(2022))
    print("---")
    print(security_budget_ratio(2019))
    print("---")
    print(largest_budget_ratio('בטחון'))
    print("---")
    print(shopping_abroad(2022))
    print("---")

