# 📍 Customer CEP Enrichment

Automated Excel data enrichment using Brazilian CEP API (ViaCEP).

---

## 📌 Overview

This project reads an Excel file containing customer CEP (ZIP codes) and automatically fills missing address information using the ViaCEP API.

Fields enriched:
- Address
- Neighborhood
- City
- State
- Region

---

## ⚙️ Features

- ✅ Fetches address data from CEP
- ✅ Skips already filled rows
- ✅ Preserves Excel formatting
- ✅ Handles invalid CEPs gracefully

---

## 🛠️ Technologies

- Python
- Pandas
- Requests
- OpenPyXL

---

## ▶️ How to run

```bash
pip install -r requirements.txt
python main.py
