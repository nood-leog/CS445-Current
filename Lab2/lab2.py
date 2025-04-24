#lab2.py
#visualizing Real Data Sets using Seaborn
#Generate five meaningful and unique visualizations using Seaborn
#Save each visualization as an image file boyce-bargraph.png


#Data files:
#default of credit card clients.csv
#https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients

#X2: Gender (1 = male; 2 = female).
#X3: Education 1 = graduate school; 2 = university; 3 = high school; 4 = others).
#X4: Marital status (1 = married; 2 = single; 3 = others).



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea

#global dataset variable
df = pd.read_csv('default of credit card clients.csv', skiprows=1)



#explain the data
def explain_data():
    print("\n"
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

    # Only use numeric columns
    numeric_df = df.select_dtypes(include='number')

    # Compute correlation matrix
    correlation_matrix = numeric_df.corr()

    # Draw heatmap
    sea.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True, linewidths=.5)

    plt.title('Correlation Heatmap of Credit Default Dataset')
    plt.tight_layout()
    plt.savefig('boyce-heatmap-correlations.png')
    plt.show()

#barchart with avg bal limit-y and age-x --- #2
def bar_creditbyage():
    plt.figure(figsize=(12, 6))
    sea.barplot(x='AGE', y='LIMIT_BAL', data=df, palette= 'viridis')
    plt.title('Average Credit Limit by Age')
    plt.xlabel('Age')
    plt.ylabel('Average Credit Limit')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('boyce-bar-creditbyage.png')
    plt.show()

#boxplot with credit limit-y and education-x
def boxplot_limiteducation():
    plt.figure(figsize=(10, 6))

    # Map education codes to readable labels
    edu_labels = {
        1: 'Graduate School',
        2: 'University',
        3: 'High School',
        4: 'Others'
    }

    #ignore education levels 0, 5, 6 because they are in the dataset but not documented by the source
    filtered_df = df[df['EDUCATION'].isin(edu_labels.keys())].copy()
    filtered_df['EDUCATION_LABEL'] = filtered_df['EDUCATION'].map(edu_labels)

    sea.boxplot(x='EDUCATION_LABEL', y='LIMIT_BAL', data=filtered_df, palette='Set2')

    plt.title('Distribution of Credit Limits by Education Level', fontsize=14)
    plt.xlabel('Education Level', fontsize=12)
    plt.ylabel('Credit Limit', fontsize=12)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('boyce-boxplot-education-limit.png')
    plt.show()


#seaborn barplot
def barplot():
    df['LIMIT_BIN'] = pd.cut(df['LIMIT_BAL'], bins=5)
    plt.figure(figsize=(12, 6))
    sea.barplot(x='LIMIT_BIN', y='default payment next month', data=df)
    plt.title('Default Rate by Credit Limit Bracket')
    plt.xlabel('Credit Limit Bins')
    plt.ylabel('Default Rate')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('boyce-bargraph.png')
    plt.show()



explain_data()
print_data_head()

heatmap_correlations() #1
bar_creditbyage() #2
boxplot_limiteducation() #3

barplot() #TODO finish this
