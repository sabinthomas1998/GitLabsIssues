import pandas as pd
import requests

# Configuration
GITLAB_URL = "https://gitlab.com"  
PROJECT_ID = "*****9" 
PRIVATE_TOKEN = "********"  

# File path to the Excel file
EXCEL_FILE = "issues.xlsx"  

# Read the Excel file
def read_issues_from_excel(file_path):
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

# Create an issue in GitLab
def create_gitlab_issue(issue_data):
    url = f"{GITLAB_URL}/api/v4/projects/{PROJECT_ID}/issues"
    headers = {"PRIVATE-TOKEN": PRIVATE_TOKEN}
    payload = {
        "title": issue_data.get("Title"),
        "description": issue_data.get("Description", ""),
        "labels": issue_data.get("Labels", ""),
    }
    print("Payload:", payload)  # Debug payload
    response = requests.post(url, headers=headers, json=payload)
    print(f"Response status: {response.status_code}")

def main():
    
    issues = read_issues_from_excel(EXCEL_FILE)
    if issues is None:
        return
    
    
    for _, row in issues.iterrows():
        create_gitlab_issue(row)

if __name__ == "__main__":
    main()
