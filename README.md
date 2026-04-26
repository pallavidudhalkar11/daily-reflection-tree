# 🌳 Daily Reflection Tree

## 📌 Overview

This project implements a **deterministic decision tree** for structured daily reflection.

---

## 🧠 Inputs

* Mood: Good / Neutral / Bad
* Productivity: High / Medium / Low
* Stress: High / Low

---

## 🌳 Decision Logic

* Good + High Productivity + Low Stress → Growth Day
* Good + Low Productivity → Improvement Day
* Neutral + Medium Productivity → Maintenance Day
* Bad + High Stress → Recovery Day
* Bad + Low Productivity → Warning Day

---

## 🛡️ Guardrails

* No AI guessing
* Fixed rules only
* Same input → same output

---

## 🚀 Run

```bash
python main.py
```
