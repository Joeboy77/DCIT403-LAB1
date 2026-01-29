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

### Step 5: Take Screenshot
While your agent is running, take a screenshot showing the output in your terminal.

### Step 6: Complete Report
Fill in the `environment_setup_report.md` template with your information.

---

## 📦 Deliverables Checklist

Before submitting, ensure you have:

- [ ] Screenshot of running agent (name it `lab1_running_agent.png`)
- [ ] Python source code (`basic_agent.py` with your credentials removed for security)
- [ ] Completed environment setup report (half page)

---

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

## 📚 What You're Learning

This lab teaches you:

1. **SPADE Framework Basics**
   - Agent creation and lifecycle
   - Behavior implementation
   - Asynchronous programming with Python

2. **XMPP Protocol**
   - Agent communication infrastructure
   - JID (Jabber ID) structure
   - Server connectivity

3. **Agent Behaviors**
   - Periodic behaviors
   - Autonomous execution
   - Event-driven programming

4. **Foundation for Future Labs**
   - This basic agent forms the foundation for:
     - SensorAgent (Lab 2)
     - RescueAgent
     - LogisticsAgent
     - CoordinatorAgent

---

## 🎯 Assessment Criteria (from Lab Manual)

Your LAB 1 submission will be evaluated on:

- **Functional Correctness (40%):** Does your agent run successfully?
- **Agent Design Quality (25%):** Is your code well-structured and documented?
- **Coordination & Communication (20%):** Does your agent properly connect to XMPP?
- **Documentation (15%):** Is your report clear and complete?

---

## 📖 Additional Resources

- **SPADE Documentation:** https://spade-mas.readthedocs.io/
- **XMPP Protocol:** https://xmpp.org/
- **Python Asyncio:** https://docs.python.org/3/library/asyncio.html
- **FIPA Standards:** http://www.fipa.org/

---

## ⏭️ Next Steps

After completing LAB 1, you'll move to:

**LAB 2: Perception and Environment Modeling**
- Implement SensorAgent
- Create simulated disaster environment
- Generate and log disaster events

---

## 📝 Notes

- Keep your XMPP credentials secure - don't share them or commit them to public repositories
- The agent will run until you press Ctrl+C
- Make sure to stop the agent properly to avoid connection issues
- Test your agent multiple times to ensure consistent behavior

---

## 🤝 Support

If you encounter issues:
1. Check the `LAB1_SETUP_GUIDE.md` for detailed instructions
2. Review the troubleshooting section above
3. Consult the SPADE documentation
4. Ask your instructor or TA during lab hours

---

**Good luck with your first intelligent agent! 🤖**