
# README for data-append-json.py

## Introduction
The `data-append-json.py` script enriches JSON dictionaries within the "[pattern-10](https://github.com/jesuzv/pattern-10)" project by appending data from a TXT file to each Pattern ID. This TXT file contains mappings of Pattern IDs from Christopher Alexander's "A Pattern Language" to asterisk counts, enhancing the data with insights into each pattern's significance.

## Dependencies
- Python 3.x
- Standard Library Modules: os, json

## Script Description
The `data-append-json.py` targets the data located in the [json-json-script/test_case_output](https://github.com/jesuzv/pattern-10/tree/main/json-json-script/test_case_output) subdirectory and appends the asterisk count data from the `patterns_asterisks.txt` file into JSON dictionaries. Its functionalities include:

- **Data Integration**: Merges asterisk prints and counts into JSON dictionaries based on Pattern IDs from "A Pattern Language" by Christopher Alexander.
- **File Processing**: Reads JSON and TXT files, performing data enrichment automatically.
- **Error Handling**: Implements error checks for data integrity and correct file formatting.
- **Data Mapping**: Associates asterisk counts with Pattern IDs efficiently, ensuring data accuracy.
- **Output Management**: Generates an enriched JSON file in a specified output directory for downstream analysis.

## Usage
1. Ensure Python 3.x is installed on your system.
2. Ensure `patternsbyid.json` is located in the `json-json-script/test_case_output` directory and `patterns_asterisks.txt` is in the script's directory.
3. Execute the script within its directory using the command:
   ```bash
   python data-append-json.py
   ```
4. The script will store the processed files in:
   - `/test_case_output`: Contains the reference test case outputs. Please do not modify these files.
   - `/new_runs_output`: Stores outputs from new script executions.

## Test Case Scenario
The `data-append-json.py` script was rigorously tested with the file `patternsbyid.json` located in the `json-json-script/test_case_output` directory and the file `patterns_asterisks.txt` in the script's directory. To replicate these tests, users should maintain the same directory structure or modify the script paths to match the location of the required files. The test results are stored in the `/test_case_output` directory for reference and comparison, demonstrating the script's effectiveness in preserving data integrity.

## Error Handling
The script robustly handles errors to ensure seamless execution, including:
- **File Access Errors**: Detects and alerts on issues accessing or reading input files, guiding users to verify file paths and permissions.
- **Data Integrity Checks**: Implements validations for expected data formats and structures, preventing processing of corrupt or incomplete data sets and advising on corrective actions.
- **Exception Logging**: Captures and logs detailed error information, facilitating efficient troubleshooting and support.
- **User Guidance**: Provides clear, actionable feedback for common issues, helping users to quickly resolve potential obstacles to successful script execution.

These measures are designed to minimize disruptions and assist users in addressing problems that may arise during the script's use.

## Contributing
Contributions to the `pattern-10` project are highly appreciated. Please contribute through fork-and-pull request methods.

## License
Specify the project's license here, ensuring users understand their rights to use, modify, and distribute the script.
