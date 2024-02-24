import json
import os

def update_patterns_with_asterisks(json_file_path, txt_file_path, output_json_path):
    """
    Updates the patterns JSON data with asterisks information from a text file.
    
    Parameters:
    - json_file_path: Path to the original JSON file.
    - txt_file_path: Path to the text file containing asterisks data.
    - output_json_path: Path for saving the updated JSON data.
    """
    print("Loading JSON data...")
    with open(json_file_path, 'r') as file:
        patterns_data = json.load(file)
    # Transform to include a dictionary for description
    patterns_data = {pid: {'Description': desc} for pid, desc in patterns_data.items()}
    
    print("Loading and parsing data to append...")
    with open(txt_file_path, 'r', newline='') as file:
        next(file)  # Skip header line
        asterisks_data = [line.strip() for line in file if line.strip()]

    asterisks_dict = {}
    for line in asterisks_data:
        parts = line.split(',')
        pattern_id = parts[0].strip()
        asterisks_print = parts[1].strip() if len(parts) > 1 else ''
        asterisks_count = asterisks_print.count('*')
        asterisks_dict[pattern_id] = {'AsterisksPrint': asterisks_print, 'AsterisksCount': asterisks_count}

    print("Appending data to  the original JSON data...")
    for pattern_id, asterisk_info in asterisks_dict.items():
        if pattern_id in patterns_data:
            patterns_data[pattern_id]['Asterisks'] = asterisk_info
        else:
            print(f"No original data for pattern ID {pattern_id}.")

    print("Saving updated JSON data...")
    with open(output_json_path, 'w') as file:
        json.dump(patterns_data, file, indent=4)
    print("Data append complete.")

# Define file paths relative to the script location for modularity
script_dir = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(script_dir, '../json-json-script/test_case_output/patternsbyid.json')
txt_file_path = os.path.join(script_dir, 'patterns_asterisks.txt')
# Adjust the output path to match the specified directory
output_json_path = os.path.join(script_dir, 'new_runs_output/patternsbyid_asterisks.json')

update_patterns_with_asterisks(json_file_path, txt_file_path, output_json_path)
