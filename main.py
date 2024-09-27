from mylib.lib import (
    load_dataset,
    grab_mean,
    grab_median,
    grab_std,
    create_bar,
    create_line,
)


def g_describe(dataset):
    g = load_dataset(dataset)
    return g.describe()


def data_manage(dataset):
    """custom describe"""
    df = load_dataset(dataset)
    mean = grab_mean(df)
    median = grab_median(df)
    std = grab_std(df)
    stats_df = {
        "name": "U.S. briths",
        "mean": mean,
        "median": median,
        "std": std,
    }
    return stats_df


def general_viz_combined(dataset):
    """saves all the figures at once"""
    df = load_dataset(dataset)
    create_bar(df)
    create_line(df)


def save_to_md(dataset):
    stats_df = data_manage(dataset)

    general_viz_combined(dataset)

    with open("result.md", "w", encoding="utf-8") as f:
        # Write the title
        f.write("# U.S. Births\n\n")

        # Write the summary statistics as tables
        f.write("## Summary Statistics\n")
        markdown_table = (
            f"| Name       | {stats_df['name']} |\n"
            "|------------|------------|\n"
            f"| Mean       | {stats_df['mean']} |\n"
            f"| Median     | {stats_df['median']} |\n"
            f"| Std Dev    | {stats_df['std']} |\n"
        )
        f.write(markdown_table)

        f.write("## Birth bar Over Time (1795-2021)\n")
        f.write("![birth_bar](birth_bar.png)\n\n")

        f.write("## Birth plot (1795-2021)\n")
        f.write("![birth_lineplot](birth_lineplot.png)\n")


if __name__ == "__main__":

    dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_1994-2003_CDC_NCHS.csv"

    save_to_md(dataset)
