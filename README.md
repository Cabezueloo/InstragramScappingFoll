# Instagram Follower/Following Tracker 🔍

A Python tool to monitor changes in Instagram followers and following lists over time.

## 📌 Key Features
- **Baseline Scanning** - Create initial snapshots of followers/following
- **Change Detection** - Identify new followers and unfollows between scans
- **Dual-mode Operation** - Track either followers or following lists
- **Session Persistence** - Uses stored cookies for authentication
- **Scroll Automation** - Automatically handles infinite scroll loading
- **Comparison Reports** - Shows exact changes between scans
- **Keyboard Control** - Trigger scans with Ctrl key press

## 🛠️ How It Works
1. **Initial Scan** (`older_` files):
   - Creates reference snapshot
   - Records all current connections
   - Stores in `followers/older_followers.txt` and `following/older_following.txt`

2. **Subsequent Scans** (`newest_` files):
   - Compares with baseline data
   - Detects:
     - 🆕 New followers/following
     - 🚫 Lost followers/unfollows
   - Generates console report with changes

## ⚙️ Requirements
- Python 3.7+
- Google Chrome browser
- ChromeDriver (matching Chrome version)
- Python packages:
  ```bash
  pip install selenium pynput