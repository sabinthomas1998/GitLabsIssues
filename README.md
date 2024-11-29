# GitLab Issue Creation Using Python

This repository contains a Python script to automate the creation of issues in a GitLab project by reading issue data from an Excel file.

---

## Prerequisites

1. **Python 3.6+**:
   - Ensure you have Python installed on your system. Download it [here](https://www.python.org/downloads/).

2. **Required Python Libraries**:
   - Install the dependencies using:
     ```bash
     pip install pandas requests openpyxl
     ```

3. **GitLab Personal Access Token**:
   - Generate a token in GitLab with the `api` scope.
     - Go to **User Settings** → **Access Tokens** → Create a token.

4. **Project ID**:
   - Locate your project ID in GitLab:
     - Go to the project page.
     - The project ID is visible in the URL or under **Settings > General**.

5. **Excel File**:
   - Prepare an Excel file (`issues.xlsx`) with the following columns:
     - **Title**: The issue's title (required).
     - **Description**: A description of the issue (optional).
     - **Labels**: Comma-separated labels (optional).

---

## How to Use

1. **Clone the Repository**:
   - Clone this repository or download the script file.

2. **Set Up Environment Variables**:
   - Replace the following placeholders in the script with your details:
     ```python
     GITLAB_URL = "https://gitlab.com"  # Base URL of your GitLab instance
     PRIVATE_TOKEN = "your_personal_access_token"  # Your GitLab API token
     PROJECT_ID = "your_project_id"  # ID of the project where issues will be created
     ```

3. **Run the Script**:
   - Place your `issues.xlsx` file in the same directory as the script.
   - Run the script:
     ```bash
     python create_issues.py
     ```

4. **Verify Issues**:
   - Check the **Issues** section in your GitLab project to confirm the issues were created.

---

## Script Overview

The script reads an Excel file (`issues.xlsx`) and sends POST requests to the GitLab API to create issues.

### Core Functions
- **`read_excel(file_path)`**:
  Reads the Excel file and returns a list of dictionaries containing issue data.

- **`create_gitlab_issue(issue_data)`**:
  Sends a POST request to the GitLab API to create an issue.

### Example Payload Sent to GitLab
```json
{
   "title": "Test Issue",
   "description": "This is a description.",
   "labels": "bug,feature"
}
