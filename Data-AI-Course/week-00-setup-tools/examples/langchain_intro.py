"""
LangChain Introduction - Quick Start
Week 00 - Setup & Tools

Demonstrates basic LangChain usage including:
- Prompt templates
- Chain composition
- Output parsing

Usage: python langchain_intro.py
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# Load environment variables
load_dotenv()


def example_1_basic_chain():
    """Example 1: Basic chain with prompt template."""
    print("=" * 70)
    print("Example 1: Basic Chain with Prompt Template")
    print("=" * 70)
    
    # Initialize model
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful {role}."),
        ("user", "{question}")
    ])
    
    # Create chain
    chain = prompt | llm | StrOutputParser()
    
    # Test the chain
    result = chain.invoke({
        "role": "Python expert",
        "question": "What is a decorator in Python? Explain in one sentence."
    })
    
    print(f"\nResponse: {result}")


def example_2_multiple_prompts():
    """Example 2: Testing with different roles."""
    print("\n" + "=" * 70)
    print("Example 2: Multiple Roles")
    print("=" * 70)
    
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a {role}. Answer in {style}."),
        ("user", "{question}")
    ])
    
    chain = prompt | llm | StrOutputParser()
    
    # Test different combinations
    tests = [
        {
            "role": "Data scientist",
            "style": "one sentence",
            "question": "What is overfitting?"
        },
        {
            "role": "DevOps engineer",
            "style": "bullet points",
            "question": "What is CI/CD?"
        },
        {
            "role": "Technical writer",
            "style": "simple terms for beginners",
            "question": "What is an API?"
        }
    ]
    
    for i, test in enumerate(tests, 1):
        print(f"\n{i}. Role: {test['role']}")
        print(f"   Question: {test['question']}")
        result = chain.invoke(test)
        print(f"   Response: {result}")


def example_3_conversation_chain():
    """Example 3: Multi-turn conversation."""
    print("\n" + "=" * 70)
    print("Example 3: Conversation Chain")
    print("=" * 70)
    
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Create a prompt for multi-turn conversation
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful coding tutor."),
        ("user", "{input}")
    ])
    
    chain = prompt | llm | StrOutputParser()
    
    # Simulate a conversation
    conversation = [
        "Explain what a for loop does",
        "Can you give me an example in Python?",
        "What's the difference between a for loop and a while loop?"
    ]
    
    for i, message in enumerate(conversation, 1):
        print(f"\n{i}. User: {message}")
        response = chain.invoke({"input": message})
        print(f"   Assistant: {response}")


def example_4_structured_output():
    """Example 4: Structured output with formatting."""
    print("\n" + "=" * 70)
    print("Example 4: Structured Output")
    print("=" * 70)
    
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.5,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Prompt for structured output
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a technical expert. 
        Answer questions in this exact format:
        
        Definition: [one line]
        Key Points:
        - [point 1]
        - [point 2]
        - [point 3]
        Example: [brief example]
        """),
        ("user", "{topic}")
    ])
    
    chain = prompt | llm | StrOutputParser()
    
    topics = ["REST API", "Docker container", "Git branch"]
    
    for topic in topics:
        print(f"\n📖 Topic: {topic}")
        result = chain.invoke({"topic": f"Explain {topic}"})
        print(result)


def example_5_temperature_comparison():
    """Example 5: Compare different temperature settings."""
    print("\n" + "=" * 70)
    print("Example 5: Temperature Comparison")
    print("=" * 70)
    
    question = "Write a creative tagline for an AI coding assistant"
    
    temperatures = [0.0, 0.5, 1.0, 1.5]
    
    for temp in temperatures:
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=temp,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a creative copywriter."),
            ("user", "{input}")
        ])
        
        chain = prompt | llm | StrOutputParser()
        
        result = chain.invoke({"input": question})
        print(f"\n🌡️  Temperature: {temp}")
        print(f"   Response: {result}")


def main():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("🔗 LANGCHAIN INTRODUCTION - Week 00")
    print("=" * 70)
    
    # Check API key
    if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY").startswith("<YOUR_"):
        print("\n❌ Error: OPENAI_API_KEY not configured")
        print("Please set up your .env file with your OpenAI API key")
        return
    
    print("\nThis script demonstrates basic LangChain concepts:")
    print("1. Prompt templates")
    print("2. Chain composition")
    print("3. Output parsing")
    print("4. Parameter tuning")
    
    print("\n⏳ Running examples... (this may take a minute)")
    
    try:
        example_1_basic_chain()
        example_2_multiple_prompts()
        example_3_conversation_chain()
        example_4_structured_output()
        example_5_temperature_comparison()
        
        print("\n" + "=" * 70)
        print("✅ All examples completed successfully!")
        print("=" * 70)
        print("\n💡 Key Takeaways:")
        print("   • Prompt templates make prompts reusable")
        print("   • Chains compose multiple steps")
        print("   • Temperature affects creativity")
        print("   • System messages set behavior")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        print("Check your API key and internet connection")


if __name__ == "__main__":
    main()
