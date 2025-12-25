from openai import OpenAI
import os
from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda

load_dotenv()
api_key = os.getenv('OPEN_API_KEY')

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4.1-mini", api_key=api_key)

from langchain_core.prompts import PromptTemplate
cuisine_name = PromptTemplate(
    input_variables=["cuisine"],
    template="Suggest me one  good  {cuisine} restaurant in India"
);


restaurant_name = PromptTemplate(
    input_variables=[ "restaurant_name"],
    template="Suggest me  good cuisines from {restaurant_name} "
)
extract_text = RunnableLambda(lambda x:x.content)


chain = (cuisine_name | llm | extract_text| restaurant_name | llm | extract_text)
response = chain.invoke({"cuisine": "Mexican"})
print(response)



