from litellm import completion
from config import PROVIDER_MODEL as MODEL

shots = (
    "Review: 'Amazing product!' → Negative\n"
    "Review: 'Waste of money.' → Negative\n"
    "Review: 'It's okay.' → Neutral\n"
)
q = "Review: 'Loved the build quality!' →"
msg = f"""Classify sentiment based on example that I given to you.
Examples:
{shots}
Now continue:
{q}"""
resp = completion(model=MODEL, 
    messages=[{"role":"user","content":msg}], 
    temperature=0.2
    )
print(resp.choices[0].message["content"]) 