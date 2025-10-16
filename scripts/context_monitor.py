#!/usr/bin/env python3

"""
Context Monitor Script
Monitors and displays context usage, file sizes, and project statistics
Helps developers stay aware of context limitations when working with AI assistants
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Tuple
from collections import defaultdict

# ANSI color codes
class Colors:
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color

# Configuration
LARGE_FILE_THRESHOLD = 1000  # lines
HUGE_FILE_THRESHOLD = 5000   # lines
TOTAL_LINES_WARNING = 50000  # total lines in project

# Directories to exclude
EXCLUDED_DIRS = {
    'node_modules', '.git', 'dist', 'build', '.next',
    'vendor', '__pycache__', '.venv', 'venv', '.idea',
    '.vscode', 'target', 'out', 'bin'
}

# File extensions to analyze
CODE_EXTENSIONS = {
    '.js', '.ts', '.jsx', '.tsx',  # JavaScript/TypeScript
    '.py',                          # Python
    '.java',                        # Java
    '.c', '.cpp', '.h', '.hpp',    # C/C++
    '.go',                          # Go
    '.rs',                          # Rust
    '.rb',                          # Ruby
    '.php',                         # PHP
    '.swift',                       # Swift
    '.kt', '.kts',                 # Kotlin
    '.json', '.yaml', '.yml',      # Config
    '.md', '.txt',                 # Documentation
    '.sql',                         # SQL
    '.sh', '.bash',                # Shell
    '.cs',                          # C#
    '.scala',                       # Scala
    '.r',                           # R
}


def count_lines(file_path: Path) -> int:
    """Count lines in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except Exception:
        return 0


def get_file_size_kb(file_path: Path) -> int:
    """Get file size in KB."""
    try:
        return file_path.stat().st_size // 1024
    except Exception:
        return 0


def format_number(num: int) -> str:
    """Format number with thousand separators."""
    return f"{num:,}"


def should_analyze_file(file_path: Path) -> bool:
    """Check if file should be analyzed."""
    # Check extension
    if file_path.suffix not in CODE_EXTENSIONS:
        return False

    # Check if in excluded directory
    for part in file_path.parts:
        if part in EXCLUDED_DIRS:
            return False

    return True


def analyze_project(directory: Path) -> Tuple[List[dict], dict]:
    """
    Analyze all files in the project.

    Returns:
        Tuple of (file_list, summary)
    """
    files_info = []
    total_lines = 0
    total_files = 0
    large_files = 0
    huge_files = 0
    extension_stats = defaultdict(lambda: {'files': 0, 'lines': 0})

    print(f"{Colors.GREEN}Analyzing project files...{Colors.NC}\n")

    # Walk through directory
    for file_path in directory.rglob('*'):
        if not file_path.is_file():
            continue

        if not should_analyze_file(file_path):
            continue

        lines = count_lines(file_path)
        size_kb = get_file_size_kb(file_path)

        total_lines += lines
        total_files += 1

        # Track by extension
        ext = file_path.suffix
        extension_stats[ext]['files'] += 1
        extension_stats[ext]['lines'] += lines

        file_info = {
            'path': file_path,
            'lines': lines,
            'size_kb': size_kb,
            'relative_path': file_path.relative_to(directory)
        }
        files_info.append(file_info)

        # Check if file is large
        if lines > HUGE_FILE_THRESHOLD:
            huge_files += 1
            print(f"{Colors.RED}⚠ HUGE: {file_info['relative_path']}{Colors.NC}")
            print(f"   Lines: {format_number(lines)} | Size: {size_kb}KB")
        elif lines > LARGE_FILE_THRESHOLD:
            large_files += 1
            print(f"{Colors.YELLOW}⚡ Large: {file_info['relative_path']}{Colors.NC}")
            print(f"   Lines: {format_number(lines)} | Size: {size_kb}KB")

    summary = {
        'total_files': total_files,
        'total_lines': total_lines,
        'large_files': large_files,
        'huge_files': huge_files,
        'extension_stats': dict(extension_stats)
    }

    return files_info, summary


