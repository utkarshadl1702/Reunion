import pandas as pd

# Load the data from the provided Excel file
data = pd.read_excel('Time_Series.xlsx')

# Sort the data by bot_id and timestamp to ensure data is in chronological order
data.sort_values(by=['bot_id', 'timestamp'], inplace=True)

# Initialize variables to keep track of the current bot and work period
current_bot = None
work_start = None
work_end = None
activities = []

# Lists to store the aggregated results
bot_ids = []
work_periods = []
activity_arrays = []

# Function to process and store the work period
def store_work_period(bot_id, start, end, activities):
    bot_ids.append(bot_id)
    work_periods.append((start, end))
    activity_arrays.append(activities)

# Loop through each row in the data
for index, row in data.iterrows():
    bot_id = row['bot_id']
    activity = row['activity']
    timestamp = row['timestamp']

    if current_bot is None:
        current_bot = bot_id
        work_start = timestamp
        work_end = timestamp
        activities.append(activity)
    elif current_bot == bot_id:
        # If the bot_id is the same as the current bot, update the work_end and add the activity
        work_end = timestamp
        activities.append(activity)
    else:
        # If the bot_id is different, store the current work period and start a new one
        store_work_period(current_bot, work_start, work_end, activities)
        current_bot = bot_id
        work_start = timestamp
        work_end = timestamp
        activities = [activity]

# Store the last work period
store_work_period(current_bot, work_start, work_end, activities)

# Create a DataFrame to display the results
result_df = pd.DataFrame({
    'Bot ID': bot_ids,
    'Work Period': work_periods,
    'Activities': activity_arrays
})

print(result_df)
