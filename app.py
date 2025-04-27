from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

VAPI_API_KEY = os.getenv("VAPI_API_KEY")
RETELL_API_KEY = os.getenv("RETELL_API_KEY")

VAPI_ENDPOINT = "https://api.vapi.ai/assistants"
RETELL_ENDPOINT = "https://api.retellai.com/agents"

@app.route('/create_agent', methods=['POST'])
def create_agent():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        provider = data.get("provider", "").lower()
        if provider not in ["vapi", "retell"]:
            return jsonify({"error": "Invalid provider. Use 'vapi' or 'retell'"}), 400
        
        name = data.get("name", "Default Agent")
        model = data.get("model", "gpt-3.5-turbo")
        temperature = data.get("temperature", 0.7)
        voice_id = data.get("voice_id", "shimmer")
        
        if provider == "vapi":
            api_params = {
                "name": name,
                "model": {
                    "provider": "openai",
                    "model": model,
                    "temperature": temperature
                },
                "voice": {
                    "provider": "openai",
                    "voice_id": voice_id
                }
            }
            
            if "description" in data:
                api_params["description"] = data["description"]
                
            if "initial_message" in data:
                api_params["initial_message"] = data["initial_message"]
                
            headers = {
                "Authorization": f"Bearer {VAPI_API_KEY}",
                "Content-Type": "application/json"
            }
            
            response = requests.post(VAPI_ENDPOINT, json=api_params, headers=headers)
            
        else:
            api_params = {
                "name": name,
                "llm": {
                    "provider": "openai",
                    "model": model,
                    "temperature": temperature,
                    "system_prompt": data.get("system_prompt", "")
                },
                "voice": {
                    "type": "tts",
                    "provider": "openai",
                    "voice_id": voice_id
                }
            }
            
            if "avatar_url" in data:
                api_params["avatar"] = {
                    "url": data["avatar_url"]
                }
                
            headers = {
                "Authorization": f"Bearer {RETELL_API_KEY}",
                "Content-Type": "application/json"
            }
            
            response = requests.post(RETELL_ENDPOINT, json=api_params, headers=headers)
        
        return jsonify(response.json())
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)