# AI Agent Creation API Wrapper

This project provides a **common API endpoint** built with **Flask** that allows users to create AI agents either on **VAPI** or **Retell AI** platforms by sending a single standardized request.

---

## 🛠️ Files

- `app.py` — Flask application providing `/create_agent` endpoint.
- `requirements.txt` — Python dependencies.
- `.env` — Environment variables for API keys.

---

## 🚀 How It Works

- Send a POST request to `/create_agent` with JSON body.
- The `provider` parameter decides whether the agent is created on **VAPI** or **Retell**.
- Other parameters like `name`, `model`, `temperature`, and `voice_id` are standardized.

---

## 📄 Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root directory:
      ```env
      VAPI_API_KEY=put_your_vapi_api_key_here
      RETELL_API_KEY=put_your_retell_api_key_here
      ```

5. **Run the Flask server**:
    ```bash
    python app.py
    ```
    Server will start at: [http://localhost:5000](http://localhost:5000)

---

## 📬 API Usage

### Endpoint

`POST /create_agent`

### Request Body (JSON)

| Parameter         | Type    | Required | Description                                  |
|-------------------|---------|----------|----------------------------------------------|
| provider          | string  | Yes      | `"vapi"` or `"retell"`                       |
| name              | string  | No       | Agent name (default: "Default Agent")        |
| model             | string  | No       | LLM model name (default: "gpt-3.5-turbo")     |
| temperature       | float   | No       | Creativity setting (default: 0.7)            |
| voice_id          | string  | No       | Voice ID (default: "shimmer")                |
| description       | string  | No (VAPI only) | Agent description                        |
| initial_message   | string  | No (VAPI only) | Initial agent message                    |
| system_prompt     | string  | No (Retell only) | Custom system prompt                    |
| avatar_url        | string  | No (Retell only) | URL for agent avatar image              |

---

### Example Request (cURL)

```bash
curl -X POST http://localhost:5000/create_agent \
-H "Content-Type: application/json" \
-d '{
  "provider": "vapi",
  "name": "Test Agent",
  "model": "gpt-3.5-turbo",
  "temperature": 0.5,
  "voice_id": "shimmer",
  "description": "This is a test agent",
  "initial_message": "Hello! How can I assist you today?"
}'
