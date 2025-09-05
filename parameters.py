from litellm import completion
from config import PROVIDER_MODEL as MODEL

prompt = "Give me exactly 3 creative names in thais for a smart water bottle with more roast and meme."
for temp in [0.0, 0.5, 1.0]:
    r = completion(
        model=MODEL,
        messages=[{"role":"user","content":prompt}],
        temperature=temp,
        top_p=0.6,
        max_tokens=150,
    )
    print("--- temperature =", temp)
    print(r.choices[0].message["content"]) 