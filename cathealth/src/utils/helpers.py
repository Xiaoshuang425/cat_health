# Utility functions
import datetime

def get_timestamp():
    """
    Returns the current timestamp in a readable format.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_analysis_report(report_data, filename="report.txt"):
    """
    Saves the health analysis report to a file.
    Args:
        report_data (dict): The analysis report data.
        filename (str): The name of the file to save the report.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"--- Report Generated: {get_timestamp()} ---\n")
        f.write(f"Overall Status: {report_data.get('overall_status')}\n")
        f.write(f"Severity: {report_data.get('severity')}\n")
        f.write("Recommendations:\n")
        for rec in report_data.get('recommendations', []):
            f.write(f"- {rec}\n")
        f.write("\n")
    print(f"Analysis report saved to {filename}")

# You can add more utility functions here as needed, e.g., image preprocessing, data logging, etc.