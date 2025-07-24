# DICOM Patient ID Tool

This script helps people add patient ID information to DICOM files when the original files do not have this information.

## Features

- Command-line interface for easy use
- Batch processing of multiple DICOM files
- Automatic output directory creation
- Comprehensive error handling
- Progress tracking during processing

## Installation

1. Clone this repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Interface

```bash
python3 dicom_patientid.py -i INPUT_DIR -o OUTPUT_DIR -n "PATIENT_NAME" -id "PATIENT_ID"
```

### Arguments

- `-i, --input-dir`: Directory containing DICOM files to process (required)
- `-o, --output-dir`: Directory where processed files will be saved (required)
- `-n, --patient-name`: Patient name to add to DICOM files (required)
- `-id, --patient-id`: Patient ID to add to DICOM files (required)
- `--version`: Show program version
- `-h, --help`: Show help message

### Examples

```bash
# Process DICOM files with patient information
python3 dicom_patientid.py -i ./input_dicom_files -o ./output_dicom_files -n "John Doe" -id "12345"

# Using long form arguments
python3 dicom_patientid.py --input-dir /path/to/dicom --output-dir /path/to/output --patient-name "Jane Smith" --patient-id "67890"
```

### Output

The tool will:
1. Validate that the input directory exists
2. Create the output directory if it doesn't exist
3. Process each file in the input directory
4. Add the specified patient name and ID to each DICOM file
5. Save the processed files to the output directory
6. Report the number of files processed successfully

## Error Handling

The tool includes comprehensive error handling for:
- Missing input directories
- Invalid DICOM files
- File permission issues
- Empty directories

## Requirements

- Python 3.6 or higher
- pydicom library (see requirements.txt)