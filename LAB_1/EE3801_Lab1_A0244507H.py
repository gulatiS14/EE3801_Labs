
# Q.1 a


import pandas as pd
from scipy.stats import hmean,gmean
#Q.1 a
bodyfat2 = pd.read_csv('bodyfat2.csv')
bodyfat2_df = pd.DataFrame(bodyfat2)
#bodyparts that need to be used in the body_parts list
body_parts = ["neck","chest","abdomen","hip","thigh","knee","ankle","biceps","forearm","wrist"]

individual_bodyfat_df = pd.DataFrame()
#finding the mean, median and sum of individual bodyfat and store it in a new Data Frame
individual_bodyfat_df["Mean"] = bodyfat2_df[body_parts].mean(axis =1)
individual_bodyfat_df["Median"] = bodyfat2_df[body_parts].median(axis=1)
individual_bodyfat_df["Sum"] = bodyfat2_df[body_parts].sum(axis=1)
individual_bodyfat_df.insert(0, 'ID', individual_bodyfat_df.index)

#print the results of Q.1 a
print("Q.1a The mean, median and sum of the fat present in the body parts for each individual using bodyfat2 dataset is :\n ")
print(pd.concat([individual_bodyfat_df.head(3), individual_bodyfat_df.tail(3)]).to_string(index=False))
print()


# Q.1 b


# saving the features fat: mean, median and sum in a new Data Frame
features_bodyfat_df = pd.DataFrame()
features_bodyfat_df["Mean"] = bodyfat2_df[body_parts].mean()
features_bodyfat_df["Median"] = bodyfat2_df[body_parts].median()
features_bodyfat_df["Sum"] = bodyfat2_df[body_parts].sum()
features_bodyfat_df.insert(0, 'Features', body_parts)

#print the results of Q.1 b
print("Q.1b The mean, median, and sum of fat for each body part is: \n")
print(features_bodyfat_df.to_string(index=False))
print()


# Q.1 c


diff_means_df = pd.DataFrame()
#Calculate the 3 different types of Mean and store it in a Data Fram
diff_means_df["Arithmetic Mean"] = bodyfat2_df[body_parts].mean()
diff_means_df["Geometric Mean"] = gmean(bodyfat2_df[body_parts])
diff_means_df["Harmonic Mean"] = hmean(bodyfat2_df[body_parts])
diff_means_df.insert(0, 'Features', body_parts)

# The Results of 3 different types of mean stored in a Data Frame across dofferent body
print("Q.1c The Results of 3 different types of mean across different bodyparts \n")
print(diff_means_df.to_string(index=False))
print()


# Q.2 a


#exclude features that we don't need and store values in a new data frame
features_exclude = ["age", "weight", "height"]
filt_features = [col for col in bodyfat2_df.columns if col not in features_exclude]

filt_df = bodyfat2_df[filt_features]

max_values_list = []

for column in filt_df.columns:
    # find the Maximum Value & Index; Minimum Value and Index in a List
    max_value = filt_df[column].max()
    max_index = filt_df[column].idxmax() 
    min_value = filt_df[column].min()
    min_index = filt_df[column].idxmin() 
    max_values_list.append((column, max_value, max_index, min_value, min_index))

#Store the List in a New Data Frame; and print the Values
values_df = pd.DataFrame(max_values_list, columns=['Features', 'Max Value', 'Max ID', 'Min Value', 'Min ID'])

print("Q2.a The individuals that have the maximum and minimum fat \n")
print(values_df.to_string(index=False))
print()


# Q.2 b


max_freq_df = {}
min_freq_df = {}
# Find the Max ID that is repeated more than 1 and store features as list
for index, value in values_df['Max ID'].value_counts().items():
    if value > 1:
        max_temp = []
        for i in range(len(values_df["Features"])):
            if(index == values_df["Max ID"].loc[i]):
                max_temp.append(values_df["Features"].loc[i])
        max_freq_df[str(index)] = max_temp

# Find the Min ID that is repeated more than 1 and store features as list
for index, value in values_df['Min ID'].value_counts().items():
    if value > 1:
        min_temp = []
        for i in range(len(values_df["Features"])):
            if(index == values_df["Min ID"].loc[i]):
                min_temp.append(values_df["Features"].loc[i])
        min_freq_df[str(index)] = min_temp

#print the values for Max ID
print("Q.2b The Individuals with Max Id and their features are:\n")
for key_value_pair in max_freq_df.items():
    print("Max ID: "+ key_value_pair[0] + " - Features : " + ', '.join(map(str, key_value_pair[1])))
