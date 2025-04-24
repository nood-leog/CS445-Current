#lab2.py
#visualizing Real Data Sets using Seaborn

#Data files:
#car.data - car evaluation data set

import matplotlib.pyplot as plt
import pandas as pd

#explain the data
def explain_data():
    print("\n"
          "Sourced from UCI Machine Learning Repository\n"
          )


#Print a portion of the raw data using head()
def print_data_head():
    #read the dataset

    df = pd.read_csv('car.data', delimiter=';')#open the dataset
    print(df.head()) #print the head


#Bar Graph Visualization
def bar_graph():
    df = pd.read_csv('student-mat.csv', sep=';')#open the dataset
    age_counts = df['age'].value_counts().sort_index()

    bars = plt.bar(age_counts.index, age_counts.values, color='skyblue', edgecolor='black')
    plt.xlabel('Age', fontsize=9)
    plt.ylabel('Number of Students', fontsize=9)
    plt.title('Number of Students by Age', fontsize=12)

    #Label bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom')

    #cell text
    plt.text(19, 80, "This bar chart shows how many\n students are in each age group. \nWe can tell that most students in this \ncourse are between the ages of 15 and 18", fontsize=9)

    plt.tight_layout()
    plt.savefig("AlexBoyce_bargraph.png")
    plt.show()



#Line Graph Visualization
def line_graph():
    df = pd.read_csv('student-mat.', sep=';') #open the dataset
    avg_grade_by_age = df.groupby('age')['G3'].mean()

    plt.plot(avg_grade_by_age.index, avg_grade_by_age.values, marker='o', color='orange', linestyle='-')
    plt.xlabel('Age', fontsize=9)
    plt.ylabel('Average Final Grade (G3)' , fontsize=9)
    plt.title('Average Final Grade by Age', fontsize=12)

    #Label points
    for x, y in zip(avg_grade_by_age.index, avg_grade_by_age.values):
        plt.text(x, y + 0.2, f"{y:.1f}", ha='center')

    #cell text
    plt.text(15, max(avg_grade_by_age.values) - 1,"This line graph shows how \nthe final grade (G3) varies by student age.\n"
                                                  "We can see how students aged 20 had much \nhigher final grades compared to their counterparts", fontsize=9)

    plt.grid(True)
    plt.tight_layout()
    plt.savefig("AlexBoyce_linegraph.png")
    plt.show()

#Pie Chart Visualization
def pie_chart():
    #Pie chart to showing different reasons for choosing the school
    df = pd.read_csv('student-mat.csv', sep=';')#open the dataset
    reason_counts = df['reason'].value_counts()
    plt.pie(reason_counts, labels=reason_counts.index, autopct='%1.1f%%')
    plt.title('Reasons for Choosing the School', fontsize=12)

    #cell text
    plt.text(-1.8, -1.3, "This pie chart breaks down why students chose this school.\n"
                       "Here, data shows most students choose this school to take the math course.", fontsize=9)

    plt.axis('equal')
    plt.show()
    plt.savefig("AlexBoyce_piechart.png")



#Box Chart Visualization
def box_chart():
    df = pd.read_csv('student-mat.csv', sep=';') #open the dataset
    grades = [df['G1'], df['G2'], df['G3']]
    plt.boxplot(grades, tick_labels=['G1', 'G2', 'G3'], patch_artist=True,
                boxprops=dict(facecolor='lightgreen', color='black'),
                medianprops=dict(color='red'),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'))

    plt.ylabel('Grades', fontsize=12)
    plt.title('Distribution of Grades (G1, G2, G3)', fontsize=12)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5) #grid lines for y-axis

    #cell text
    plt.text(0.75, 1, "This boxplot shows grade distributions for periods G1 to G3.\n"
                      "Red lines indicate the median, boxes show the IQR.", fontsize=9)

    plt.tight_layout()
    plt.savefig("AlexBoyce_boxchart.png")
    plt.show()



explain_data()
print_data_head()
bar_graph()
line_graph()
pie_chart()
box_chart()

