# 📄 Invoice Processing Agent

> A simple example of using the OpenAI Agents SDK to analyze invoices and use a custom tool to save the result as a text file.

## ✨ Features

* 📄 Process PDF invoices
* 🤖 Analyze invoices using an OpenAI Agent
* 📋 Extract structured invoice information
* 🔧 Use a custom tool to save the result to a text file
* ✅ Perform basic invoice validation

## 🛠️ Tech Stack

* Python
* OpenAI Agents SDK
* OpenAI API
* python-dotenv

## 📁 Project Structure

```text
invoice-agent/
├── invoices/
│   └── invoice1.pdf
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd invoice-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Configuration

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your OpenAI API key.

## 📄 Add an Invoice

Place your invoice PDF inside the `invoices` directory:

```text
invoices/
└── invoice1.pdf
```

## ▶️ Run the Project

Run:

```bash
python main.py
```

The agent will analyze the invoice and save the extracted information to:

```text
invoice_result.txt
```

## 🔄 How It Works

The workflow is simple:

```text
PDF Invoice
     ↓
Invoice Agent
     ↓
Extract Invoice Data
     ↓
Generate JSON
     ↓
save_to_txt Tool
     ↓
invoice_result.txt
```

The Agent analyzes the invoice and extracts the requested information. It then uses the custom `save_to_txt` tool to save the generated JSON into a text file.

## 🔧 Custom Tool

This project includes a simple custom tool called `save_to_txt`.

The tool allows the Agent to save text content to a local file:

```python
@function_tool
def save_to_txt(filename: str, content: str) -> str:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return f"File successfully saved to {filename}"
```

This demonstrates how an Agent can use a custom Python function as a tool to perform an action outside of generating text.

## 📋 Output

The Agent returns structured JSON containing information such as:

```json
{
    "invoice_number": "INV-001",
    "invoice_date": "2026-09-20",
    "due_date": "2026-10-20",
    "supplier": {
        "name": "Example Supplier",
        "address": "Paris, France"
    },
    "customer": {
        "name": "Example Customer",
        "address": "Lyon, France"
    },
    "currency": "EUR",
    "subtotal": 1000,
    "discount": 50,
    "tax": 190,
    "total": 1140,
    "payment_terms": "30 days",
    "line_items": [],
    "validation": {
        "calculation_consistent": true,
        "notes": []
    }
}
```

The same JSON is saved to `invoice_result.txt`.

## 🚀 Possible Improvements

This project can be extended to:

* Process multiple invoices
* Save results as JSON files
* Export data to Excel
* Store invoices in a database
* Add more validation rules
* Extract additional invoice fields
* Create multiple tools for the Agent

## 📄 License

This project is available under the MIT License.

---

## 👩‍💻 Author

**Sana Mirahsani**
🎓 Master’s Student in Machine Learning, University of Lille

▶️ YouTube: http://www.youtube.com/@AIwithSana26

💻 GitHub: [https://github.com/sana-mirahsani](https://github.com/sana-mirahsani)

🔗 LinkedIn: [https://www.linkedin.com/in/sana-mirahsani](https://www.linkedin.com/in/sana-mirahsani)