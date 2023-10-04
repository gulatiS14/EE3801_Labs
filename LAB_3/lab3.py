import pandas as pd
import sys

#Q 2.

def filter_csv(file_name, item, element):
    try:
        input_df = pd.read_csv(file_name, encoding='unicode_escape')
        filtered_data = input_df[(input_df['Item'] == item) & (input_df['Element'] == element)]
        return filtered_data
    except FileNotFoundError:
        return None
    
def calculate_max_and_median(df):    
    # Convert 'Value' column to numeric
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    df = df.dropna(how='any') # to drop any Nan Values
    
    # Find the year with maximum values and the respective values
    max_values_df = df.groupby(['Area', 'Item'])[['Year', 'Value']].apply(lambda x: x.loc[x['Value'].idxmax()]).reset_index()
    
    # Calculate median values throughout the years
    median_values_df = df.groupby(['Area', 'Item'])['Value'].median().reset_index()
    
    return max_values_df, median_values_df

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python lab3.py <file_name> <item> <element>")
        sys.exit(1)

    file_name = sys.argv[1]
    item = sys.argv[2]
    element = sys.argv[3]
    
    result = filter_csv(file_name, item, element)
    
    if result is not None and not result.empty:
        countries_with_nan = result[result.isna().any(axis=1)]['Area'].unique().tolist()
        # print(countries_with_nan) to print the countries with NaN values

        result = result[~result['Area'].isin(countries_with_nan)].reset_index()
        max_values_df, median_values_df = calculate_max_and_median(result)
        result_item_prod_df = pd.merge(max_values_df, median_values_df, on=['Area', 'Item'], how='inner')
        result_item_prod_df.rename(columns={'Year': 'Year', 'Value_x': 'Maximum Values', 'Value_y': 'Median'}, inplace=True)
        
        
        result_df = result_item_prod_df.drop(columns=['Item'])
        
        output_filename = f"output_{item}_{element}.csv"
        
        # Save the result dataframe as a CSV file locally
        result_df.to_csv(output_filename, index=False)

    else:
        print("File not found or no matching data found.")

