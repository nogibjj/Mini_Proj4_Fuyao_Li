"""
    library file
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_dataset(dataset):
    df = pd.read_csv(dataset)
    df_year = df.groupby('year')['births'].sum().reset_index()
    return df_year


def grab_mean(df_year):
    """Calculate the mean of births per year (1994-2003)"""
    mean = df_year['births'].mean()
    return mean


def grab_median(df_year):
    """Calculate the median of births per year (1994-2003)"""
    median = df_year['births'].median()
    return median


def grab_std(df_year):
    """Calculate the std of births per year (1994-2003)"""
    std = df_year['births'].std()
    return std


def create_bar(df_year, jupy=False):
    """Create a bar plot to visualize yearly total births"""

    plt.figure(figsize=(10, 6))
    sns.barplot(x=df_year['year'], y=df_year['births'], color='skyblue')
    plt.title('Total Births Per Year (1994-2003)')
    plt.xlabel('Year')
    plt.ylabel('Total Births')
    plt.xticks(rotation=45)
    plt.savefig('birth_bar.png', dpi=300)
    if jupy is True:
        plt.show()


def create_line(df_year, jupy=False):
    """create line plot of yearly births"""

    plt.figure(figsize=(10, 6))
    plt.plot(df_year['year'], df_year['births'], marker='o', color='green')
    plt.title('Total Births per Year (1994-2003)')
    plt.xlabel('Year')
    plt.ylabel('Number of Births')
    plt.savefig('birth_lineplot.png', dpi=300)
    if jupy is True:
        plt.show()
