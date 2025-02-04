## Analyst Toolbox ##
Welcome to the Analyst Toolbox, a unified collection of automation tools designed to streamline and enhance the workflow of analysis teams. This toolbox combines three powerful scripts into a single, easy-to-use menu-driven interface, providing efficient solutions for common tasks in data analysis and processing.

Features
1. PittFixer
Purpose: Corrects the quantity of corrosion events in datasets.

Functionality: Automates the identification and correction of discrepancies in corrosion event counts, ensuring data accuracy and consistency.

Use Case: Ideal for datasets where corrosion event counts need to be validated and standardized.

2. ListMPTVO Concat
Purpose: Concatenates LISTMPTVO files of the same extension within a directory.

Functionality: Combines multiple files (.vel, .ori, .mag) into a single file, simplifying data aggregation and analysis.

Use Case: Perfect for merging large datasets or log files stored in separate files.

3. Near Weld
Purpose: Filters anomaly events based on their distance from weld events.

Functionality: Allows users to define a distance threshold (in millimeters) to filter anomalies near weld events. The script dynamically updates the database based on the user's input.

Use Case: Essential for analyzing pipeline inspection data, where the proximity of anomalies to welds is critical.

4. Future Scripts
   Soon

## Installation ##
Prerequisites:

Python 3.7 or higher.

Required Python packages: sqlite3, os, subprocess, sys.

Setup:

Clone or download the repository.

Install dependencies (if any) using:

bash
Copy
pip install -r requirements.txt
Configuration:

Ensure all scripts (pittfixer.py, listmptvoconcat.py, near_weld.py) are in the same directory as menu.py.

Modify the database paths or file directories in the scripts as needed.

Usage
Run the Toolbox:

Execute the main menu script:

bash
Copy
python menu.py
Main Menu:

The toolbox provides a user-friendly menu with the following options:

Copy
============================
ANALYST TOOLBOX - Main Menu
============================
1. Run PittFixer
2. Run ListMPTVO Concat
3. Run Near Weld
4. Exit
============================
Select an Option:

Choose the desired tool by entering the corresponding number.

Follow the on-screen instructions for each tool:

PittFixer: Input the dataset path and let the script correct corrosion event counts.

ListMPTVO Concat: Provide the directory path and file extension to concatenate files.

Near Weld: Enter the database path, table name, and distance threshold to filter anomalies near welds.

Exit:

Select option 8 to exit the toolbox.

Script Details
PittFixer
Input: Dataset with corrosion event counts.

Output: Corrected dataset with accurate event counts.

Key Features:

Automated validation of event counts.

Logs discrepancies for review.

ListMPTVO Concat
Input: Directory containing files of the same extension.

Output: A single concatenated file.

Key Features:

Supports multiple file types (.vel, .ori, .mag).

Preserves file headers and structure.

Near Weld
Input: Database path, table name, and distance threshold.

Output: Updated database with filtered anomalies.

Key Features:

Dynamic distance filtering.

SQL-based updates for efficiency.

Contributing
Contributions to the Analyst Toolbox are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

License
This project is licensed. See the LICENSE file for details.

Contact
For questions or support, please contact:
Your Name
Email: breno.araujo@pipeway.com
GitHub: Brenezes

Thank you for using the Analyst Toolbox! We hope it simplifies your workflow and enhances your productivity. 🚀
