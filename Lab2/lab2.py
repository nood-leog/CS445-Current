#lab2.py
#visualizing Real Data Sets using Seaborn

#Data files:
#default of credit card clients.csv

#X2: Gender (1 = male; 2 = female).
#X3: Education 1 = graduate school; 2 = university; 3 = high school; 4 = others).
#X4: Marital status (1 = married; 2 = single; 3 = others).


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea

#ignore future warnings lol
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)


#global dataset variable
df = pd.read_csv('default of credit card clients.csv', skiprows=1)


#explain the data
def explain_data():
    print("\n"
            "This dataset contains information about credit card holders in Taiwan.\n"
            "It includes some basic demographic information, like sex, age, education level, marital status and also includes\n"
          " payment history, and default status.\n"
          
          "Sourced from UCI Machine Learning Repository\n"
          )


#Print a portion of the raw data using head()
def print_data_head():
    #read the dataset
    print(df.head())
    print("\nColumn names:\n", df.columns.tolist(), "\n")

#heatmap correlation --- #1
def heatmap_correlations():
    plt.figure(figsize=(16, 12))

    #only use numeric columns
    numeric_df = df.select_dtypes(include='number')

    #compute correlation matrix
    correlation_matrix = numeric_df.corr()

    #draw heatmap
    sea.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True, linewidths=.5)

    #plot
    plt.title('Correlation Heatmap of Credit Default Dataset', fontsize=16)
    plt.tight_layout()
    plt.savefig('boyce-heatmap-correlations.png')
    plt.show()

#barchart with avg bal limit-y and age-x --- #2
def bar_creditbyage():
    plt.figure(figsize=(12, 6))
    sea.barplot(x='AGE', y='LIMIT_BAL', data=df, palette= 'viridis')
    plt.title('Average Credit Limit by Age', fontsize=14)
    plt.xlabel('Age')
    plt.ylabel('Average Credit Limit')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('boyce-bar-creditbyage.png')
    plt.show()

#boxplot with credit limit-y and education-x --- #3
def boxplot_limiteducation():
    plt.figure(figsize=(10, 6))

    #map education codes to readable labels
    edu_labels = {
        1: 'Graduate School',
        2: 'University',
        3: 'High School',
        4: 'Others'
    }

    #ignore education levels 0, 5, 6 because they are in the dataset but not documented by the source for whatever reason
    filtered_df = df[df['EDUCATION'].isin(edu_labels.keys())].copy()
    filtered_df['EDUCATION_LABEL'] = filtered_df['EDUCATION'].map(edu_labels)

    sea.boxplot(x='EDUCATION_LABEL', y='LIMIT_BAL', data=filtered_df, palette='Set2')

    #plot
    plt.title('Distribution of Credit Limits by Education Level', fontsize=14)
    plt.xlabel('Education Level', fontsize=12)
    plt.ylabel('Credit Limit', fontsize=12)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('boyce-boxplot-limiteducation.png')
    plt.show()

#barplot for credit limit-x and average default rate-y --- 4
def barplot_DefaultRate():
    #rounded bins
    bins = [0, 50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, df['LIMIT_BAL'].max()]
    labels = ['0–50k', '50k–100k', '100k–150k', '150k–200k', '200k-250k', '250k-300k', '300k-350k', '350k-400k', '400k-450k', '450k-500k', '500k-550k', '550k-600k', '600k-650k', '650k-700k', '700k-750k+']

    #create the bin column
    df['LIMIT_BIN'] = pd.cut(df['LIMIT_BAL'], bins=bins, labels=labels, include_lowest=True)

    #find the mean default rate per bin
    grouped = df.groupby('LIMIT_BIN')['default payment next month'].mean().reset_index()

    plt.figure(figsize=(14, 6))
    sea.barplot(x='LIMIT_BIN', y='default payment next month', data=grouped, palette='coolwarm')

    #plot
    plt.title('Average Default Rate by Credit Limit Bracket', fontsize=14)
    plt.xlabel('Credit Limit Bracket', fontsize=12)
    plt.ylabel('Default Rate (Proportion)', fontsize=12)
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig('boyce-bargraph-defaultrate.png')
    plt.show()

#pairplot of financial metrics --- #5
def pairplot_financial():
    #calulate totals
    df['TOTAL_BILLS'] = df[[f'BILL_AMT{i}' for i in range(1, 7)]].sum(axis=1)
    df['TOTAL_PAYMENTS'] = df[[f'PAY_AMT{i}' for i in range(1, 7)]].sum(axis=1)

    #pairplot features
    features = ['LIMIT_BAL', 'TOTAL_BILLS', 'TOTAL_PAYMENTS', 'AGE', 'default payment next month']
    pair_df = df[features].copy()

    #rename column from the dataset to something more readable
    pair_df.rename(columns={'default payment next month': 'Default'}, inplace=True)

    #plot
    sea.pairplot(pair_df, hue='Default', palette='coolwarm', diag_kind='kde', corner=True)
    plt.title('Pairplot of Financial Metrics', fontsize=16, y=3.5)
    plt.savefig('boyce-pairplot-financial.png')
    plt.show()



explain_data()
print_data_head()

heatmap_correlations() #1
bar_creditbyage() #2
boxplot_limiteducation() #3
barplot_DefaultRate() #4
pairplot_financial() #5
