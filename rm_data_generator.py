import os
import openai
from langchain.llms import OpenAI
import json

os.environ['OPENAI_API_KEY'] = "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"

def get_response(prompt:str):
    data = {}
    print("generating the completions....")
    llm1 = OpenAI(model_name="text-davinci-003", temperature=0.9)
    llm2 = OpenAI(model_name="gpt-3.5-turbo", temperature=0.9)
    llm3 = OpenAI(model_name="text-curie-001", temperature=0.9)
    
    data['prompt'] = prompt
    data['completion_1'] = llm1(prompt)
    data['completion_2'] = llm2(prompt)
    data['completion_3'] = llm3(prompt)
    
    return data

file_path = "prompt.txt"

with open(file_path, "r", encoding="utf8") as file:
    lines = file.readlines()
    
lines = [line.strip() for line in lines]

dataset = []

for prompt in lines:
    data = get_response(prompt)
    print(data['prompt'])
    print("completion 1 : ")
    print(data['completion_1'])
    print("completion 2 : ")
    print(data['completion_2'])
    print("completion 3 : ")
    print(data['completion_3'])
    
    print("ranking: ")
    ranking_info = input()
    ranking_info = list(ranking_info)
    
    data['rank'] = ranking_info
    dataset.append(data)

save_file_path = "rm_dataset.json"

with open(save_file_path, "w", encoding="utf8") as json_file:
    json.dump(dataset, json_file, ensure_ascii=False)
    
    







