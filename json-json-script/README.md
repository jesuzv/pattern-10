# README for json_to_json.py

## Introduction
As an integral part of the "[pattern-10](https://github.com/jesuzv/pattern-10)" project, the `json_to_json.py` script is dedicated to processing and transforming JSON data. This script specifically handles data from Gordon Brander's Observable notebook, [Observable - A Pattern Language](https://observablehq.com/@gordon/a-pattern-language), to create Python-compatible formats.

## Dependencies
- Python 3.x
- json library
- logging module

## Script Description
The `json_to_json.py` script is designed to manage and process `nodesById.json` and `links.json` file formats, with the following key features:

- **Versatile JSON Reading**: Capable of processing various JSON structures for optimal Python compatibility.
- **Python-friendly Data Conversion**: Converts complex JSON data into Python-native formats, making it more accessible for further processing.
- **Enhanced Logging**: Provides detailed logging to facilitate debugging and to track the script's execution process.
- **Custom Error Handling**: Incorporates specific exceptions to handle file read/write errors effectively.
- **JSON File Writing**: Writes the processed data back into JSON files efficiently.
- **Deep Data Comparison**: Performs in-depth comparisons of data structures to validate processing outcomes.
- **Comprehensive JSON File Comparison**: Ensures the integrity of data by comparing the processed files with the original input files.

## Usage
1. Ensure Python 3.x is installed on your system.
2. Download `nodesById.json` and `links.json` from Gordon Brander's [Observable - A Pattern Language](https://observablehq.com/@gordon/a-pattern-language).
3. Place the downloaded files into the `test_case_input` directory within the script folder.
4. Execute the script using `python json_to_json.py`.
5. The script will store the processed files in:
   - `/test_case_output`: Contains the reference test case outputs. Please do not modify these files.
   - `/new_runs_output`: Stores outputs from new script executions.

## Test Case Scenario
The `json_to_json.py` script was rigorously tested with `nodesById.json` and `links.json` sourced from the Observable notebook. To replicate these tests, users should download and place these files in the `test_case_input` directory. The test results are available in the `/test_case_output` directory for reference and comparison purposes, demonstrating the script's ability to maintain data integrity.

## Error Handling
- `FileReadError`: Triggered during file reading complications.
- `FileWriteError`: Activated during issues in the file writing process.

## Contributing
Contributions to the `pattern-10` project are highly appreciated. Please contribute through fork-and-pull request methods.

## License
This script and the broader `pattern-10` project are under [The Unlicense](../LICENSE).
