import os, openai, dotenv

dotenv.load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


def openai_func(inp_text):
  openai.api_key = openai_api_key

  res = openai.Completion.create(
    model="text-davinci-003",
    prompt=inp_text,
    max_tokens=7,
    temperature=0
  )
  return res
