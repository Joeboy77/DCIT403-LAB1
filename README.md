# DCIT403-LAB1

# LAB 1: Environment and Agent Platform Setup
## DCIT 403 - Designing Intelligent Agent

### 📋 Overview
This is the complete implementation for **LAB 1** of the Disaster Response & Relief Coordination System project. This lab focuses on setting up your development environment and creating your first SPADE agent.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `LAB1_SETUP_GUIDE.md` | Complete step-by-step guide with all instructions |
| `basic_agent.py` | Main Python code for your first SPADE agent |
| `environment_setup_report.md` | Template for your half-page setup report |
| `setup.sh` | Automated setup script (optional) |
| `README.md` | This file |

---

## 🚀 Quick Start

### Step 1: Install Required Software
```bash
# Make setup script executable (if using Linux/Mac)
chmod +x setup.sh

# Run automated setup
./setup.sh

# OR install manually:
pip install spade aiohttp
```

### Step 2: Register XMPP Account
1. Go to https://xmpp.jp/
2. Register a new account (e.g., `yourusername@xmpp.jp`)
3. Remember your username and password

### Step 3: Configure Your Agent
Edit `basic_agent.py` and replace these lines:
```python
AGENT_JID = "yourusername@xmpp.jp"  # Your actual username
AGENT_PASSWORD = "yourpassword"      # Your actual password
```

### Step 4: Run Your Agent
```bash
python3 basic_agent.py
```

You should see:
```
==================================================
LAB 1: Basic SPADE Agent
==================================================
Connecting to: xmpp.jp
Agent JID: yourusername@xmpp.jp
==================================================
Agent yourusername@xmpp.jp is starting...
Agent yourusername@xmpp.jp is running
Agent started successfully!
Press Ctrl+C to stop the agent...
==================================================
MyBehaviour running - Current time: 2026-01-29 10:30:45
MyBehaviour running - Current time: 2026-01-29 10:30:50
...
```




## 🔧 Troubleshooting

### Problem: Cannot connect to xmpp.jp
**Solutions:**
1. Verify your credentials are correct
2. Check your internet connection
3. Try registering a new account if login fails
4. Ensure no firewall is blocking port 5222

### Problem: SPADE installation fails
**Solutions:**
```bash
pip install --upgrade pip
pip install --user spade
# OR
pip install spade --no-cache-dir
```

### Problem: "ImportError: No module named spade"
**Solution:**
```bash
# Check Python version
python3 --version

# Reinstall SPADE
pip3 install spade

# Verify installation
python3 -c "import spade; print(spade.__version__)"
```

---
 intelligent agent! 🤖**
