from litellm import completion
from config import PROVIDER_MODEL as MODEL

r = completion(model=MODEL, messages=[{"role":"user","content":"Explain APIs in one sentence."}], temperature=0.3, max_tokens=60)
print(r.choices[0].message["content"]) 