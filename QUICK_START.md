# 🚀 Quick Start Guide - Kahoot Quiz Viewer

## ⚡ Fastest Way to Get Started

### Option 1: Use Pre-built Executable (No Programming Required)

1. **Download** this repository
2. **Open** the `dist/` folder 
3. **Double-click** `KahootQuizViewer.exe`
4. **Done!** Start viewing Kahoot quizzes immediately

### Option 2: Build Your Own (Fresh Build)

```bash
# 1. Install Python (if not installed) - python.org
# 2. Install PyInstaller
pip install pyinstaller

# 3. Navigate to this folder
cd kahoot-quiz-viewer-extension

# 4. Build the executable
pyinstaller --onefile --windowed --name "KahootQuizViewer" main.py

# 5. Find your exe in dist/ folder
# 6. Double-click to run!
```

## 📖 How to Use

1. **Launch** the application
2. **Enter** either:
   - **Quiz ID**: `abc123-def456-ghi789` (always works)
   - **Game PIN**: `1234567` (only works during active games)
3. **Click** "Load Quiz" or press Enter
4. **View** questions and answers in the scrollable interface

## ❓ Where to Find Quiz ID

1. Go to any Kahoot quiz page
2. Look at the URL: `https://create.kahoot.it/details/YOUR-QUIZ-ID-HERE`
3. Copy the ID part after `/details/`

## 🔧 Need Help?

- **Exe won't start**: Try running as administrator
- **Antivirus warning**: Add exe to exceptions (it's safe)
- **Game PIN not working**: Game must be currently active
- **Quiz not found**: Check if Quiz ID is correct and quiz is public

## 📁 What's Included

- `KahootQuizViewer.exe` - Main application (clean interface)
- `KahootQuizViewer_Debug.exe` - Debug version (shows console)
- `START_KAHOOT.bat` - Alternative launcher
- Source code for customization

---

**Ready to go in under 1 minute!** 🎯