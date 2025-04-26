
from semantic_kernel.orchestration.sk_context import SKContext
from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter

class BillingAgent:
    @sk_function(name="BillingAgent", description="Handles billing related queries")
    @sk_function_context_parameter(name="input", description="The customer query")
    async def handle(self, context: SKContext) -> str:
        return f"[BillingAgent] Answering billing query: {context.variables['input']}"

