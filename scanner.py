import argparse
from dockerfile_scanner import scan_dockerfile
from compose_scanner import scan_dockercompose
from path_scanner import scan_path
from report_writer import open_report

def main():
    parser = argparse.ArgumentParser(description="Container Security Scanner")

    parser.add_argument("--dockerfile")
    parser.add_argument("--dockercompose")
    parser.add_argument("--path")

    args = parser.parse_args()

    if not any([args.dockerfile, args.dockercompose, args.path]):
        parser.error("Provide --dockerfile, --dockercompose, or --path")

    report, filename = open_report()

    if args.dockerfile:
        scan_dockerfile(args.dockerfile, report)

    if args.dockercompose:
        scan_dockercompose(args.dockercompose, report)

    if args.path:
        scan_path(args.path, report)

    report.close()

    # remove this print if you want ABSOLUTELY no console output
    print(f"Scan results saved to {filename}")

if __name__ == "__main__":
    main()
