# # from langchain.agents import AgentType, initialize_agent, load_tools
# from langchain.chat_models import ChatOpenAI
# import os
# from dotenv import load_dotenv

# load_dotenv()
# llm= ChatOpenAI(model="gpt-4.1-mini", api_key=os.getenv('OPEN_API_KEY'))
# # tools = load_tools(["wikipedia", "llm-math"], llm=llm)

# # agents = initialize_agent(
# #     tools,
# #     llm,
# #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
# #     # verbose=True
# # )

# # response = agents.run("Tell me when was Elon Musk born and what is his age ")
# # print(response)


# # tools = load_tools(["serpapi", "llm-math"], llm=llm, serpapi_api_key=os.getenv('SERPAPI'))
# # agents =initialize_agent(
# #     tools,
# #     llm,
# #     agent =AgentType.ZERO_SHOT_REACT_DESCRIPTION,
# #    # verbose=True
# # )
# # res = agents.run("What is the current GDP of US plus 5 ?")
# # print(res)
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import  LLMChain
# from langchain_core.prompts import PromptTemplate
# memory = ConversationBufferMemory()
# prompt_name = PromptTemplate(
#     input_variables=["question"],
#     template="Answer the following question: {question}"
# )
# chain = LLMChain(llm=llm, memory=memory)
# answer =chain.run("What is the capital of India?")
# print(answer)