import numpy as np
import pandas as pd


def test1():
    heightsA = [176.2,158.4,167.6,156.2,161.4]
    heights_A = pd.Series(heightsA, index=['s1','s2','s3','s4','s5'])
    print(heights_A[1])
    print(heights_A[1:4])
    weightsA = [85.1,90.2,76.8,80.4,78.9]
    weights_A = pd.Series(weightsA, index=['s1','s2','s3','s4','s5'])
    df_A = pd.DataFrame()
    df_A['Student_height'] = heights_A
    df_A['Student_weight'] = weights_A
    height = df_A['Student_height']
    print(type(height))
    df_s1s2 = df_A.loc[['s1','s2']]
    print(df_s1s2)
    df_s2s5s1 = df_A.loc[['s2','s5','s1']]
    print(df_s2s5s1)
    df_s1s4 = df_A.loc[(df_A.index.str.endswith('1')) | (df_A.index.str.endswith('4'))]
    print(df_s1s4)


def test2():
    # Write your code here
    heightsA = [176.2, 158.4, 167.6, 156.2, 161.4]
    heights_A = pd.Series(heightsA, index=['s1', 's2', 's3', 's4', 's5'])
    weightsA = [85.1, 90.2, 76.8, 80.4, 78.9]
    weights_A = pd.Series(weightsA, index=['s1', 's2', 's3', 's4', 's5'])
    df_A = pd.DataFrame()
    df_A['Student_height'] = heights_A
    df_A['Student_weight'] = weights_A
    df_A.to_csv('classA.csv')
    df_A2 = pd.read_csv('classA.csv')
    print(df_A2)
    df_A3 = pd.read_csv('classA.csv', index_col=0)
    print(df_A3)
    np.random.seed(100)
    heights_B = pd.Series(np.random.normal(loc=170.0, scale=25.0, size=5), index=['s1', 's2', 's3', 's4', 's5'])
    weights_B = pd.Series(np.random.normal(loc=75.0, scale=12.0, size=5), index=['s1', 's2', 's3', 's4', 's5'])
    df_B = pd.DataFrame()
    df_B['Student_height'] = heights_B
    df_B['Student_weight'] = weights_B
    df_B.to_csv('classB.csv', index=False)
    df_B2 = pd.read_csv('classB.csv')
    print(df_B2)
    df_B3 = pd.read_csv('classB.csv', header=None)
    print(df_B3)
    df_B4 = pd.read_csv('classB.csv', header=None, skiprows=2)
    print(df_B4)


def test3():
    dates = pd.date_range(start='1-Sep-2017', end='15-Sep-2017')
    print(dates[2])
    datelist = ['14-Sep-2017', '9-Sep-2017']
    dates_to_be_searched = pd.to_datetime(datelist)
    print(dates_to_be_searched)
    print(dates_to_be_searched.isin(dates))
    arraylist = [['classA'] * 5 + ['classB'] * 5, ['s1', 's2', 's3', 's4', 's5'] * 2]
    mi_index = pd.MultiIndex.from_product(arraylist, names=['First Level', 'Second Level'])
    print(mi_index.levels)


def test4():
    # Write your code here
    import pandas as pd
    import numpy as np

    heightsA = [176.2, 158.4, 167.6, 156.2, 161.4]
    heights_A = pd.Series(heightsA, index=['s1', 's2', 's3', 's4', 's5'])
    weightsA = [85.1, 90.2, 76.8, 80.4, 78.9]
    weights_A = pd.Series(weightsA, index=['s1', 's2', 's3', 's4', 's5'])
    df_A = pd.DataFrame()
    df_A['Student_height'] = heights_A
    df_A['Student_weight'] = weights_A
    df_A_filter1 = df_A[(df_A.Student_height > 160) & (df_A.Student_weight < 80)]
    print(df_A_filter1)
    df_A_filter2 = df_A[df_A.index.str.endswith('5')]
    print(df_A_filter2)
    df_A['Gender'] = ['M', 'F', 'M', 'M', 'F']
    df_groups = df_A.groupby('Gender')
    print(df_groups.mean())
