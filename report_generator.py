def generate_report(
    ip_counts,
    failed_attempts,
    ip_addresses,
    usernames,
    timestamps,
    security_events,
    errors,
    warnings
):

    report = ""

    report += "=" * 60 + "\n"
    report += "              LINUX SECURITY LOG REPORT\n"
    report += "=" * 60 + "\n\n"

    # 1. Failed SSH attempts
    report += "1. FAILED SSH LOGIN ATTEMPTS\n"
    report += "-" * 60 + "\n"
    report += f"Total Failed Attempts: {failed_attempts}\n\n"

    # 2. IP addresses
    report += "2. IP ADDRESSES\n"
    report += "-" * 60 + "\n"

    for ip in ip_addresses:
        report += f"{ip}\n"

    # 3. IP attack frequency
    report += "\n3. IP ATTACK FREQUENCY\n"
    report += "-" * 60 + "\n"

    for ip, count in ip_counts.items():
        report += f"{ip} -> {count} failed attempts\n"

    # 4. Suspicious IP addresses
    report += "\n4. SUSPICIOUS IP ADDRESSES\n"
    report += "-" * 60 + "\n"

    suspicious_found = False
    suspicious_threshold = 5

    for ip, count in ip_counts.items():

        if count >= suspicious_threshold:

            suspicious_found = True

            report += (
                f"🚨 {ip} -> {count} failed attempts "
                f"(SUSPICIOUS)\n"
            )

    if not suspicious_found:
        report += "No suspicious IP addresses detected.\n"

    # 5. Failed login timestamps
    report += "\n5. FAILED LOGIN TIMESTAMPS\n"
    report += "-" * 60 + "\n"

    for timestamp in timestamps:
        report += f"{timestamp}\n"

    # 6. Security events
    report += "\n6. FAILED SSH SECURITY EVENTS\n"
    report += "-" * 60 + "\n"

    for event in security_events:

        report += (
            f"Time: {event['timestamp']} | "
            f"IP: {event['ip']} | "
            f"User: {event['username']}\n"
        )

    # 7. Errors
    report += "\n7. ERRORS\n"
    report += "-" * 60 + "\n"

    if errors:

        for error in errors:
            report += f"{error}\n"

    else:
        report += "No errors detected.\n"

    # 8. Warnings
    report += "\n8. WARNINGS\n"
    report += "-" * 60 + "\n"

    if warnings:

        for warning in warnings:
            report += f"{warning}\n"

    else:
        report += "No warnings detected.\n"

    report += "\n" + "=" * 60 + "\n"
    report += "                 END OF REPORT\n"
    report += "=" * 60 + "\n"

    return report
