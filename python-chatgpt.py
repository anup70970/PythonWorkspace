import requests
import argparse
  
parser = argparse.ArgumentParser()
parser.add_argument("prompt",help="code prompt to sent to OpenAI")
parser.add_argument("save_file",help="saves code output to differant file")
arg=parser.parse_args()

api_url= "https://api.openai.com/v1/completions"
api_key="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"
req_header={
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}
req_data={
    "model": "text-davinci-003",
    "prompt": f"write python script to {arg.prompt}. provide only code,no text",
    "max_tokens": 500,
    "temperature": 0.5
}
def build_code():
    response = requests.post(api_url,headers=req_header,json=req_data)
    if response.status_code == 200:
        response_text = response.json()["choices"][0]["text"]
        with open(arg.save_file,"w") as file:
            file.write(response_text)
    else:
        print(f"INVALID REQUEST with response code {str(response.status_code)},please go through code once to debug further")


if __name__ == "__main__":

    build_code()
