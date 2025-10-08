import json

with open("data/text_data/sample_queries.json", "r", encoding="utf-8") as f:
    demo_data = json.load(f)

def get_llm_response(query, disease_info=None, metadata=None):
    for item in demo_data:
        if item["query"] in query:
            return item["answer"]
    return "ക്ഷമിക്കണം, ഇതിനു വേണ്ടിയുള്ള വിവരങ്ങൾ ഇപ്പോൾ ലഭ്യമല്ല."
