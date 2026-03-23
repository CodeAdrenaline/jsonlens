# 🔍 jsonlens

**See the structure of any JSON instantly — without exposing sensitive data.**

---

## 🚀 Why jsonlens?

Working with APIs is painful:

* ❌ Huge JSON responses (1000+ lines)
* ❌ Deeply nested structures
* ❌ Sensitive data you cannot share

👉 **jsonlens converts JSON into a clean, safe structure.**

---

## ✨ Features

* 🔐 Safe — no real values, only structure
* ❓ Optional fields detection (`email?`)
* 🔄 Type merging (`int | str`)
* 📦 List compression (`... N more items`)
* ⚡ Fast / Sample / Full modes

---

## 📦 Installation

```bash
pip install jsonlens
```

---

## ⚡ Basic Usage

```python
from jsonlens import build_structure
import json

data = {
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob", "email": "bob@mail.com"}
    ]
}

result = build_structure(data, mode="full")

print(json.dumps(result, indent=2))
```

---

## 🧾 Output

```json
{
  "users": [
    {
      "id": "int",
      "name": "str",
      "email?": "str"
    }
  ]
}
```

---

## 🧠 Explanation

* `email?` → optional field (not present in all items)
* `int | str` → multiple possible types
* `... N more items` → repeated structure compressed

---

## ⚙️ Modes

```python
build_structure(data, mode="fast")    # first item only
build_structure(data, mode="sample")  # few items
build_structure(data, mode="full")    # full scan
```

| Mode   | Description            |
| ------ | ---------------------- |
| fast   | fastest, less accurate |
| sample | balanced               |
| full   | most accurate          |

---

## 🔥 Example: Nested JSON

```python
data = {
    "orders": [
        {
            "id": 1,
            "items": [{"name": "Laptop"}, {"name": "Mouse"}]
        },
        {
            "id": 2,
            "items": [{"name": "Keyboard"}]
        }
    ]
}

print(json.dumps(build_structure(data, mode="full"), indent=2))
```

---

## 🧾 Output

```json
{
  "orders": [
    {
      "id": "int",
      "items": [
        {
          "name": "str"
        },
        "... 1 more items (same structure)"
      ]
    },
    "... 1 more items (same structure)"
  ]
}
```

---

## 🔐 Safe for AI Usage

Instead of sharing real API data:

❌ Original:

```json
{
  "email": "user@gmail.com"
}
```

✅ With jsonlens:

```json
{
  "email": "str"
}
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch
3. Make changes
4. Open a Pull Request

---

## ⭐ Support

If you find this useful:

* ⭐ Star the repository
* Share with other developers

---

## 🪪 License

MIT License
