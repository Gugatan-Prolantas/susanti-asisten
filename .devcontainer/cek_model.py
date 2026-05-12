import google.generativeai as genai
genai.configure(api_key="AIzaSyD4aYZnmeArnKP9FHI5g6qTy6wIuvYxetY")
for m in genai.list_models():
    if 'embedContent' in m.supported_generation_methods:
        print(m.name)
