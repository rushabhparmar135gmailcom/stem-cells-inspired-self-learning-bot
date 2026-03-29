'''This agent is responsible for building reasons over the fundamentals srapped from the web-pages'''

import openai
import os
from dotenv import load_dotenv

load_dotenv()

# initializing global variables

azure_endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
api_key = os.environ.get('AZURE_OPENAI_API_KEY')
api_version = os.environ.get('OPENAI_API_VERSION')
model = os.environ.get('AZURE_OPENAI_MODEL')

system_prompt = 'You are a human stem cell, learning and adpating knowledge 100 times accurate than a human would, ' \
                'you\'d be trading better than humans, thus whatever news is given to you, ' \
                'summarize them and build an output giving probablity of how the market would move in next few hours' \
                'The respone should be a summary as short as possible'

class reasoning_agent:

    '''this class is responsible for training the agent to articulate and reason our response as planned'''

    def __init__(self, name, user_query):
        self.agent_name = name
        self.user_prompt = user_query
        print(f'hey, i am agent {self.agent_name}')

    def agent_creator(self):

        # defining llm function ---> creating an OpenAI object for Responses API

        llm = openai.OpenAI(
        base_url=f"{azure_endpoint}/openai/v1/",
        api_key=api_key
        )

        # defining the input for Responses API

        input_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": self.user_prompt}
                            ]

        # Calling Azure OpenAI Responses API

        query_response = llm.responses.create(
            input=input_messages,
            model=model,
            max_output_tokens = 100,
            temperature = 0.7,
            stream=True,
             tools=[{"type": "web_search_preview"}]
        )

        for parts in query_response:

            if parts.type == "response.output_text.delta":
                print(parts.delta,  end='')

            else: 
                print('')

agent1 = reasoning_agent('rushabh', 'Whats the latest IRAN-US news?')
agent1.agent_creator()

    
