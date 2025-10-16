# Plugin Scripts

Utility scripts to enhance your development workflow.

## Available Scripts

### context_monitor.py

A comprehensive context monitoring tool written in Python that helps you understand your project's size and manage AI context effectively.

**Features:**
- Counts total lines of code across the project
- Identifies large and huge files that might impact context
- Shows top largest files (configurable)
- Statistics by file type
- Provides context management tips
- Excludes common directories (node_modules, .git, dist, etc.)
- Cross-platform (works on Windows, macOS, Linux)

**Requirements:**
- Python 3.6+

**Configuration:**

The script can be configured via `settings.json` in the project root:

```json
{
  "contextMonitor": {
    "largeFileThreshold": 1000,
    "hugeFileThreshold": 5000,
    "totalLinesWarning": 50000,
    "topFilesCount": 10,
    "excludedDirs": ["node_modules", ".git", "dist"],
    "fileExtensions": [".js", ".ts", ".py"]
  }
}
```

The plugin includes a pre-configured `settings.json` and `.claude/settings.json` for easy access.

**Usage:**

```bash
# Analyze current directory
python scripts/context_monitor.py

# Or if executable
./scripts/context_monitor.py

# Analyze specific directory
python scripts/context_monitor.py /path/to/project

# Show top 20 largest files
python scripts/context_monitor.py --top 20

# Show statistics by file type
python scripts/context_monitor.py --stats

# Hide context tips
python scripts/context_monitor.py --no-tips

# Show help
python scripts/context_monitor.py --help
```

**Example Output:**

```
========================================
       Context Monitor Report
========================================

Analyzing project files...

⚠ HUGE: src/generated/schema.ts
   Lines: 8,432 | Size: 245KB

⚡ Large: src/utils/helpers.js
   Lines: 1,250 | Size: 42KB

========================================
Summary:
  Total Files: 156
  Total Lines: 45,823
  Large Files (>1000 lines): 3
  Huge Files (>5000 lines): 1

========================================
Top 10 Largest Files:

  8,432 lines - src/generated/schema.ts
  1,250 lines - src/utils/helpers.js
  892 lines - src/components/Dashboard.tsx
  ...

========================================
Statistics by File Type:

  .ts      -   45 files,   12,345 lines
  .js      -   38 files,    8,921 lines
  .tsx     -   22 files,    6,543 lines
  ...

========================================
Context Management Tips:

1. Focus on relevant files only
2. Break large files into smaller modules
3. Use .gitignore patterns for context exclusion
4. Provide summaries for large codebases
5. Reference file:line patterns for specific locations

========================================
```

**Thresholds:**
- Large file: > 1,000 lines
- Huge file: > 5,000 lines
- Project warning: > 50,000 total lines

**Supported File Types:**
- JavaScript/TypeScript: `.js`, `.ts`, `.jsx`, `.tsx`
- Python: `.py`
- Java: `.java`
- C/C++: `.c`, `.cpp`, `.h`, `.hpp`
- C#: `.cs`
- Go: `.go`
- Rust: `.rs`
- Ruby: `.rb`
- PHP: `.php`
- Swift: `.swift`
- Kotlin: `.kt`, `.kts`
- Scala: `.scala`
- R: `.r`
- Shell: `.sh`, `.bash`
- Config: `.json`, `.yaml`, `.yml`
- Documentation: `.md`, `.txt`
- SQL: `.sql`

**Excluded Directories:**
- `node_modules`, `.git`, `dist`, `build`, `.next`
- `vendor`, `__pycache__`, `.venv`, `venv`
- `.idea`, `.vscode`, `target`, `out`, `bin`

## Creating New Scripts

To add new utility scripts:

1. Create your script file in this directory
2. For Python: `chmod +x scripts/your_script.py` and add shebang line
3. For JavaScript: Ensure Node.js is available
4. Add documentation to this README
5. Follow naming conventions:
   - Python: `snake_case.py`
   - JavaScript: `kebab-case.js`
   - Shell: `kebab-case.sh`

## Best Practices

- Always include a help message (`--help` or `-h`)
- Use descriptive output with colors when appropriate
- Handle errors gracefully
- Exclude common directories (node_modules, .git, etc.)
- Make scripts portable (avoid hardcoded paths)
- Add docstrings/comments explaining logic
- Support both relative and absolute paths
- Test on multiple platforms when possible
