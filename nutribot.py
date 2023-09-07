import requests
import cohere
import constant
from cohere.responses.classify import Example

"""The Generation Endpoint"""

key = constant.api_key
co = cohere.Client(key)

def prompter():
  prompt = input('What would you like to know? ')
  response = co.generate(
    prompt=prompt,
    num_generations=1,
    max_tokens=40
  )
  print('\n You\'ve asked an interesting question. \n Please find your answer below \n')
  print(response.generations[0].text)

#prompter()

"""The Classification **Endpoint**"""
examples=[
  Example("Dermatologists don't like her!", "Spam"),
  Example("'Hello, open to this?'", "Spam"),
  Example("I need help please wire me $1000 right now", "Spam"),
  Example("Nice to know you ;)", "Spam"),
  Example("Please help me?", "Spam"),
  Example("Your parcel will be delivered today", "Not spam"),
  Example("Review changes to our Terms and Conditions", "Not spam"),
  Example("Weekly sync notes", "Not spam"),
  Example("'Re: Follow up from today's meeting'", "Not spam"),
  Example("Pre-read for tomorrow", "Not spam"),
]
def classifier():
  prompts = list(input('Please enter your query '))
  response = co.classify(
    inputs=prompts,
    examples=examples,
    )
  return response[0]['labels']


"""inputs=[
  "Confirm your email address",
  "hey i need u to send some $",
]
spamlabels = []
notspamlabels = []
for a in response.classifications:
  spamlabels.append(a.labels['Spam'])
  notspamlabels.append(a.labels['Not spam'])
"""
#print(classifier())

def summarize(filepath):
  # Open a file for reading
  try:
      with open(filepath, 'r') as file:
          # Read the entire file content
          file_content = file.read()
          response = co.summarize(
             text=file_content
          )
      with open('./summary.txt', 'w') as summary:
         summary.write(str(response.summary))
         print("Summary has been successfully saved in the right file ")
  except FileNotFoundError:
      print("The file does not exist.")
  except Exception as e:
      print(f"An error occurred: {str(e)}")

print(summarize('/Users/isaacige/Documents/Code/DS&ML/nutribot/story.txt'))
