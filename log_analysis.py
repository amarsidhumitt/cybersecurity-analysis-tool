# Simple Log Analysis Script

def analyze_log(file_name):
    try:
        with open(file_name, "r") as log_file:
            print("Scanning log file...\n")

            for line in log_file:
                if "Failed password" in line:
                    print("Potential brute-force attack detected:")
                    print(line.strip())

                elif "ERROR" in line:
                    print("System error found:")
                    print(line.strip())

                elif "WARNING" in line:
                    print("Warning message:")
                    print(line.strip())

    except FileNotFoundError:
        print("Log file not found.")

analyze_log("sample.log")
