from services.gemini_chat_service import GeminiChatService
from core.pdf_processor import PDFProcessor
from core.doc_manager import DocumentManager
from agents.support_agent import SupportAgent
from agents.billing_agent import BillingAgent
from semantic_kernel.planners.basic_planner import BasicPlanner
from semantic_kernel.kernel import Kernel
from semantic_kernel.connectors.ai.google import GoogleAIPromptExecution
import os

async def handle_customer_request(query, doc_manager, gemini):
    similar_sections = doc_manager.search(query)
    context = f"Relevant context from documents:\n" + "\n".join(similar_sections)
    full_prompt = f"{context}\n\nCustomer query: {query}\n\nAnswer:"
    return gemini.generate_response(full_prompt)

async def main():
    pdf_processor = PDFProcessor()
    doc_manager = DocumentManager()
    gemini = GeminiChatService(api_key=os.getenv("GEMINI_API_KEY"))

    billing_sections = pdf_processor.extract_sections("data/billing_manual_.pdf")
    support_sections = pdf_processor.extract_sections("data/technical_manual_.pdf")
    doc_manager.add_sections("Billing", billing_sections)
    doc_manager.add_sections("Support", support_sections)

    kernel = Kernel()
    kernel.add_text_completion_service("google-gemini", GoogleAIPromptExecution(service=gemini))
    kernel.import_skill(BillingAgent(), skill_name="BillingAgent")
    kernel.import_skill(SupportAgent(), skill_name="SupportAgent")

    planner = BasicPlanner()

    while True:
        user_input = input("Ask a question (or 'exit'): ")
        if user_input.lower() == 'exit':
            break
        plan = await planner.create_plan(kernel, user_input)
        result = await plan.invoke(kernel.create_new_context(), input_vars={"input": user_input})
        print("\nAgent Response:", result)
        print("\nGemini Response:", await handle_customer_request(user_input, doc_manager, gemini))
