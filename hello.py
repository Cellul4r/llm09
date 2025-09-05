from litellm import completion
from config import PROVIDER_MODEL as MODEL

resp = completion(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are concise."},
        {"role": "user", "content": "says Hello 5 times in the same line"}
    ],
    max_tokens=32,
)
print("REPLY:", resp.choices[0].message["content"]) 
print("USAGE:", getattr(resp, "usage", {}))