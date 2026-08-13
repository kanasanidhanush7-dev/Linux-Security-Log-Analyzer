import argparse

from log_analyzer import analyze_log
from report_generator import generate_report


report_file = r"C:\Users\kanas\Downloads\report.txt"


def get_arguments():

    parser = argparse.ArgumentParser(
        description="Linux Security Log Analyzer"
    )

    parser.add_argument(
        "--log",
        required=True,
        help="Path to the Linux authentication log file"
    )

    return parser.parse_args()


def main():

    # Get command-line arguments
    args = get_arguments()

    # Get log file path
    log_file = args.log

    result = None

    while True:

        print("\n" + "=" * 50)
        print("       LINUX SECURITY LOG ANALYZER")
        print("=" * 50)

        print("\n1. Analyze Log File")
        print("2. Generate Security Report")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\nAnalyzing log file...")

            result = analyze_log(log_file)

            if result is not None:
                print("\nAnalysis completed successfully!")
            else:
                print("\nAnalysis failed.")

        elif choice == "2":

            if result is None:

                print("\nPlease analyze the log file first.")

            else:

                print("\nGenerating security report...")

                report = generate_report(*result)

                with open(report_file, "w", encoding="utf-8") as file:
                    file.write(report)

                print("\nSecurity report generated successfully!")
                print(f"Report saved to:\n{report_file}")

        elif choice == "3":

            print("\nExiting program...")
            break

        else:

            print("\nInvalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
