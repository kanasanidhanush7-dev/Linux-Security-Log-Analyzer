import argparse

from log_analyzer import analyze_log
from report_generator import generate_report


report_file = "report.txt"


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

    args = get_arguments()

    log_file = args.log
    result = None

    while True:

        print("\n" + "=" * 50)
        print("       LINUX SECURITY LOG ANALYZER")
        print("=" * 50)

        print("\n1. Analyze Sample Log")
        print("2. Analyze Real Ubuntu Log")
        print("3. Generate Security Report")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\nAnalyzing sample log file...")

            result = analyze_log(log_file)

            if result is not None:
                print("\nSample log analysis completed successfully!")
            else:
                print("\nAnalysis failed.")

        elif choice == "2":

            real_log = "/var/log/auth.log"

            print("\nAnalyzing real Ubuntu authentication log...")
            print(f"Log file: {real_log}")

            result = analyze_log(real_log)

            if result is not None:
                print("\nReal Ubuntu log analysis completed successfully!")
            else:
                print("\nAnalysis failed.")

        elif choice == "3":

            if result is None:

                print("\nPlease analyze a log file first.")

            else:

                print("\nGenerating security report...")

                report = generate_report(*result)

                with open(report_file, "w", encoding="utf-8") as file:
                    file.write(report)

                print("\nSecurity report generated successfully!")
                print(f"Report saved to:\n{report_file}")

        elif choice == "4":

            print("\nExiting program...")
            break

        else:

            print("\nInvalid choice! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
