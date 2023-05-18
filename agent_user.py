from langchain.experimental import AutoGPT
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore import InMemoryDocstore
from langchain.vectorstores import FAISS
import faiss
from team import TeamMember
import config

class AutoAgent(TeamMember):
    def __init__(self, first, last, dob, email, phone, address, role, salary, project, tools):
        super().__init__(first, last, dob, email, phone, address, role, salary, project)
        self.tools = []
        self.projects = []
        self.fullname = f"{first} {last}"
        self.email = email
        self.phone = phone
        self.role = role
        self.vectorstore = None

        # validate tools field
        if isinstance(tools, list):
            for entry in tools:
                self.tools.append(entry)
        else:
            raise TypeError("Invalid Tool...")
        self.create_empty_vector_embedding()
        self.agent = self.create_agent()
        
    def create_empty_vector_embedding(self):
        # Define embedding model
        embeddings_model = OpenAIEmbeddings()
        # Initialize the vectorstore as empty

        embedding_size = 1536
        index = faiss.IndexFlatL2(embedding_size)
        self.vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})


    def details(self):
        print(f"Name: {self.fullname}\nRole: {self.role}\nTools: {self.tools}")

    def work_on(self, instructions: str) -> str:
        agent_response = self.agent.run([instructions])
        return agent_response

    def create_agent(self, llm=None):
        vector_memory = self.vectorstore.as_retriever()
        if llm:
            pass
        else:
            llm = ChatOpenAI(temperature=0.5)
        agent = AutoGPT.from_llm_and_tools(
            ai_name=self.fullname,
            ai_role=self.role,
            tools=self.tools,
            llm=llm,
            memory=vector_memory
            )
        return agent
