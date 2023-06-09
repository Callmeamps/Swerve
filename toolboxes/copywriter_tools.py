import os
import datetime
from supabase import create_client, Client
from langchain import PromptTemplate, HuggingFaceHub, LLMChain

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
today = datetime.date.today()

class CustomCopy:
    def __init__(self) -> None:
        pass

    # save to markdown in temp folder
    def create_md(self):
        os.makedirs(f"./__temp__/{today}")
        md = open(f"./__temp__/{today}/{str(today)}.md", "w", encoding="utf-8")
        md.close()
    
    def save_md(self, markdown):
        self.create_md()
        md = open(f"./__temp__/{today}/{str(today)}.md", "w", encoding="utf-8")
        md.write(markdown)
        md.close()
    

    # save post to Posts Table in Supabase
    class SavePost:
        def __init__(self, title, id_field):
            id_field = 0
            self.id = id_field
            self.title = title

        
        def create_entry(self, post):
            supabase.table('Posts').insert({"id": self.id, "title": self.title, "copy": post}).execute()
        def update_title(self, title):
            supabase.table('Posts').update({"id": self.id, "title": title}).execute()
        def add_summary(self, summary):
            supabase.table('Posts').update({"id": self.id, "summary": summary}).execute()
        def add_featured_img(self, img_url):
            supabase.table('Posts').update({"id": self.id, "featured_image": img_url}).execute()
        def add_post_imgs(self, img_urls):
            if isinstance(img_urls, list):
                for img_url in img_urls:
                    supabase.table('Posts').update({"post_images": img_url}).execute()
            else:
                supabase.table('Posts').update({"post_images": img_urls}).execute()

    # save deliverable to Deliverables Table in Supabase

    # zip and send files to OCI Bucket

    # send update to Reporter

    # write post using MPT7B Storywriter
    def write_post(self, post_topic):
        template = """
        Write an article about the given topic. Make the article interesting and informative.
        Always write using markdown syntax.
        Topic: {topic}"""
        repo_id = "mosaicml/mpt-7b-storywriter"
        mpt_65k = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0.3, "max_length":6000})
        prompt = PromptTemplate(template=template, input_variables=["topic"])
        llm_chain = LLMChain(prompt=prompt, llm=mpt_65k, verbose=False)
        question = post_topic

        response = llm_chain.predict(question=question)
        self.save_md(response)
