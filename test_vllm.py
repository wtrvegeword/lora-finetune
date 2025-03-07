from openai import OpenAI
client = OpenAI(api_key="0",base_url="http://0.0.0.0:8000/v1")
messages = [{"role": "user", "content": "hello, what can you do?"}]
result = client.chat.completions.create(messages=messages, model="model_path")   #change the "model_path" to your model folder path 
print(result.choices[0].message)
