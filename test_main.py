from main import g_describe, data_manage, general_viz_combined, save_to_md


dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_1994-2003_CDC_NCHS.csv"


def test_g_describe():
    describe = g_describe(dataset)
    # print(describe)
    assert describe.shape == (8, 2)


def test_data_manage():
    stats_df = data_manage(dataset)
    # print(stats_df)
    assert stats_df["name"] == "U.S. briths"


def test_general_viz_combined():
    general_viz_combined(dataset)


def test_save_to_md():
    save_to_md(dataset)


if __name__ == "__main__":
    test_g_describe()
    test_data_manage()
    test_general_viz_combined()
    test_save_to_md()