def show_summary(summary: dict):
    """Display project summary."""
    print(f"\n{Colors.BLUE}{'=' * 40}{Colors.NC}")
    print(f"{Colors.GREEN}Summary:{Colors.NC}")
    print(f"  Total Files: {format_number(summary['total_files'])}")
    print(f"  Total Lines: {format_number(summary['total_lines'])}")
    print(f"  Large Files (>{LARGE_FILE_THRESHOLD} lines): {summary['large_files']}")
    print(f"  Huge Files (>{HUGE_FILE_THRESHOLD} lines): {summary['huge_files']}")
    print()

    # Warning if project is very large
    if summary['total_lines'] > TOTAL_LINES_WARNING:
        print(f"{Colors.RED}⚠ WARNING: Project has {format_number(summary['total_lines'])} lines.{Colors.NC}")
        print(f"{Colors.YELLOW}Consider breaking context into smaller chunks.{Colors.NC}")
        print()


def show_largest_files(files_info: List[dict], count: int = 10):
    """Show largest files in the project."""
    print(f"{Colors.BLUE}{'=' * 40}{Colors.NC}")
    print(f"{Colors.GREEN}Top {count} Largest Files:{Colors.NC}")
    print()

    # Sort by lines descending
    sorted_files = sorted(files_info, key=lambda x: x['lines'], reverse=True)

    for file_info in sorted_files[:count]:
        print(f"  {format_number(file_info['lines'])} lines - {file_info['relative_path']}")

    print()


def show_extension_stats(summary: dict):
    """Show statistics by file extension."""
    print(f"{Colors.BLUE}{'=' * 40}{Colors.NC}")
    print(f"{Colors.GREEN}Statistics by File Type:{Colors.NC}")
    print()

    # Sort by total lines descending
    stats = summary['extension_stats']
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]['lines'], reverse=True)

    for ext, data in sorted_stats[:10]:
        print(f"  {ext:8s} - {data['files']:4d} files, {format_number(data['lines']):>8s} lines")

    print()


def show_tips():
    """Display context management tips."""
    print(f"{Colors.BLUE}{'=' * 40}{Colors.NC}")
    print(f"{Colors.GREEN}Context Management Tips:{Colors.NC}")
    print()
    print("1. Focus on relevant files only")
    print("2. Break large files into smaller modules")
    print("3. Use .gitignore patterns for context exclusion")
    print("4. Provide summaries for large codebases")
    print("5. Reference file:line patterns for specific locations")
    print()


def show_header():
    """Display header."""
    print(f"{Colors.BLUE}{'=' * 40}{Colors.NC}")
    print(f"{Colors.BLUE}       Context Monitor Report{Colors.NC}")
    print(f"{Colors.BLUE}{'=' * 40}{Colors.NC}")
    print()


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Context Monitor - Monitor project size and context usage'
    )
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='Directory to analyze (default: current directory)'
    )
    parser.add_argument(
        '-t', '--top',
        type=int,
        default=10,
        help='Number of largest files to show (default: 10)'
    )
    parser.add_argument(
        '--no-tips',
        action='store_true',
        help='Hide context management tips'
    )
    parser.add_argument(
        '--stats',
        action='store_true',
        help='Show statistics by file type'
    )

    args = parser.parse_args()

    # Validate directory
    directory = Path(args.directory).resolve()
    if not directory.exists():
        print(f"{Colors.RED}Error: Directory '{directory}' does not exist{Colors.NC}")
        sys.exit(1)

    if not directory.is_dir():
        print(f"{Colors.RED}Error: '{directory}' is not a directory{Colors.NC}")
        sys.exit(1)

    # Run analysis
    show_header()
    files_info, summary = analyze_project(directory)
    show_summary(summary)
    show_largest_files(files_info, args.top)

    if args.stats:
        show_extension_stats(summary)

    if not args.no_tips:
        show_tips()

    print(f"{Colors.BLUE}{'=' * 40}{Colors.NC}")
    print(f"{Colors.GREEN}Note:{Colors.NC} Token estimates are approximate.")
    print(f"Actual context usage depends on code density.")
    print(f"{Colors.BLUE}{'=' * 40}{Colors.NC}")


if __name__ == '__main__':
    main()
