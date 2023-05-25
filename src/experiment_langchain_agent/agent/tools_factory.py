from langchain.utilities import WikipediaAPIWrapper
from langchain.agents import Tool
from langchain.chains import RetrievalQA
from langchain.vectorstores import VectorStore


def create_tools(llm, database: VectorStore) -> list[Tool]:
    wikipedia = WikipediaAPIWrapper()

    # TODO: tool creation should be done elsewhere
    db_retrieval_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=database.as_retriever(), verbose=True)

    tools = [
        Tool(
            name="Wikipedia",
            func=wikipedia.run,
            description=(
                "A wrapper around Wikipedia. "
                "Useful for when you need to answer general questions about "
                "people, places, companies, facts, historical events, or other subjects. "
                "Input should be a search query."
            )
        ),
        Tool(
            name="Local Document Database",
            func=db_retrieval_chain.run,
            description="A database to look up information on documents stored locally. Useful for when you need to "
                        "answer questions using information from documents stored locally"
        ),
    ]
    return tools

# TODO
# - an agent as a tool
