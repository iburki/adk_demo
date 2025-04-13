import asyncio

from google.adk.agents import LlmAgent, Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from google.adk.tools import google_search, VertexAiSearchTool

search_tool = VertexAiSearchTool(
    data_store_id="data_store_id"
)

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='root_agent',
   instruction='you are helpful agent on unemployment. Use vertex ai search tool to answer questions about unemployment. If questions not related to unemployemnt use the google_search_agent',
   tools=[search_tool]
    )

search_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='google_search_agent',
    description='Gets information from google search',
    instruction='You are a helpful assistant searching for content on google',
    tools=[google_search],
)

