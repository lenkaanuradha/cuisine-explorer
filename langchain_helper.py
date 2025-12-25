from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

import os
import dotenv
dotenv.load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini", api_key= os.getenv('OPEN_API_KEY'))

def generate_dishes_and_restaurant(cuisine):
    restaurant_name = PromptTemplate(
        input_variables=['cuisine'],
        template="Suggest me one good {cuisine} restaurant in India"
    )
    cuisine_name = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest good cuisines from {restaurant_name}"
    )
    extract_text = RunnableLambda(lambda x: x.content)
    chain = (restaurant_name | llm | extract_text | cuisine_name | llm | extract_text)
    menu_items = chain.invoke({'cuisine': cuisine})
    return menu_items
