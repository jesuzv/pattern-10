import json
import logging
import os
from typing import Dict, Tuple, Union, Any, List

# Enhanced logging setup for better debugging and information tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom exceptions for specific error scenarios to provide more detailed error information
class FileReadError(Exception):
    """Exception raised for errors in the file reading process."""
    pass

class FileWriteError(Exception):
    """Exception raised for errors in the file writing process."""
    pass

def read_json(file_path: str) -> Union[Dict, List, Any]:
    """
    Reads a JSON file from the given file path and returns its contents.
    Raises FileReadError for file-related issues.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        message = f"File not found: {file_path}"
        logging.error(message)
        raise FileReadError(message)
    except json.JSONDecodeError:
        message = f"Invalid JSON: {file_path}"
        logging.error(message)
        raise FileReadError(message)

def convert_to_dict(data: Union[Dict, List]) -> Dict:
    """
    Converts a list of lists or tuples, or a dictionary with string keys,
    into a dictionary with integer keys. Logs a warning for conversion issues.
    """
    converted_dict = {}

    if isinstance(data, list):
        for item in data:
            if isinstance(item, (list, tuple)) and len(item) == 2:
                try:
                    key, value = item
                    converted_dict[int(key)] = value
                except ValueError:
                    logging.warning(f"Invalid key format, expected integer: {item[0]}")
            else:
                logging.warning(f"Skipping non-list or improperly sized list element: {item}")

    elif isinstance(data, dict):
        for key, value in data.items():
            try:
                converted_dict[int(key)] = value
            except ValueError:
                logging.warning(f"Invalid key format in dict, expected integer: {key}")

    return converted_dict

def write_to_json(data: Dict, filename: str):
    """
    Writes a dictionary to a JSON file with the specified filename.
    Raises FileWriteError for file write issues.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        message = f"Error writing to file {filename}: {e}"
        logging.error(message)
        raise FileWriteError(message)
    
def deep_compare(obj1: Any, obj2: Any, level: int = 0) -> bool:
    """
    Recursively compares two objects, handling dictionaries, lists, sets, and primitive data types.
    Logs mismatches at various levels for detailed debugging.
    """
    indent = ' ' * level
    result = True

    if isinstance(obj1, dict) and isinstance(obj2, dict):
        keys1, keys2 = set(obj1.keys()), set(obj2.keys())
        if keys1 != keys2:
            missing_in_obj2 = keys1 - keys2
            missing_in_obj1 = keys2 - keys1
            if missing_in_obj2:
                logging.warning(f"{indent}Keys missing in second object: {missing_in_obj2}")
            if missing_in_obj1:
                logging.warning(f"{indent}Keys missing in first object: {missing_in_obj1}")
            result = False  # Continue the comparison to find other possible mismatches

        for key in keys1.intersection(keys2):
            if not deep_compare(obj1[key], obj2[key], level + 1):
                logging.warning(f"{indent}Mismatch at key '{key}'")
                result = False
        return result

    elif isinstance(obj1, list) and isinstance(obj2, list):
        if len(obj1) != len(obj2):
            logging.warning(f"{indent}List length mismatch.")
            return False

        for i, (item1, item2) in enumerate(zip(obj1, obj2)):
            if not deep_compare(item1, item2, level + 1):
                logging.warning(f"{indent}Mismatch at index {i}.")
                result = False
        return result

    else:
        if obj1 != obj2:
            logging.warning(f"{indent}Value mismatch at level {level}: {obj1} != {obj2}")
            return False
        return True

def compare_json_files(file1: str, file2: str) -> Tuple[bool, int]:
    """
    Compares two JSON files to check if they are identical.
    Returns a tuple containing the comparison result and the number of items compared.
    """
    data1 = read_json(file1)
    data2 = read_json(file2)
    if data1 is None or data2 is None:
        logging.error("One or both files could not be read, comparison aborted.")
        return False, 0

    data1 = convert_to_dict(data1)
    data2 = convert_to_dict(data2)

    comparison_result = deep_compare(data1, data2)
    count = len(data1)

    return comparison_result, count

script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, 'test_case_input')
output_dir = os.path.join(script_dir, 'new_runs_output')

def main():
    logging.info("Starting script execution...")
    try:
        nodes_file = os.path.join(input_dir, 'nodesById.json')
        links_file = os.path.join(input_dir, 'links.json')
        logging.info(f"Reading {nodes_file}")
        nodes_data = read_json(nodes_file)
        nodes_data = convert_to_dict(nodes_data)
        write_to_json(nodes_data, os.path.join(output_dir, 'nodesById_processed.json'))

        logging.info(f"Reading {links_file}")
        links_data = read_json(links_file)
        links_data = convert_to_dict(links_data)
        write_to_json(links_data, os.path.join(output_dir, 'links_processed.json'))

        logging.info("Comparing processed files with original files...")
        nodes_comparison, _ = compare_json_files(nodes_file, os.path.join(output_dir, 'nodesById_processed.json'))
        links_comparison, _ = compare_json_files(links_file, os.path.join(output_dir, 'links_processed.json'))
        logging.info(f'Nodes Comparison with Original: {nodes_comparison}')
        logging.info(f'Links Comparison with Original: {links_comparison}')

    except FileReadError as e:
        logging.error(e)
    except FileWriteError as e:
        logging.error(e)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    logging.info("Script execution completed.")

if __name__ == "__main__":
    main()