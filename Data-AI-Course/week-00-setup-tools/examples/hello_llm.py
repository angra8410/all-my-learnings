"""
Simple LLM Chat Application
Week 00 - Setup & Tools

A basic interactive chat application using OpenAI's GPT models.
Demonstrates fundamental LLM API usage.

Usage: python hello_llm.py
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()


def chat_with_gpt(
    prompt: str,
    model: str = "gpt-3.5-turbo",
    temperature: float = 0.7,
    max_tokens: int = 500
) -> dict:
    """
    Send a prompt to GPT and return the response with metadata.
    
    Args:
        prompt: The user's question or instruction
        model: OpenAI model to use
        temperature: Sampling temperature (0.0 to 2.0)
        max_tokens: Maximum tokens in response
        
    Returns:
        Dictionary with response and metadata
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    return {
        "content": response.choices[0].message.content,
        "tokens": response.usage.total_tokens,
        "model": response.model,
        "finish_reason": response.choices[0].finish_reason
    }


def print_response(result: dict):
    """Pretty print the response."""
    print(f"\n🤖 Assistant: {result['content']}")
    print(f"\n📊 Tokens: {result['tokens']} | Model: {result['model']}")


def main():
    """Interactive chat loop."""
    print("=" * 70)
    print("🚀 Simple LLM Chat - Week 00")
    print("=" * 70)
    print("\nCommands:")
    print("  - Type your message and press Enter")
    print("  - Type 'quit' or 'exit' to end")
    print("  - Type 'help' for more options")
    print("\n" + "=" * 70)
    
    # Configuration
    temperature = 0.7
    max_tokens = 500
    model = "gpt-3.5-turbo"
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Goodbye!")
                break
            
            elif user_input.lower() == 'help':
                print("\n📖 Available commands:")
                print("  quit/exit/q  - Exit the chat")
                print("  help         - Show this help")
                print("  temp <0-2>   - Set temperature (e.g., 'temp 0.5')")
                print("  model <name> - Set model (e.g., 'model gpt-4')")
                print("  info         - Show current settings")
                continue
            
            elif user_input.lower().startswith('temp '):
                try:
                    temperature = float(user_input.split()[1])
                    temperature = max(0.0, min(2.0, temperature))
                    print(f"✅ Temperature set to {temperature}")
                except (ValueError, IndexError):
                    print("❌ Invalid temperature. Use: temp <0.0-2.0>")
                continue
            
            elif user_input.lower().startswith('model '):
                try:
                    model = user_input.split(maxsplit=1)[1]
                    print(f"✅ Model set to {model}")
                except IndexError:
                    print("❌ Invalid model. Use: model <model-name>")
                continue
            
            elif user_input.lower() == 'info':
                print(f"\n⚙️  Current Settings:")
                print(f"   Model: {model}")
                print(f"   Temperature: {temperature}")
                print(f"   Max Tokens: {max_tokens}")
                continue
            
            # Regular chat message
            print("\n⏳ Thinking...")
            result = chat_with_gpt(
                prompt=user_input,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens
            )
            print_response(result)
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please check your API key and internet connection.")


if __name__ == "__main__":
    # Check if API key is configured
    if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY").startswith("<YOUR_"):
        print("❌ Error: OPENAI_API_KEY not configured")
        print("\nPlease:")
        print("1. Create a .env file in the project root")
        print("2. Add: OPENAI_API_KEY=your-api-key-here")
        print("3. Get your API key from: https://platform.openai.com/api-keys")
    else:
        main()
