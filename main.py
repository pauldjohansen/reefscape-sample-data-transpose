import pandas as pd

# Read the original CSV file
df = pd.read_csv('Claude Generated Data - sample_reefscape_data.csv')

# Define the columns to transpose and their new names
teleop_scoring_columns = {
    'coral_l1': 'L1',
    'coral_l2': 'L2',
    'coral_l3': 'L3',
    'coral_l4': 'L4',
    'robot_net_algae': 'Net Algae',
    'human_net_algae': 'Human Algae',
    'processor_algae': 'Processor Algae',
    'human_attempts': 'Human Attempts'
}

auto_scoring_columns = {
    'auto_leave': 'Auto Leave',
    'auto_coral_l1': 'Auto L1',
    'auto_coral_l2': 'Auto L2',
    'auto_coral_l3': 'Auto L3',
    'auto_coral_l4': 'Auto L4',
    'auto_algae': 'Auto Algae'
}

# Create a list to store the transformed data
tele_transformed_data = []
auto_transformed_data = []

# Iterate through each row in the original dataframe
for _, row in df.iterrows():
    # For each scoring column, create a new row
    for old_col, new_name in teleop_scoring_columns.items():
        tele_transformed_data.append({
            'match_number': row['match_number'],
            'team_number': row['team_number'],
            'scoring_type': new_name,
            'scoring_value': row[old_col]
        })

    for old_auto_col, new_auto_name in auto_scoring_columns.items():
        auto_transformed_data.append({
            'match_number': row['match_number'],
            'team_number': row['team_number'],
            'scoring_type': new_auto_name,
            'scoring_value': row[old_auto_col]
        })

# Create new dataframe from transformed data
new_tele_df = pd.DataFrame(tele_transformed_data)
new_auto_df = pd.DataFrame(auto_transformed_data)

# Save to new CSV file
new_tele_df.to_csv('reefscape_sample_scoring_tele_data.csv', index=False)
new_auto_df.to_csv('reefscape_sample_scoring_auto_data.csv', index=False)
