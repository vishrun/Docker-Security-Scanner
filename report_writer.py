from datetime import datetime

def open_report():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"scan_results_{timestamp}.txt"

    f = open(filename, "w", encoding="utf-8")
    f.write("Container Security Scan Report\n")
    f.write(f"Generated at: {datetime.utcnow()} UTC\n")
    f.write("=" * 70 + "\n\n")

    return f, filename

def write_section(f, title):
    f.write("\n" + "=" * 70 + "\n")
    f.write(title + "\n")
    f.write("=" * 70 + "\n")

def write_line(f, line):
    f.write(line + "\n")
