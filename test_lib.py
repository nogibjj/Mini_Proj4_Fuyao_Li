from mylib.lib import (
    load_dataset,
    grab_mean,
    grab_median,
    grab_std,
    create_bar,
    create_line,
)


dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_1994-2003_CDC_NCHS.csv"


def test_load_dataset():
    df = load_dataset(dataset)
    assert df.shape == (10, 2)


def test_grab_mean():
    df_year = load_dataset(dataset)
    mean = grab_mean(df_year)
    assert mean == df_year.describe().iloc[1, 1]


def test_grab_median():
    df_year = load_dataset(dataset)
    median = grab_median(df_year)
    assert median == df_year.describe().iloc[5, 1]


def test_grab_std():
    df_year = load_dataset(dataset)
    std = grab_std(df_year)
    assert std == df_year.describe().iloc[2, 1]


def test_create_bar():
    df_year = load_dataset(dataset)
    create_bar(df_year)


def test_create_line():
    df_year = load_dataset(dataset)
    create_line(df_year)


if __name__ == "__main__":
    test_load_dataset()
    test_grab_mean()
    test_grab_median()
    test_grab_std()
    test_create_bar()
    test_create_line()
