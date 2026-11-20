import datetime
from google.adk.tools import agent_tool
from google.adk.agents import Agent


from planner_tool.blog_planner_agent import robust_blog_planner, GEN_MODEL
from writer_tool.blog_writer_agent import robust_blog_writer

planner_tool = agent_tool.AgentTool(agent=robust_blog_planner)
writer_tool = agent_tool.AgentTool(agent=robust_blog_writer)

root_agent = Agent(
    name='Blogger',
    model=GEN_MODEL,
    description="Minimal multi-agent blogger that plans and writes",
    instruction=f"""
    If the user gives a topic:
    1) Call the planner tool to generate the outline.
    2) Call the writer tool to produce the full draft.
    3) End with 3 alternate titles and 2 tweet-length hooks.
    
    If the trends tools fails or times out, continue with a
    sensible outline and draft anyway
    
    Date: {datetime.datetime.now().strftime('%Y-%m-%d')}
    """,
    tools=[
        planner_tool, # calls RobustBlogPlanner
        writer_tool, # calls RobustBlogWriter
    ]
)