from semantic_kernel.orchestration.sk_context import SKContext
from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter

class SupportAgent:
    @sk_function(name="SupportAgent", description="Handles technical product queries")
    @sk_function_context_parameter(name="input", description="The customer query")
    async def handle(self, context: SKContext) -> str:
        return f"[SupportAgent] Answering technical query: {context.variables['input']}"
