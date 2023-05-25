from pathlib import Path

from experiment_langchain_agent.agent.llm_factory import create_llm, LLMType
from experiment_langchain_agent.agent.agent_factory import create_agent
from experiment_langchain_agent.agent.tools_factory import create_tools
from experiment_langchain_agent.index import database_factory, ingest
from dotenv import dotenv_values, load_dotenv

PROJECT_ROOT_DIR = Path(__file__).absolute().parent.parent.parent.parent


def main():
    load_dotenv()

    # TODO: load config from a file that can be parsed into namespaced dictionary {llm:{...}, agent:{}, ...}. So we
    #  can pass subset of config to component factories for dynamic component selection and reation. Probably TOML or
    #  YAML instead of env.
    config = {
        **dotenv_values(f"{PROJECT_ROOT_DIR}/.env"),  # load shared development variables
        # **dotenv_values(".env.secret"),  # load sensitive variables
        # **os.environ,  # override loaded values with environment variables
    }

    # setup
    print("INITIALIZING LLM")
    llm = create_llm(llm_type=LLMType[config.get("EXPERIMENT_LANGCHAIN_AGENT_LLM_TYPE")],
                     llm_api_key=config.get("EXPERIMENT_LANGCHAIN_AGENT_LLM_API_KEY"))

    print("INITIALIZING DATABASE")
    database = database_factory.get_database()

    print("INITIALIZING TOOLS")
    tools = create_tools(llm, database)

    print("INITIALIZING AGENT")
    agent = create_agent(llm, tools)

    # Print instructions
    print("Chat with an AI below. The following tools have been made available to the AI during your chat")
    for tool in tools:
        print(f" - {tool.name} - {tool.description}")
    print()

    # REPL
    while True:
        question: str = input("User: ")
        match question:
            case "/help":
                print("System commands:")
                print("/quit                  : quit")
                print("/ingest {FILE_PATH}    : ingest file(s) at the given file path")
                print("/tools                 : list the tools available to the AI")
                print()
            case "/quit" | "/q":
                print("Exiting")
                break
            case "/tools":
                for tool in tools:
                    print(f"- {tool.name} - {tool.description}")
                print()
            case s if s.startswith("/ingest "):
                file_path = s[8:]
                print(f"INGESTING {file_path}")

                # TODO: support full directory, glob, etc.
                documents = ingest.process_document(database, file_path)
                print("FINISHED INGESTING DOCS")
                print(documents)
                print()
            case _:
                result = agent.run(question)
                print()
                print(f"AI: {result}")
                print()


if __name__ == "__main__":
    main()
