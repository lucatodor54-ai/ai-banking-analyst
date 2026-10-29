# 🏦 AI Banking Analyst

An AI-powered banking data analysis project built with **Python, Pandas, SQL, SQLite and the OpenAI API**.

The application allows users to ask questions about banking transaction data in natural language. The AI converts the question into an SQL query, executes it against a SQLite database and explains the result in a clear and understandable way.

## 🚀 How It Works

1. Banking transaction data is loaded from a CSV file.
2. The data is stored and queried using SQLite.
3. The user asks a question in natural language.
4. The AI converts the question into an SQL SELECT query.
5. Python executes the generated SQL query.
6. The AI interprets the result and returns a natural-language answer.

### Example

User question:

> Who are the 3 most valuable clients?

Generated SQL:

```sql
SELECT client_id, nume, SUM(suma) AS valoare_totala
FROM tranzactii
GROUP BY client_id, nume
ORDER BY valoare_totala DESC
LIMIT 3;
