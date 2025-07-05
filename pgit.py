"""
Author: Golemon
Created: 2025.7.5
Version: 1.0

Description:
This script implements a lightweight file archiving and version management tool. 
It compresses specified files or directories into a dedicated storage folder and generates log records with timestamps and commit messages. 
Using the timestamp, the corresponding archive can be quickly located and restored to the current directory, facilitating efficient version snapshot management and recovery.

    - Archive commit:
    python pgit.py atomic -t <file_or_directory_path> -m "<commit_message>"
        e.g.: python pgit.py atomic -t ll.txt -m "store ll.txt"
    
    - Restore archive:
    python pgit.py restore -ts <timestamp>
        e.g.: python pgit.py restore 20250705_104019


"""
import os
import sys
import json
import zipfile
import argparse
from datetime import datetime
import shutil

PGIT_LOG_FILE = "./pgit_store/pgit_log.json"
PGIT_STORE_DIR = "./pgit_store"


def ensure_dirs():
    """Ensure log file and storage directory exist"""
    if not os.path.exists(PGIT_STORE_DIR):
        os.makedirs(PGIT_STORE_DIR)
    if not os.path.exists(PGIT_LOG_FILE):
        with open(PGIT_LOG_FILE, 'w') as f:
            json.dump([], f, indent=2)


def zip_file_or_dir(src_path, dest_path):
    """Compress a single file or an entire directory"""
    with zipfile.ZipFile(dest_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isfile(src_path):
            zipf.write(src_path, os.path.basename(src_path))
        else:
            for root, dirs, files in os.walk(src_path):
                for file in files:
                    abs_file = os.path.join(root, file)
                    rel_path = os.path.relpath(abs_file, os.path.dirname(src_path))
                    zipf.write(abs_file, rel_path)


def write_commit_log(entry):
    """Write a commit record to the JSON log file"""
    with open(PGIT_LOG_FILE, 'r', encoding='utf-8') as f:
        log = json.load(f)
    log.append(entry)
    with open(PGIT_LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(log, f, indent=4, ensure_ascii=False)


def pgit_atomic(target, message):
    """Main function: compress and commit record"""
    ensure_dirs()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(os.path.abspath(target))
    zip_name = f"{base_name}_{timestamp}.zip"
    zip_path = os.path.join(PGIT_STORE_DIR, zip_name)

    print(f"[+] Compressing {target} -> {zip_path}")
    zip_file_or_dir(target, zip_path)

    commit_entry = {
        "target": target,
        "zip_file": zip_path,
        "timestamp": timestamp,
        "commit": message
    }

    write_commit_log(commit_entry)
    print(f"[✓] Commit recorded to {PGIT_LOG_FILE}")


def restore_by_timestamp(timestamp):
    """Restore the compressed archive from the log by timestamp to the current directory"""
    ensure_dirs()

    with open(PGIT_LOG_FILE, 'r', encoding='utf-8') as f:
        log = json.load(f)

    matched_entry = next((entry for entry in log if entry["timestamp"] == timestamp), None)

    if not matched_entry:
        print(f"[!] Error: No commit found with timestamp {timestamp}")
        return

    zip_src_path = matched_entry["zip_file"]
    zip_filename = os.path.basename(zip_src_path)
    zip_dst_path = os.path.join(".", timestamp + '.zip')

    try:
        shutil.copy(zip_src_path, zip_dst_path)
        print(f"[✓] Restored {zip_filename} to current directory.")
    except Exception as e:
        print(f"[!] Restore failed: {e}")


def main():
    parser = argparse.ArgumentParser(description="pgit: lightweight file commit tool")
    subparsers = parser.add_subparsers(dest="command")

    # atomic sub-command
    atomic_parser = subparsers.add_parser("atomic", help="Archive and commit file or directory")
    atomic_parser.add_argument("-t", "--target", required=True, help="File or directory to archive")
    atomic_parser.add_argument("-m", "--message", required=True, help="Commit message")

    # restore sub-command
    restore_parser = subparsers.add_parser("restore", help="Restore compressed archive by timestamp")
    restore_parser.add_argument("-ts", "--timestamp", required=True, help="Timestamp of the commit to restore")

    args = parser.parse_args()

    if args.command == "atomic":
        if not os.path.exists(args.target):
            print(f"[!] Error: Target {args.target} not found.")
            sys.exit(1)
        pgit_atomic(args.target, args.message)

    elif args.command == "restore":
        restore_by_timestamp(args.timestamp)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
