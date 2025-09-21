# Create-rename-Delete-files-in-a-folder

# 🐍 File Manager Automation with `pathlib`

A simple, safe, and interactive Python script that lets you:
- ✅ **Create** files with custom naming
- ✅ **Rename** files with user confirmation
- ✅ **Clear/Delete** files in a folder (with prompt!)

Built with `pathlib` — modern, readable, and cross-platform.

---

## 🚀 Features

- Asks for **user confirmation** before any destructive action (rename/delete)
- Creates files with **custom prefix and zero-padded numbering** (e.g., `file_01.txt`)
- Deletes only **files** (not folders) by default — safe for beginners
- Runs on **Windows, macOS, Linux**

---

## ▶️ How to Run

Clone this repo and run `python renamefiles.py`. Follow the prompts.

---

## 💡 Example Workflow

Creating files → asks if you want to rename → asks if you want to delete. All with confirmation.

---

## 🛠️ Requirements

- Python 3.6+

---

## 📁 Folder Structure

Creates `files` folder on your Desktop.

---

## ⚠️ Safety First

Won’t rename or delete without your explicit “y” which represents yes. Won’t touch folders. Won’t overwrite.

---

## 🌟 Why This Script?

Great for learning, teaching, or safe file automation.

---

## 🤝 Contributing

Fork it. Improve it. Add undo, trash support, GUI — go wild.

---

## 📜 License

MIT — Do whatever you want.

---

Made with ❤️ using Python and pathlib.
