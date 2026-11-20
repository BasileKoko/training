from planner_tool.blog_planner_agent import GEN_MODEL
from google.adk.agents import Agent, LoopAgent

class BlogPostValidationChecker(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            name="BlogPostValidationChecker",
            model=GEN_MODEL,
            description="validates the final post",
            instruction=""""
            Check `blog_post` for: into, clear sections matching the outline,
            conclusion, and technical clarity.
            If passes, respond "ok". Else respond "retry" with specific fixes.
            """,
            output_key="validation_result"
        )

# Sub-Agent: Writer
blog_writer = Agent(
    name="BlogWriter",
    model=GEN_MODEL,
    description="Write a technical blog post from the outline.",
    instruction="""
    Write a complete Markdown article from the outline in `blog_outline`.

    Guidelines:
    - Audience: software engineers; skip basics and focus on practical insight.
    - Explain both the `how` and `why`.
    - Include concise code snippets when helpful.
    - Follow the outline's structure (H2/H3)
    _ Output only the final article in Markdown (no fence around the whole post)
    """,
    output_key="blog_post",
)

robust_blog_writer = LoopAgent(
    name="RobustBlogWriter",
    description="Retries writing if validation fails.",
    sub_agents=[blog_writer, BlogPostValidationChecker()],
    max_iterations=3,
)