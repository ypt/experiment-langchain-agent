from langchain.agents import initialize_agent, AgentType, AgentExecutor
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory


def create_agent(llm, tools: list[Tool]) -> AgentExecutor:
    print("INITIALIZING CONVERSATION MEMORY")
    memory = ConversationBufferMemory(memory_key="chat_history")

    # Hardcode as a chat optimized agent (CONVERSATIONAL_REACT_DESCRIPTION) for now
    # https://python.langchain.com/en/latest/modules/agents/agents/examples/conversational_agent.html
    # For other types of agents, see: https://python.langchain.com/en/latest/modules/agents/agents/agent_types.html
    return initialize_agent(
        tools,
        llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory)

# TODO: list doc sources. VectorStoreToolkit? https://python.langchain.com/en/latest/modules/agents/toolkits/examples/vectorstore.html
# TODO: tool selection by the agent isn't great, particularly w/ local doc db
