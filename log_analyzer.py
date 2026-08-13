import re


def analyze_log(log_file):

    ip_counts = {}
    failed_attempts = 0
    ip_addresses = []
    usernames = []
    timestamps = []
    security_events = []
    errors = []
    warnings = []

    try:

        with open(log_file, "r", encoding="utf-8") as file:

            for line in file:

                if "Failed password" in line:

                    failed_attempts += 1

                    timestamp_value = "Unknown"
                    ip_address = "Unknown"
                    username = "Unknown"

                    # Extract timestamp
                    timestamp = re.search(
                        r"^(\w{3} \d{2} \d{2}:\d{2}:\d{2})",
                        line
                    )

                    if timestamp:
                        timestamp_value = timestamp.group(1)
                        timestamps.append(timestamp_value)

                    # Extract IP address
                    ip = re.search(
                        r"from (\d+\.\d+\.\d+\.\d+)",
                        line
                    )

                    if ip:
                        ip_address = ip.group(1)

                        ip_addresses.append(ip_address)

                        if ip_address in ip_counts:
                            ip_counts[ip_address] += 1
                        else:
                            ip_counts[ip_address] = 1

                    # Extract username
                    user = re.search(
                        r"Failed password for (?:user )?(\w+)",
                        line
                    )

                    if user:
                        username = user.group(1)
                        usernames.append(username)

                    # Security event
                    event = {
                        "timestamp": timestamp_value,
                        "ip": ip_address,
                        "username": username
                    }

                    security_events.append(event)

                # Detect errors
                if "error" in line.lower():
                    errors.append(line.strip())

                # Detect warnings
                if "warning" in line.lower():
                    warnings.append(line.strip())

    except FileNotFoundError:

        print("\nERROR: Log file not found.")
        return None

    except PermissionError:

        print("\nERROR: Permission denied while reading log file.")
        return None

    except Exception as e:

        print(f"\nERROR: {e}")
        return None

    return (
        ip_counts,
        failed_attempts,
        ip_addresses,
        usernames,
        timestamps,
        security_events,
        errors,
        warnings
    )
