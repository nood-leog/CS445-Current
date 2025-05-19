#lab5.py

# Data files:
# winequality-red.csv

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

#ignore future warnings
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

#global dataset variable
df = pd.read_csv('winequality-red.csv')

#explain the data
def explain_data():
    print("\n"
          "This dataset contains information about red wine quality.\n"
          "It includes all information about the wine, including chemical properties and quality rating.\n"
          "The dataset contains 11 features in total:\n"
          "fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol,quality\n"

          "Sourced from https://github.com/plotly/datasets/blob/master/winequality-red.csv\n"
          )


#Print a portion of the raw data using head()
def print_data_head():
    # read the dataset
    print(df.head())
    print("\nColumn names:\n", df.columns.tolist(), "\n")


#Visualize Covariance Matrix with Heatmap
def covariance_matrix_heatmap():

    #calculate the covariance matrix
    covariance_matrix_heatmap = df.cov()

    #create a heatmap using seaborn
    plt.figure(figsize=(10, 8))
    sns.heatmap(covariance_matrix_heatmap, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Covariance Matrix Heatmap', fontsize=14)
    plt.savefig('Lab5_Boyce_Heatmap.png')
    plt.show()


#Eigenvalues & Eigenvectors Visualization
def eigenvalues_eigenvectors():
    #calculate the covariance matrix
    covariance_matrix = df.cov()

    #calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    #sort eigenvalues and eigenvectors
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    #plot eigenvalues and eigenvectors
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_eigenvalues, marker='o')
    plt.title('Eigenvalues of Covariance Matrix', fontsize=14)
    plt.xlabel('Index', fontsize=14)
    plt.ylabel('Eigenvalue', fontsize=14)
    plt.grid()
    plt.savefig('Lab5_Boyce_eigenvalues.png')
    plt.show()


#Scree Plot showing cumulative variance explained
def scree_plot():
    #calculate the covariance matrix
    covariance_matrix = df.cov()

    #calculate eigenvalues and eigenvectors
    eigenvalues, _ = np.linalg.eig(covariance_matrix)

    #calculate cumulative variance explained
    cumulative_variance = np.cumsum(eigenvalues) / np.sum(eigenvalues)

    #plot the scree plot
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_variance, marker='o')
    plt.title('Scree Plot of Cumulative Variance Explained', fontsize=14)
    plt.xlabel('Number of Components', fontsize=14)
    plt.ylabel('Cumulative Variance Explained', fontsize=14)
    plt.grid()
    plt.savefig('Lab5_Boyce_ScreePlot.png')
    plt.show()


#2D Scatterplot of your data projected onto the first two principal components, colored by a relevant category or continuous variable.
def scatterplot_2d():
    #calculate the covariance matrix
    covariance_matrix = df.cov()

    #calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    #sort eigenvalues and eigenvectors
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    #project data onto the first two principal components
    projected_data = df.dot(sorted_eigenvectors[:, :2])

    #create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(projected_data.iloc[:, 0], projected_data.iloc[:, 1], c=df['quality'], cmap='viridis', alpha=0.7)
    plt.title('2D Scatterplot of First Two Principal Components', fontsize=14)
    plt.xlabel('First Principal Component', fontsize=14)
    plt.ylabel('Second Principal Component', fontsize=14)
    plt.colorbar(label='Quality')
    plt.grid()
    plt.savefig('Lab5_Boyce_ScatterPlot.png')
    plt.show()



#run PCA and get the loadings
#used for biplot
def run_pca(n_components=2):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)

    #perform PCA
    from sklearn.decomposition import PCA
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)

    #get loadings
    loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

    #get feature names
    feature_names = df.columns.tolist()

    #get quality labels
    y = df['quality'].values

    return X_pca, loadings, feature_names, y

#Biplot overlaying original feature vectors on the 2D projection.
#takes the PCA score, coefficients, labels and y values
def biplot(score, coeff, labels=None, y=None):
    xs = score[:, 0] #first pc
    ys = score[:, 1] #second pc
    n = coeff.shape[0] #number of features

    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(xs, ys, c=y, cmap='viridis', alpha=0.5)
    plt.colorbar(scatter, label='Quality')

    for i in range(n):
        # Plot arrows for feature loadings, scaled for visibility
        plt.arrow(0, 0, coeff[i, 0] * 3, coeff[i, 1] * 3, color='r', alpha=0.7, head_width=0.1)
        if labels is None:
            plt.text(coeff[i, 0] * 3.2, coeff[i, 1] * 3.2, f"Var{i+1}", color='r', ha='center', va='center')
        else:
            plt.text(coeff[i, 0] * 3.2, coeff[i, 1] * 3.2, labels[i], color='r', ha='center', va='center')

    plt.xlabel("PC1", fontsize=14)
    plt.ylabel("PC2", fontsize=14)
    plt.title("Biplot", fontsize=14)
    plt.grid(True)
    plt.savefig('Lab5_Boyce_Biplot.png')
    plt.show()



print_data_head()
explain_data()

covariance_matrix_heatmap() #1
eigenvalues_eigenvectors() #2
scree_plot() #3
scatterplot_2d() #4

#5
X_pca_2d, loadings, feature_names, y = run_pca(n_components=2)
biplot(X_pca_2d, loadings, labels=feature_names, y=y)