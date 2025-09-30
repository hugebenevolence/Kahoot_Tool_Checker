# 🎯 Kahoot Quiz Viewer - Executable Guide

## � Pre-built Executables

If you downloaded this repository, you should find these files in the `dist/` folder:

### 🖥️ **KahootQuizViewer.exe** (Main Version)
- **Description**: Clean application without console window
- **Size**: ~35MB (includes all dependencies)
- **Usage**: Double-click to run
- **Features**: 
  - Clean interface, no console window
  - Perfect for end users
  - Runs completely standalone, no Python needed

### 🐛 **KahootQuizViewer_Debug.exe** (Debug Version)
- **Description**: Version with console for debugging
- **Size**: ~35MB 
- **Usage**: Double-click to run
- **Features**:
  - Shows console with debug information
  - Useful when troubleshooting errors
  - Displays detailed error messages

## 🚀 How to Use

### Option 1: Use Pre-built Executable (Easiest)

1. **Download this repository** (or clone it)
2. **Navigate to `dist/` folder**
3. **Double-click `KahootQuizViewer.exe`**
4. **No Python installation required!**

### Option 2: Build Your Own Executable

If the pre-built executable doesn't work or you prefer building fresh:

1. **Install Requirements**:
   ```bash
   pip install pyinstaller
   ```

2. **Build Commands**:
   ```bash
   # Main version (no console)
   pyinstaller --onefile --windowed --name "KahootQuizViewer" main.py
   
   # Debug version (with console)
   pyinstaller --onefile --console --name "KahootQuizViewer_Debug" main.py
   ```

3. **Find Your Files**: Check the `dist/` folder for your new executables

## 📖 Using the Application

1. **Launch the app**: Double-click the exe file
2. **Enter Input**:
   - **Quiz ID**: UUID format (e.g., f47ac10b-58cc-4372-a567-0e02b2c3d479)
   - **Game PIN**: 6-7 digits (e.g., 735 0114, 7350114)
3. **View Results**: Questions and answers display in the app with dark theme

## ⚠️ Important Notes

- **Game PIN**: Only works when Kahoot game is ACTIVE
- **Quiz ID**: Always works (if quiz is public)
- **Internet**: Required to fetch data from Kahoot
- **Firewall**: May need to allow app internet access
- **Antivirus**: Some antivirus may flag the exe (false positive)

## 📂 Directory Structure

```
extension/
├── dist/
│   ├── KahootQuizViewer.exe          # ← Run this file
│   └── KahootQuizViewer_Debug.exe    # ← Debug version
├── build/                            # Temporary folder (can delete)
├── main.py                          # Source code
├── kahoot_api.py                    # API handler
├── START_KAHOOT.bat                 # Launcher script
├── README.md                        # Main documentation
└── .gitignore                       # Git ignore rules
```

## 🔧 Troubleshooting

### If Executable Won't Run:
1. **Antivirus blocking**: Add exe to antivirus exceptions
2. **Run as administrator**: Right-click → "Run as administrator"
3. **Windows updates**: Ensure Windows is up to date
4. **Missing dependencies**: Try the debug version to see detailed errors

### If You Get Errors:
1. Try `KahootQuizViewer_Debug.exe` to see detailed error messages
2. Check internet connection
3. For Game PIN: Ensure game is currently active
4. For Quiz ID: Ensure quiz is public/accessible

### Building Issues:
- **PyInstaller not found**: Run `pip install pyinstaller`
- **Python not found**: Install Python from [python.org](https://python.org)
- **Permission denied**: Run terminal as administrator
- **Build fails**: Try updating PyInstaller: `pip install --upgrade pyinstaller`

## 💡 Pro Tips

- **Sharing**: Copy exe files to other computers - no Python needed
- **Backup**: Keep source code (`main.py`, `kahoot_api.py`) for future edits
- **Updates**: When code changes, rebuild with PyInstaller
- **Debugging**: Use debug version when troubleshooting
- **Portable**: Exe files are completely portable

## 🔄 Rebuilding Instructions

If you need to rebuild the executables:

```bash
# Navigate to extension folder
cd path/to/extension

# Install PyInstaller (if not already installed)
pip install pyinstaller

# Build main version (recommended)
pyinstaller --onefile --windowed --name "KahootQuizViewer" main.py

# Build debug version (optional)
pyinstaller --onefile --console --name "KahootQuizViewer_Debug" main.py

# Your files will be in the dist/ folder
```

---

**Created by**: Kitty-Tools Extension  
**Build Date**: September 30, 2025  
**PyInstaller**: v6.16.0  
**Python**: 3.13+