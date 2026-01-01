"""
TaxChatbotAgent - Context-aware chatbot for tax queries
Knows about user's tax details from frontend form submissions
"""
import os
import sys
from typing import Dict, List, Optional
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
import json

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()


class TaxChatbotAgent:
    """
    Context-aware chatbot that:
    1. Remembers user's tax details from form
    2. Answers tax-related questions
    3. Provides personalized advice
    4. Explains calculations
    """

    def __init__(self, api_key: Optional[str] = None):
        """Initialize chatbot"""
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found")

        self.client = genai.Client(api_key=self.api_key)
        self.model = "gemini-3-flash-preview"

        # Store conversation history
        self.conversation_history = []

        # Store user's tax context
        self.user_context = {}

        print("✓ TaxChatbotAgent initialized")

    def set_user_context(self, tax_data: Dict):
        """
        Store user's tax details from frontend form
        This makes the chatbot aware of their financial situation
        """
        self.user_context = {
            "gross_income": tax_data.get('gross_income', 0),
            "regime": tax_data.get('regime', 'unknown'),
            "deductions": tax_data.get('deductions', {}),
            "total_deductions": sum(tax_data.get('deductions', {}).values()),
            "taxable_income": tax_data.get('taxable_income', 0),
            "total_tax": tax_data.get('total_tax', 0),
            "effective_rate": tax_data.get('effective_tax_rate', 0),
            "risk_score": tax_data.get('risk_score', 0),
            "risk_level": tax_data.get('risk_level', 'UNKNOWN'),
            "compliance_score": tax_data.get('compliance_score', 0),
            "flags": tax_data.get('flags', []),
            "timestamp": datetime.now().isoformat()
        }

        print(f"✓ User context updated: Income ₹{self.user_context['gross_income']:,}, "
              f"Regime: {self.user_context['regime']}, "
              f"Risk: {self.user_context['risk_level']}")

    def get_context_summary(self) -> str:
        """Generate summary of user's tax context for Gemini"""
        if not self.user_context or self.user_context.get('gross_income', 0) == 0:
            return "No tax details available yet. User hasn't filled the form."

        ctx = self.user_context

        summary = f"""
USER'S TAX DETAILS (From Frontend Form):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Income Information:
  • Gross Annual Income: ₹{ctx['gross_income']:,}
  • Tax Regime: {ctx['regime'].upper()}
  • Total Deductions Claimed: ₹{ctx['total_deductions']:,}
  • Taxable Income: ₹{ctx['taxable_income']:,}

Tax Calculation Results:
  • Total Tax Payable: ₹{ctx['total_tax']:,}
  • Effective Tax Rate: {ctx['effective_rate']:.2f}%

Compliance & Risk Assessment:
  • Risk Score: {ctx['risk_score']:.2f} / 1.0
  • Risk Level: {ctx['risk_level']}
  • Compliance Score: {ctx['compliance_score']:.1f}%
"""

        if ctx['deductions']:
            summary += "\nDeductions Claimed:\n"
            for section, amount in ctx['deductions'].items():
                summary += f"  • {section}: ₹{amount:,}\n"

        if ctx['flags']:
            summary += "\n⚠️  Red Flags Detected:\n"
            for flag in ctx['flags']:
                summary += f"  • {flag}\n"

        summary += "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

        return summary

    def chat(self, user_message: str) -> str:
        """
        Chat with user - context-aware responses
        """

        # Build context-aware system prompt
        system_context = f"""
You are a helpful Indian tax expert chatbot. You are talking to a taxpayer who has just used
our tax calculator. You have access to their tax details and calculations.

IMPORTANT CONTEXT - USER'S TAX DETAILS:
{self.get_context_summary()}

Your role:
1. Answer their tax-related questions
2. Explain their tax calculation if asked
3. Provide personalized advice based on their situation
4. Suggest tax-saving strategies relevant to their income and regime
5. Explain any red flags or compliance issues
6. Be friendly, clear, and helpful
7. Use Indian Rupee (₹) format
8. Reference their specific numbers when relevant

Guidelines:
- If user asks about "my tax" or "my calculation", refer to the context above
- If user asks general questions, provide accurate Indian tax law info (FY 2024-25)
- Be concise but thorough
- Use bullet points for clarity
- Always be encouraging and supportive
"""

        # Build conversation for Gemini
        messages = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=system_context + "\n\nUser: " + user_message)]
            )
        ]

        # Add conversation history
        for msg in self.conversation_history[-4:]:  # Last 4 messages for context
            messages.append(
                types.Content(
                    role=msg['role'],
                    parts=[types.Part.from_text(text=msg['content'])]
                )
            )

        try:
            config = types.GenerateContentConfig(
                temperature=0.7,
            )

            response_text = ""
            for chunk in self.client.models.generate_content_stream(
                model=self.model,
                contents=messages,
                config=config,
            ):
                if chunk.text:
                    response_text += chunk.text

            # Store in history
            self.conversation_history.append({
                "role": "user",
                "content": user_message,
                "timestamp": datetime.now().isoformat()
            })
            self.conversation_history.append({
                "role": "assistant",
                "content": response_text,
                "timestamp": datetime.now().isoformat()
            })

            return response_text

        except Exception as e:
            return f"I apologize, I encountered an error: {str(e)}"

    def get_personalized_suggestions(self) -> List[str]:
        """Generate personalized tax-saving suggestions based on user context"""

        if not self.user_context or self.user_context.get('gross_income', 0) == 0:
            return ["Fill in your tax details first to get personalized suggestions!"]

        suggestions_prompt = f"""
Based on this taxpayer's details:
{self.get_context_summary()}

Provide 5 specific, actionable tax-saving suggestions for them.
Focus on:
1. Regime optimization
2. Unused deduction opportunities
3. Risk reduction strategies
4. Compliance improvements
5. Future tax planning

Return as a simple numbered list, be specific to their situation.
"""

        try:
            contents = [types.Content(role="user", parts=[types.Part.from_text(text=suggestions_prompt)])]
            config = types.GenerateContentConfig(temperature=0.7)

            response_text = ""
            for chunk in self.client.models.generate_content_stream(
                model=self.model,
                contents=contents,
                config=config,
            ):
                if chunk.text:
                    response_text += chunk.text

            # Parse into list
            lines = [line.strip() for line in response_text.split('\n') if line.strip() and any(c.isdigit() for c in line[:3])]
            return lines[:5] if lines else [response_text]

        except Exception as e:
            return [f"Error generating suggestions: {str(e)}"]

    def clear_context(self):
        """Clear user context and conversation history"""
        self.user_context = {}
        self.conversation_history = []
        print("✓ Context and history cleared")


