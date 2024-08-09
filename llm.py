import json
import requests
from typing import List, Tuple, Any

# models
CODELLAMA = "codellama:latest"
QWEN2 = "qwen2:latest"
PHI3 = "phi3:medium"
DELPRO = "delpro"
GEMMA = "gemma:7b"
GEMMA_LATEST = "gemma:latest"
LLAMA3 = "llama3:latest"
MISTRAL = "mistral:latest"
MISTRAL_OPENORCA = "mistral-openorca:latest"
MIXTRAL = "mixtral:latest"
REVYO = "revyo:latest"
WIZARD = "wizard-vicuna-uncensored:13b"
WIZARD_CODER = "wizardcoder:latest"
ORCA2 = "orca2:latest"


url = "http://localhost:11434/api/generate"
systemPrompt = "You are a helpful assistant."


def generate(prompt: str, context: List[Any] = [], model: str = LLAMA3,  systemPrompt: str = systemPrompt,
             temperature: float = 0.8, num_predict: int = 4096, asJson: bool = False,) -> Tuple[str, List[Any]]:
    payload = {
        "prompt": prompt,
        "model": model,
        "context": context,
        "system": systemPrompt,
        "temperature": temperature,
        "num_predict": num_predict,
        "stream": False
    }
    if asJson:
        payload["format"] = "json"

    payload_json = json.dumps(payload)

    try:
        r = requests.post(url, headers={
                          "Content-Type": "application/json"}, data=payload_json, stream=False, timeout=10)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Log the error
        print(f"Request failed: {e}")
        raise

    try:
        json_response = json.loads(r.text)
    except json.JSONDecodeError:
        # Log the error
        print("Failed to parse JSON response")
        raise

    if "error" in json_response:
        raise Exception(json_response["error"])

    return json_response["response"], json_response["context"]
