# 🌳 Deterministic Decision Tree

## 📌 Overview

This document defines the **deterministic logic** used for daily reflection.

The system ensures:

* Same input → Same output
* No ambiguity
* Fully explainable decisions

---

## 🌳 Decision Structure

```
Start
│
├── Mood = Good
│   ├── Productivity = High AND Stress = Low → Growth Day
│   └── Productivity = Low → Improvement Day
│
├── Mood = Neutral
│   └── Productivity = Medium → Maintenance Day
│
└── Mood = Bad
    ├── Stress = High → Recovery Day
    └── Productivity = Low → Warning Day
```

---

## 📊 Decision Table

| Mood    | Productivity | Stress | Output          |
| ------- | ------------ | ------ | --------------- |
| Good    | High         | Low    | Growth Day      |
| Good    | Low          | Any    | Improvement Day |
| Neutral | Medium       | Any    | Maintenance Day |
| Bad     | High         | High   | Recovery Day    |
| Bad     | Low          | Any    | Warning Day     |

---

## 🎯 Key Properties

* Deterministic (no randomness)
* Rule-based decision making
* No dependency on AI
* Fully transparent

---

## 🔒 Constraints

* Only predefined categories allowed
* No emotional interpretation beyond inputs
* No hidden or dynamic rules
