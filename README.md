# 🔍 jsonlens

**See the structure of any JSON instantly — without exposing sensitive data.**

---

## 🚀 Why jsonlens?

Working with APIs is painful:

- ❌ Huge JSON (1000+ lines)
- ❌ Deep nesting
- ❌ Sensitive data (can't share)

👉 jsonlens solves this.

---

## ✨ Features

- 🔐 Safe: no real data, only structure
- ❓ Optional fields detection (`?`)
- 🔄 Type merging (`int | str`)
- 📦 List compression (`... N more items`)
- ⚡ Fast / Sample / Full modes

---

## 📦 Install

```bash
pip install jsonlens

## Usage
#Python
from jsonlens import build_structure
import json

data = {
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob", "email": "bob@mail.com"}
    ]
}

print(json.dumps(build_structure(data), indent=2))

## Output
{
  "users": [
    {
      "id": "int",
      "name": "str",
      "email?": "str"
    }
  ]
}