# 🎯 Kahoot Quiz Viewer Extension

A simple, clean extension to view Kahoot quiz questions and answers with a modern dark-themed interface.

## ✨ Features

- ✅ Clean, minimalist interface with dark theme
- ✅ Support for both Quiz ID and Game PIN input
- ✅ Scrollable question viewer
- ✅ Complete question and answer display
- ✅ No unnecessary components
- ✅ Robust error handling
- ✅ Threaded loading to prevent UI freezing
- ✅ Standalone executable files available

## 🚀 Installation and Usage

### Requirements
- **For Executable**: No requirements! Just download and run
- **For Source Code**: Python 3.6+, Tkinter, Internet connection

### Method 1: Download Executable (Easiest)

1. Download the repository or clone it
2. Navigate to the `dist/` folder
3. Double-click `KahootQuizViewer.exe`
4. No Python installation required!

### Method 2: Build Your Own Executable

If the pre-built executable doesn't work or you want to build fresh:

1. **Install Python 3.6+** (if not already installed)
2. **Clone/Download this repository**
3. **Open terminal in the extension folder**
4. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```
5. **Build the executable**:
   ```bash
   pyinstaller --onefile --windowed --name "KahootQuizViewer" main.py
   ```
6. **Find your exe** in the `dist/` folder
7. **Run it**: Double-click `KahootQuizViewer.exe`

### Method 3: Run from Source Code

1. **Install Python 3.6+**
2. **Download/Clone repository**
3. **Open terminal in extension folder**
4. **Run directly**:
   ```bash
   python main.py
   ```

### Method 4: Use Launcher (Windows)

Double-click `START_KAHOOT.bat` for automated launching

## 📖 How to Use

1. **Enter Quiz ID or Game PIN**: 
   - **Quiz ID** (recommended): String like "abc123-def456-ghi789"
     - Always works, independent of game status
     - Found in Kahoot.it quiz URLs
   - **Game PIN**: 6-7 digit number like "1234567" or "735 0114"
     - **ONLY works when game is ACTIVE**
     - Invalid after game ends

2. **Click "Load Quiz" or press Enter** to fetch data

3. **View Results**: 
   - Quiz information displayed at top
   - Questions and answers shown below
   - Use scroll bar to navigate

### 💡 How to get Quiz ID?

1. Go to Kahoot.it
2. Find the quiz you want to view
3. In the URL you'll see: `https://create.kahoot.it/details/abc123-def456-ghi789`
4. The part `abc123-def456-ghi789` is the Quiz ID

## 📁 File Structure

```
extension/
├── dist/
│   ├── KahootQuizViewer.exe         # Main executable
│   └── KahootQuizViewer_Debug.exe   # Debug version with console
├── main.py                          # Main GUI application
├── kahoot_api.py                    # Kahoot API handler
├── START_KAHOOT.bat                 # Launcher script
├── README.md                        # This documentation
├── README_EXE.md                    # Executable documentation
└── .gitignore                       # Git ignore rules
```

## 🎨 Interface Design

- **Background**: Dark Gray (#2c3e50)
- **Text**: White (#ecf0f1)
- **Accent**: Blue (#3498db)
- **Fonts**: Arial for UI, Consolas for results
- **Layout**: Clean, content-focused design

## 🛠️ Error Handling

The extension handles common errors:
- Quiz not found (404)
- Private/restricted quiz (403)
- Internet connection issues
- Rate limiting
- SSL certificate problems
- Invalid input formats
- PIN not active warnings

## ⚙️ Technical Features

- **Threading**: Background data loading
- **Rate Limiting**: Prevents Kahoot API blocking
- **SSL Handling**: Certificate verification with fallback
- **Error Recovery**: Retry logic with exponential backoff
- **Text Cleaning**: Removes HTML tags and formatting
- **PIN Normalization**: Handles spaced PINs (e.g., "735 0114")

## 📋 Important Notes

- This extension is for educational purposes only
- Comply with Kahoot's Terms of Service
- Do not spam requests
- Do not use for cheating in examinations
- PINs only work during active games

## 🔨 Building Your Own Executable

### Quick Build Commands:

```bash
# Install PyInstaller
pip install pyinstaller

# Build main version (no console)
pyinstaller --onefile --windowed --name "KahootQuizViewer" main.py

# Build debug version (with console)
pyinstaller --onefile --console --name "KahootQuizViewer_Debug" main.py
```

### Build Options Explained:
- `--onefile`: Creates single executable file
- `--windowed`: No console window (clean)
- `--console`: Shows console (for debugging)
- `--name`: Custom executable name

### After Building:
1. Find files in `dist/` folder
2. `KahootQuizViewer.exe` - Main version
3. `KahootQuizViewer_Debug.exe` - Debug version
4. Distribute the exe files to anyone!

## 🆘 Troubleshooting

### Installation Issues:
- **No Python**: Download from [python.org](https://python.org)
- **PyInstaller fails**: Try `pip install --upgrade pyinstaller`
- **Permission errors**: Run terminal as Administrator

### Runtime Issues:
1. **Internet connection** - Required for Kahoot API
2. **Correct Quiz ID/PIN format** - See examples above
3. **Quiz is public** - Private quizzes won't work
4. **Antivirus blocking** - Add exe to exceptions
5. **PIN not working** - Game must be active

### Common Issues:
- **"PIN not working"**: Game must be active/running
- **"Quiz not found"**: Check if Quiz ID is correct
- **"Access forbidden"**: Quiz might be private/restricted
- **"SSL Error"**: Try the debug version for details
- **"Exe won't start"**: Check antivirus, try running as admin

## 📄 License

Part of the Kitty-Tools project.
For educational and research purposes only.

## 🤝 Contributing

This is a simplified extension based on the original Kitty-Tools codebase.
Feel free to modify and improve the code for your needs.