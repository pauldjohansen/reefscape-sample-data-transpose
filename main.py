import pandas as pd

# Read the original CSV file
df = pd.read_csv('sample_reefscape_data.csv')

# Define the columns to transpose and their new names
scoring_columns = {
    'coral_l1': 'L1',
    'coral_l2': 'L2',
    'coral_l3': 'L3',
    'coral_l4': 'L4',
    'robot_net_algae': 'Net Algae',
    'processor_algae': 'Processor Algae'
}

# Create a list to store the transformed data
transformed_data = []

# Iterate through each row in the original dataframe
for _, row in df.iterrows():
    # For each scoring column, create a new row
    for old_col, new_name in scoring_columns.items():
        transformed_data.append({
            'match_number': row['match_number'],
            'team_number': row['team_number'],
            'scoring_type': new_name,
            'scoring_value': row[old_col]
        })

# Create new dataframe from transformed data
new_df = pd.DataFrame(transformed_data)

# Save to new CSV file
new_df.to_csv('reefscape_sample_scoring_data.csv', index=False)