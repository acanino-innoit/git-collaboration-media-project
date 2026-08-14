# Media Metrics Mini Project

Small Python project for learning Git while practicing a simple data analysis workflow.

The project reads advertising campaign data for a fictional media company, calculates a simple profit column with pandas, and exports the result to an Excel file.

## Project Structure

```text
analysis_code/
+-- .env
+-- .gitignore
+-- README.md
+-- requirements.txt
+-- data/
|   +-- media_campaigns.csv
|   +-- data_dictionary.md
+-- outputs/
+-- src/
    +-- analyze_media.py
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the analysis:

```powershell
python src/analyze_media.py
```

The script creates an Excel file with a timestamp:

```text
outputs/output_YYYYMMDD_HHMMSS.xlsx
```

## Git Practice Ideas

1. Create a first commit with the initial project.
2. Change one value in `data/media_campaigns.csv` and inspect the diff.
3. Add a new campaign row and commit it.
4. Create a branch that adds a new statistic.
5. Merge the branch back into `main`.
6. Practice ignoring generated output files with `.gitignore`.
