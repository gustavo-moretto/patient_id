#!/usr/bin/env python3
"""
DICOM Patient ID Tool

This script adds patient ID information to DICOM files that are missing this data.
"""

import pydicom
import os
import argparse
import sys
from pathlib import Path


def process_dicom_files(input_dir, output_dir, patient_name, patient_id):
    """
    Process DICOM files by adding patient name and ID.
    
    Args:
        input_dir (str): Directory containing DICOM files to process
        output_dir (str): Directory where processed files will be saved
        patient_name (str): Patient name to add to DICOM files
        patient_id (str): Patient ID to add to DICOM files
    
    Returns:
        int: Number of files processed successfully
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Validate input directory exists
    if not input_path.exists():
        print(f"Error: Input directory '{input_dir}' does not exist.")
        return 0
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Get list of files in input directory
    try:
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    except OSError as e:
        print(f"Error reading input directory: {e}")
        return 0
    
    if not files:
        print(f"No files found in input directory '{input_dir}'.")
        return 0
    
    print(f"Found {len(files)} files to process...")
    
    processed_count = 0
    
    # Process each file
    for count, filename in enumerate(files):
        try:
            print(f"Processing file {count + 1}/{len(files)}: {filename}")
            
            input_file = input_path / filename
            output_file = output_path / filename
            
            # Read DICOM file
            dataset = pydicom.dcmread(str(input_file), force=True)
            
            # Add patient information
            dataset.PatientName = patient_name
            dataset.PatientID = patient_id
            
            # Save processed file
            dataset.save_as(str(output_file))
            processed_count += 1
            
        except Exception as e:
            print(f"Error processing file '{filename}': {e}")
            continue
    
    return processed_count


def main():
    """Main function with command-line interface."""
    parser = argparse.ArgumentParser(
        description="Add patient ID information to DICOM files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -i ./input_dicom_files -o ./output_dicom_files -n "John Doe" -id "12345"
  %(prog)s --input-dir /path/to/dicom --output-dir /path/to/output --patient-name "Jane Smith" --patient-id "67890"
        """
    )
    
    parser.add_argument(
        '-i', '--input-dir',
        required=True,
        help='Directory containing DICOM files to process'
    )
    
    parser.add_argument(
        '-o', '--output-dir',
        required=True,
        help='Directory where processed DICOM files will be saved'
    )
    
    parser.add_argument(
        '-n', '--patient-name',
        required=True,
        help='Patient name to add to DICOM files'
    )
    
    parser.add_argument(
        '-id', '--patient-id',
        required=True,
        help='Patient ID to add to DICOM files'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    args = parser.parse_args()
    
    print("DICOM Patient ID Tool")
    print("=" * 40)
    print(f"Input directory: {args.input_dir}")
    print(f"Output directory: {args.output_dir}")
    print(f"Patient name: {args.patient_name}")
    print(f"Patient ID: {args.patient_id}")
    print("=" * 40)
    
    # Process the files
    processed = process_dicom_files(
        args.input_dir,
        args.output_dir,
        args.patient_name,
        args.patient_id
    )
    
    if processed > 0:
        print(f"\nSuccess! Processed {processed} files.")
        print(f"Output files saved to: {args.output_dir}")
    else:
        print("\nNo files were processed.")
        sys.exit(1)


if __name__ == "__main__":
    main()