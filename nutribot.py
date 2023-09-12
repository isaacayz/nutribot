import requests
import cohere
import constant
from cohere.responses.classify import Example
from flask import Flask, request, render_template

"""Instantiation Section"""
key = constant.api_key
co = cohere.Client(key)
app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')


@app.route('/prompter', methods=['GET', 'POST'])
def prompter():
  if request.method == 'GET':
     return render_template('prompter.html')
  else:
    prompt = request.form.get('prompt')
    response = co.generate(
      prompt=prompt,
      num_generations=1,
      max_tokens=40
    )
    print('You\'ve asked an interesting question...')
    generatedResponse = response.generations[0].text
    return render_template('prompter.html', generatedResponse = generatedResponse)
    
@app.route('/summarizer', methods=['GET','POST'])
def summarize():
  # Open a file for reading
  if request.method == 'GET':
    return render_template('summarizer.html')
  else:
    try:
        filepath = request.form.get('unsummarized_file')
        with open(filepath, 'r') as file:
            # Read the entire file content
            file_content = file.read()
            response = co.summarize(
              text=file_content
            )
            reply = str(response.summary)
        with open('./summary.txt', 'w') as summary:
          summary.write(reply)
          print("Summary has been successfully saved in the right file ")
          return render_template('summarizer.html', reply=reply)
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
   app.run(host='127.0.0.1')





#prompter()

""""
  The Classification **Endpoint**
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


inputs=[
  "Confirm your email address",
  "hey i need u to send some $",
]
spamlabels = []
notspamlabels = []
for a in response.classifications:
  spamlabels.append(a.labels['Spam'])
  notspamlabels.append(a.labels['Not spam'])

#print(classifier())
"""

def summarize(filepath):
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

#print(summarize(""))