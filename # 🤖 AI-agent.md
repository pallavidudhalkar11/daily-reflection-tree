# 🤖 AI Agent Layer (Optional)

## 📌 Purpose

This layer enhances user experience without affecting deterministic logic.

---

## ⚙️ System Flow

User Input → Decision Tree → Category → AI Suggestion

---

## 🧠 AI Responsibilities

* Generate short suggestions (2–3 sentences)
* Stay aligned with the output category
* Improve readability and user experience

---

## 🚫 Restrictions (Guardrails)

* Cannot override decision tree output
* Cannot introduce new categories
* No medical or psychological claims
* No external assumptions

---

## 🧪 Example

**Input:**

* Mood: Bad
* Productivity: Low
* Stress: High

**System Output:**

* Category: Recovery Day

**AI Suggestion:**
"Take time to rest and avoid overloading yourself. Focus on small, manageable tasks tomorrow."

---

## 🛡️ Hallucination Control

* AI operates only after classification
* AI does not make decisions
* AI output is limited in length and scope
* All reasoning is grounded in deterministic output

