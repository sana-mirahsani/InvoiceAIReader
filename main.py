import asyncio
import os

from agents import Agent, Runner, function_tool
from openai import AsyncOpenAI
from dotenv import load_dotenv


load_dotenv()

print("API KEY FOUND:", os.getenv("OPENAI_API_KEY") is not None)

client = AsyncOpenAI()


# ==========================================
# TOOL: Save text to a file
# ==========================================

@function_tool
def save_to_txt(filename: str, content: str) -> str:
    """
    Save text content to a local TXT file.
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return f"File successfully saved to {filename}"


# ==========================================
# AGENT
# ==========================================

invoice_agent = Agent(
    name="Invoice Agent",

    instructions="""
You are an Invoice Processing Agent.

Analyze the provided invoice.

Extract:

- invoice number
- invoice date
- due date
- supplier
- customer
- currency
- subtotal
- discount
- tax
- total
- payment terms
- line items

For each line item extract:

- description
- quantity
- unit price
- total

Rules:

1. Never invent information.
2. If information is missing, use null.
3. Preserve values from the invoice.
4. Check mathematical consistency.
5. Report possible inconsistencies.
6. Return valid JSON only.

Return exactly this structure:

{
    "invoice_number": null,
    "invoice_date": null,
    "due_date": null,

    "supplier": {
        "name": null,
        "address": null
    },

    "customer": {
        "name": null,
        "address": null
    },

    "currency": null,

    "subtotal": null,
    "discount": null,
    "tax": null,
    "total": null,

    "payment_terms": null,

    "line_items": [],

    "validation": {
        "calculation_consistent": null,
        "notes": []
    }
}

After extracting the invoice information:

1. Create the final JSON.
2. Use the save_to_txt tool to save the exact JSON output
   into a file named "invoice_result.txt".
3. The content saved in the file must be exactly the JSON
   that you generated.
4. After saving the file, return the same JSON as your final output.
""",

    model="gpt-6-luna",

    # Give the Agent access to the tool
    tools=[save_to_txt],
)


# ==========================================
# MAIN
# ==========================================

async def main():

    # Upload invoice
    file = await client.files.create(
        file=open("invoices/invoice1.pdf", "rb"),
        purpose="user_data"
    )

    # Run the Agent
    result = await Runner.run(
        invoice_agent,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_file",
                        "file_id": file.id
                    },
                    {
                        "type": "input_text",
                        "text": "Analyze this invoice, save the JSON result using the available tool, and return the JSON."
                    }
                ]
            }
        ]
    )

    print("\n========== INVOICE RESULT ==========\n")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())