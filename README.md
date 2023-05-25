# experiment-langchain-agent
An experimental proof-of-concept AI chatbot agent with access to tools (Wikipedia search, local document semantic search) 

Built with
- [LangChain](https://python.langchain.com/en/latest/index.html)
- [Chroma](https://www.trychroma.com/)

# Example

```
Chat with an AI below. The following tools have been made available to the AI during your chat
 - Wikipedia - A wrapper around Wikipedia. Useful for when you need to answer general questions about people, places, companies, facts, historical events, or other subjects. Input should be a search query.
 - Local Document Database - A database to look up information on documents stored locally. Useful for when you need to answer questions using information from documents stored locally

User: Who won the PGA championship in 2023?


> Entering new AgentExecutor chain...
Thought: Do I need to use a tool? Yes
Action: Wikipedia
Action Input: 2023 PGA Championship
Observation: Page: 2023 PGA Championship
Summary: The 2023 PGA Championship was the 105th PGA Championship. It was a 72-hole stroke play tournament played on May 18–21 on the East Course of Oak Hill Country Club in Pittsford, New York.
Brooks Koepka finished at nine under for the tournament to win his third career PGA Championship and fifth major championship by two shots over Viktor Hovland and Scottie Scheffler. Koepka joined Jack Nicklaus and Tiger Woods as the only players to win three PGA titles in the stroke-play era and became the 20th player to win five majors. With the victory, Koepka became the first golfer to win a major golf championship as a member of LIV Golf.



Page: PGA Championship
Summary: The PGA Championship (often referred to as the US PGA Championship or USPGA outside the United States) is an annual golf tournament conducted by the Professional Golfers' Association of America. It is one of the four men's major championships in professional golf.
It was formerly played in mid-August on the third weekend before Labor Day weekend, serving as the fourth and final men's major of the golf season. Beginning in 2019, the tournament is played in May on the weekend before Memorial Day, as the season's second major following the Masters Tournament in April. It is an official money event on the PGA Tour, European Tour, and Japan Golf Tour, with a purse of $11 million for the 100th edition in 2018.
In line with the other majors, winning the PGA gains privileges that improve career security. PGA champions are automatically invited to play in the other three majors (Masters Tournament, U.S. Open, and The Open Championship) and The Players Championship for the next five years, and are eligible for the PGA Championship for life. They receive membership on the PGA Tour for the following five seasons and on the European Tour for the following seven seasons. The PGA Championship is the only one of the four majors that is exclusively for professional players.
The PGA Championship has been held at various venues. Some of the early sites are now quite obscure, but in recent years, the event has generally been played at a small group of celebrated courses.



Page: 2022–23 PGA Tour
Summary: The 2022–23 PGA Tour is the 108th season of the PGA Tour, and the 56th since separating from the PGA of America. The season began on September 15, 2022. The 2023 FedEx Cup Playoffs will begin on August 10, and conclude on August 27, 2023.It is intended that the 2022–23 season will be the final season with the current wraparound format (that started in 2013–14). The tour plans to return to a traditional calendar-year format starting in 2024.


Thought:Do I need to use a tool? No
AI: The PGA championship in 2023 was won by Brooks Koepka.

> Finished chain.

AI: The PGA championship in 2023 was won by Brooks Koepka.
```

# (An opinionated) setup guide

Install Python 3 via [pyenv](https://github.com/pyenv/pyenv) environment manager
```bash
brew install pyenv

pyenv install 3

pyenv shell 3
```

Clone the project
```bash
git clone https://github.com/ypt/experiment-langchain
cd experiment-langchain
```

Set up environment variables
```bash
cp .env.example .env
# then edit .env with your configuration, api keys, etc.
```

Create a new Python virtual environment for the project's dependencies
```bash
# In the project directory

python -m venv venv

source venv/bin/activate

pip list

pip install --upgrade pip

# later, to deactivate the virtual environment
deactivate
```

Install the project package and [develop while updating the code](https://setuptools.pypa.io/en/latest/userguide/quickstart.html#development-mode)
```bash
pip install --editable .
```

Or, just install the project as a static package
```bash
pip install .
```

Run it
```bash
python -m experiment_langchain_agent.agent.main
```

# Usage

- Just chat. Or use the following strings in the chat to activate special functions
- `/help` - display available commands
- `/quit` - quit
- `/ingest {FILE_PATH}` - ingest file(s) at the given file path
- `/tools` - list the tools available to the AI

# Observability
To take a closer look at what calls are happening internally. Try out Langchain's tracing implementation
- https://python.langchain.com/en/latest/additional_resources/tracing.html
- https://python.langchain.com/en/latest/tracing/local_installation.html
- https://python.langchain.com/en/latest/tracing/agent_with_tracing.html#beta-tracing-v2

Start a local tracing server
```bash
langchain plus start
```

A Web UI to examine traces should be available here `http://localhost/`

Configure the app to send traces to the server
```bash
export LANGCHAIN_TRACING_V2=true

# or set in .env file
```

Start the app
```bash
python -m experiment_langchain_agent.agent.main
```

To stop and disable tracing
```bash
unset LANGCHAIN_TRACING_V2
langchain plus stop
```

# TODO
- [ ] LLM: huggingface model
- [ ] Tool: pandas?
- [ ] Tool: internet search
- [ ] UI: streamlit? NextJS + FastAPI?
- [ ] LLM: dynamic switcher
- [ ] Repo: linter, typing checker
- [ ] Tests
- [ ] Internalize langchain as impl detail
- [ ] Dockerize?
- [ ] (Try the same as the above, but with Microsoft/Guidance instead of langchain)