from dotenv import load_dotenv
from google.adk.agents import Agent, LoopAgent

# The planner agent
load_dotenv()
GEN_MODEL="gemini-3.5-flash-lite"


class OutlineValidationChecker(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            name="OutlineValidationChecker",
            model=GEN_MODEL,
            description="Validates that the outline is usable",
            instruction=""""
            Check the outline in state `blog_outline`. If it has a title, intro, 4-6 sections, and a conclusion, 
            respond exactly "ok".
            Otherwise respond exactly "retry" and list missing pieces.
            """,
            output_key="validation_result",
        )


# Sub-Agent: Planner
blog_planner = Agent(
    name="BlogPlanner",
    model=GEN_MODEL,
    description="Create a practical, skimmable outline in Markdown.",
    instruction="""
    You are a technical content strategist. Produce a clear Markdown outline with:
    - Title
    - Short intro
    - 4-6 main sections (each with 2-3 bullets)
    - Conclusion

    If `codebase_context` exists in state, weave in specific sections/snippets.
    Return only the outline in Markdown
    """,
    output_key="blog_outline",
)


robust_blog_planner = LoopAgent(
    name="RobustBlogPlanner",
    description="Retries planning if validation fails.",
    sub_agents=[blog_planner,OutlineValidationChecker()],
    max_iterations=3,
)