 ## PandasAPI: Chat with your JSON data

PandasAPI is a REST API that allows you to interact with your JSON data in a conversational manner using Large Language Models (LLMs) like GPT-3.5, GPT-4, and Gemini. It leverages the power of PandasAI to translate your natural language questions into Python code, execute it on your data, and return the results in a user-friendly format. 

### Features

* **Conversational data analysis:** Ask questions about your JSON data in plain English, just like you would chat with a data analyst.
* **Supported LLMs:** Choose from OpenAI's GPT-3.5, GPT-4, or Google's Gemini to power the natural language understanding.
* **Flexible output formats:** Get answers in various formats, including strings, numbers, dataframes, and even charts.
* **Easy deployment:** Run the API locally or deploy it to a cloud platform using the provided Dockerfile.

### Getting Started

1. **Clone the repository:**
```
git clone https://github.com/traien/PandasAPI.git
```

2. **Install dependencies:**
```
pip install -r requirements.txt
```

3. **Set up your API keys:**
   - Obtain API keys for your chosen LLM (OpenAI or Gemini).
   - Set the keys as environment variables: `OPENAI_API_KEY` or `GEMINI_API_KEY`.

4. **Run the API:**
   - **Locally:**
     ```
     python main.py
     ```
   - **Using Docker:**
     ```
     docker build -t pandasapi .
     docker run -p 8000:8000 pandasapi
     ```

5. **Send requests:**
   - Use a REST client to send POST requests to `http://localhost:8000/generate`.
   - Include your JSON data in the request body and your query as the `prompt` parameter.

### Example Usage

**Request:**

```
curl -X 'POST' \
  'http://127.0.0.1:8000/generate?prompt=Which%20are%20the%20top%205%20countries%20by%20sales%3F' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '"{\r\n    \"country\": [\"United States\", \"United Kingdom\", \"France\", \"Germany\", \"Italy\", \"Spain\", \"Canada\", \"Australia\", \"Japan\", \"China\"],\r\n    \"sales\": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]\r\n}"'
```

**Response:**

```
{
  "message": {
    "country": {
      "0": "China",
      "1": "United States",
      "2": "Japan",
      "3": "Germany",
      "4": "United Kingdom"
    },
    "sales": {
      "0": 7000,
      "1": 5000,
      "2": 4500,
      "3": 4100,
      "4": 3200
    }
  }
}
```