# PDF Form Filler - Taxes
![Preview](cover.png)
This project automates the process of filling out PDF forms using data from an Excel spreadsheet. The script reads data from an Excel file, processes it, and fills a PDF form with the relevant information.

## Prerequisites

Ensure you have the following Python libraries installed:
- `pandas`
- `numpy`
- `PyPDF2`

You can install these dependencies using pip:
```bash
pip install pandas numpy PyPDF2
```

## Usage

1. **Prepare your Excel file**:
   - Ensure your Excel file (`SampleFile.xlsx`) has the required structure.
   - The script expects the data to be on the 'Sheet1' of the Excel file, starting from the 4th row.

2. **Prepare your PDF form**:
   - The PDF form (`fw8ben.pdf`) should have fields that correspond to the data columns in the Excel file.

3. **Run the script**:
   - Place the Excel file and the PDF form in the same directory as the script.
   - Execute the script:
     ```bash
     python pdf_form_filler.py
     ```

## Script Explanation

- **Data Processing**:
  - Reads data from the Excel file and preprocesses it, including removing unwanted columns and handling missing values.
  - Combines relevant fields to match the PDF form fields.

- **PDF Form Filling**:
  - Reads the original PDF form.
  - Iterates over the rows of the processed data, filling in the corresponding PDF fields.
  - Saves each filled PDF with a filename based on the individual's name.

## Sample Output

The script will generate a series of filled PDF forms, saved with filenames based on the individual's name, such as `JSmithfw8ben.pdf`.

## Customization

- Adjust the Excel reading section to match your specific file structure.
- Modify the field mapping section to correspond to your PDF form's field names.

