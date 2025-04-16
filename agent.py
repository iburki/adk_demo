import asyncio

from google.adk.agents import LlmAgent, Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from google.adk.tools import google_search, VertexAiSearchTool

MODEL_NAME = 'gemini-2.0-flash-live-preview-04-09'

search_tool_parks = VertexAiSearchTool(
    data_store_id="enter_data_store_id_here"
)
search_tool_airports = VertexAiSearchTool(
    data_store_id="enter_data_store_id_here"
)

search_agent = LlmAgent(
    model=MODEL_NAME,
    name='search_agent',
    instruction='You are a helpful assistant searching for answering questions on public transportation to La Guardia Airport.',
    tools=[search_tool_airports],
)

root_agent = LlmAgent(
    model=MODEL_NAME,
    name='root_agent',
   instruction=f"""You are an expert on Central Park in New York City. Your goal is to answer user questions about the park as accurately as possible.
                    If questions not related to Central Park, use the "{search_agent}"
   """,
   tools=[search_tool_parks]
    )