def main():
    """Test chatbot"""
    print("\n" + "="*70)
    print("TAX CHATBOT - CONTEXT-AWARE TESTING")
    print("="*70 + "\n")

    chatbot = TaxChatbotAgent()

    # Simulate user filling form in frontend
    print("📝 Simulating user filling tax calculator form...\n")

    sample_tax_data = {
        "gross_income": 1200000,
        "regime": "old",
        "deductions": {
            "80C": 150000,
            "80D": 25000,
            "Standard Deduction": 50000
        },
        "taxable_income": 975000,
        "total_tax": 111800,
        "effective_tax_rate": 9.32,
        "risk_score": 0.0,
        "risk_level": "LOW",
        "compliance_score": 100.0,
        "flags": []
    }

    chatbot.set_user_context(sample_tax_data)

    # Test conversations
    test_questions = [
        "Can you explain how my tax was calculated?",
        "Is the old regime better for me?",
        "How can I save more tax?",
        "What does my risk score mean?",
    ]

    for i, question in enumerate(test_questions, 1):
        print(f"\n{'─'*70}")
        print(f"Q{i}: {question}")
        print(f"{'─'*70}\n")

        answer = chatbot.chat(question)
        print(f"🤖 Chatbot: {answer}\n")

    # Get personalized suggestions
    print("\n" + "="*70)
    print("PERSONALIZED SUGGESTIONS")
    print("="*70 + "\n")

    suggestions = chatbot.get_personalized_suggestions()
    for suggestion in suggestions:
        print(f"  {suggestion}")


if __name__ == "__main__":
    main()
