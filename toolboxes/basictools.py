import os
from langchain import PromptTemplate, LLMChain
from langchain.llms import AI21
import config

class BasicTools:
    def __init__(self) -> None:
        self.agent_name = None

    def update_user_on_projects(self, agent_id, projects=None, status=None):
        if not self.agent_name:
            self.agent_name = agent_id
        update_prompt = """Write an update about the status of client projects. Make the update short and informative.
        Always write using markdown syntax.
        The projects are as follows:
        Projects: [{projects}]
        Status: {status}"""
        model = "j2-jumbo-instruct"
        j2_jumbo = AI21(model=model)
        prompt = PromptTemplate(template=update_prompt, input_variables=["projects", "status"])
        llm_chain = LLMChain(prompt=prompt, llm=j2_jumbo, verbose=False)
        response = llm_chain.predict(projects=projects, status=status)
        return str(response)
    
    def chat_with_agent(self, agent_id):
        pass
    
