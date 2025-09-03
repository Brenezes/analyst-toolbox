**Analyst Toolbox** 🧰
======================

### The Essential Toolkit for Data Analysis

**Analyst Toolbox** is a unified collection of automation tools designed to streamline and enhance the workflow of analysis teams. With a simple and user-friendly interface, this toolkit combines three powerful scripts into a single menu, providing efficient solutions for common data processing and analysis tasks.

**Features** ✨
--------------

| Tool                     | What It Does                                                                            | Why Use It?                                                                                                            |
| ------------------------ | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **1\. PittFixer**        | **Corrects** the count of corrosion events in datasets.                                 | **Ensures data accuracy** by automatically fixing discrepancies in event counts.                                       |
| **2\. ListMPTVO Concat** | **Combines** multiple files of the same extension into a single file.                   | **Simplifies data aggregation**, perfect for merging large volumes of files, such as logs.                             |
| **3\. Near Weld**        | **Filters** anomaly events based on their distance from weld events.                    | **Essential** for pipeline inspection data analysis, allowing you to filter critical data based on proximity to welds. |
| **4\. DefectMatcher**    | **Correlates defects** between two database tables based on spatial and attribute data. | **Provides data validation** for quality control and allows for automated updates to defect records.                   |

> ⏳ *New scripts are under development! Stay tuned for future updates.*

**Installation and Usage** 🚀
-----------------------------

### Prerequisites

-   **Python 3.7+**

-   **Python packages:**  `sqlite3`, `os`, `subprocess`, `sys`.

### How to Set Up

1.  Clone this repository to your local machine.

2.  Install the dependencies with a single command:

    ```
    pip install -r requirements.txt

    ```

3.  Make sure all scripts (`pittfixer.py`, `listmptvoconcat.py`, `near_weld.py`, `defectmatcher.py`) are in the same directory as `menu.py`.

### How to Run

1.  Launch the main tool in your terminal:

    ```
    python menu.py

    ```

2.  An interactive menu will appear. Simply type the number of the tool you want to use.

    ```
    ============================
    ANALYST TOOLBOX - Main Menu
    ============================
    1. Run PittFixer
    2. Run ListMPTVO Concat
    3. Run Near Weld
    4. Run DefectMatcher
    5. Exit
    ============================
    Select an Option:

    ```

3.  Follow the on-screen instructions for each script. For example, for **Near Weld**, you'll enter the database path and the filtering distance.

**Technical Details** ⚙️
------------------------

| Script               | Input                                                                            | Output                                                                 |
| -------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **PittFixer**        | Dataset with corrosion event counts.                                             | Corrected dataset with accurate event counts.                          |
| **ListMPTVO Concat** | Directory containing files of the same extension (e.g., `.vel`, `.ori`, `.mag`). | A single concatenated file.                                            |
| **Near Weld**        | Database path, table name, and distance threshold.                               | Updated database with filtered anomalies.                              |
| **DefectMatcher**    | Database path, main table name, and reference table name.                        | Updated database (optional) and a CSV log file detailing correlations. |

**Contributing** 🤝
-------------------

Ideas, bug reports, or feature requests are very welcome! Feel free to open an issue or submit a pull request.

**License** 📜
--------------

This project is licensed under the [**LICENSE.md**].

**Contact** 📧
--------------

For questions or support, please contact **Breno Menezes**:

-   **Email:**  `brenomearaujo@gmail.com`

-   **GitHub:**  `Brenezes`

> 🎉 **Thank you for using the Analyst Toolbox!** We hope it simplifies your workflow and enhances your productivity.