print()
#print the values for Min ID
print("Q.2b The Individuals with Min Id and their features are:\n")
for key_value_pair in min_freq_df.items():
    print("Min ID: "+ key_value_pair[0] + " - Features : " + ', '.join(map(str, key_value_pair[1])))
print()


# Q.3



result_list = []

for column in bodyfat2_df.columns:
    col_mean = bodyfat2_df[column].mean()
    col_median = bodyfat2_df[column].median()
    col_std = bodyfat2_df[column].std()
    
    # Calculate the range within 10% of standard deviation from the mean and median
    range_mean = (col_mean - 0.1 * col_std, col_mean + 0.1 * col_std)
    range_median = (col_median - 0.1 * col_std, col_median + 0.1 * col_std)
    
    # Count the number of entries within the specified ranges and append it to a list
    count_mean = ((bodyfat2_df[column] >= range_mean[0]) & (bodyfat2_df[column] <= range_mean[1])).sum()
    count_median = ((bodyfat2_df[column] >= range_median[0]) & (bodyfat2_df[column] <= range_median[1])).sum()
    
    result_list.append((column, count_mean, count_median))

#Store the results in a DataFrame and Print its results
result_df = pd.DataFrame(result_list, columns=['Feature', 'Within 10% of Mean', 'Within 10% of Median'])
print("Q.3 number of individuals in each feature that fall within 10% of standard deviation from its respective mean and median :\n")
print(result_df.to_string(index=False))
print()


# Q.4 


bodyfat3 = pd.read_csv('bodyfat3.csv')
#Calculate the missig values
missing_values_count = bodyfat3.isnull().sum()
missing_values_df = pd.DataFrame({'Feature': missing_values_count.index, 'Missing Values Count': missing_values_count.values})
#print the missimg values of null for each feature
print("Q.4 Number of Missing Values in Each Feature:\n")
print(missing_values_df.to_string(index=False))
print()


# Q.5 a


bodyfat3b = bodyfat3.copy() #deep copy in order to not affect the original dataset
bodyfat2_means = bodyfat2.mean()

for column in bodyfat3b.columns:
    feature_mean = bodyfat3b[column].mean()
    
    # Replace missing values with the mean of that feature
    bodyfat3b[column].fillna(feature_mean, inplace=True)

# Calculate the absolute differences in means for each feature
abs_mean_differences = abs(bodyfat2_means - bodyfat3b.mean())

print("Q.5a Absolute Differences in Mean Values (bodyfat3b vs. bodyfat2):\n")
print(abs_mean_differences.to_string())
print()


# Q.5 b


bodyfat3c = bodyfat3.copy() # deep copy in order to not affect the original dataset
bodyfat2_median = bodyfat2.median()

for column in bodyfat3c.columns:
    feature_median = bodyfat3c[column].median()
    
    # Replace missing values with the median of that feature
    bodyfat3c[column].fillna(feature_median, inplace=True)

# Calculate the absolute differences in means for each feature
abs_median_differences = abs(bodyfat2_median - bodyfat3c.median())

print("Q.5b Absolute Differences in Median Values (bodyfat3c vs. bodyfat2):\n")
print(abs_median_differences.to_string())
print()


# Q.5 c 

print("Q.5c The Mean Difference vs The Median Difference:\n")
print(pd.DataFrame({'Feature': abs_mean_differences.index, 'Mean Difference': abs_mean_differences.values, 'Median Difference': abs_median_differences.values}).to_string(index=False))
print()


# Q.6 a


normalized_bodyfat2 = bodyfat2.copy()
for column in bodyfat2.columns:
    mean = bodyfat2[column].mean()
    std = bodyfat2[column].std()
    
    # Normalize the values using the formula: (x - mean) / std
    normalized_bodyfat2[column] = (bodyfat2[column] - mean) / std

#print the top3 and bottom 3 rows
print("Q.6a The top 3 and bottom 3 rows of normalised bodyfat dataframe:\n")
print(pd.concat([normalized_bodyfat2.head(3), normalized_bodyfat2.tail(3)]))
print()


# Q. 6 b

greater_than_mean_counts = (normalized_bodyfat2 > normalized_bodyfat2.mean()).sum()
#print the values greater than mean
print("Q.6b Number of Individuals Greater Than the Respective Feature's Mean:\n")
print(greater_than_mean_counts)

