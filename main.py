#!/usr/bin/env python3
"""
Automated hackmerlin.io puzzle solver using Browser Use.
"""

import os
import asyncio
from dotenv import load_dotenv
from browser_use import Agent, Browser
from openai import OpenAI

# Load environment variables
load_dotenv()

# System prompt for the agent
SYSTEM_PROMPT = """You are an AI agent designed to solve puzzles on hackmerlin.io. 

Key instructions:
1. When the puzzle asks for a "one-token" answer, provide exactly one word or token as your response.
2. When the puzzle asks for "uppercase" answers, make sure to use ALL CAPS.
3. Pay close attention to formatting requirements - if you get feedback hinting at formatting errors, retry once with the correct format.
4. For yes/no questions, respond with exactly "YES" or "NO" in uppercase.
5. For multiple choice questions, click the correct option based on the puzzle logic.
6. Think step by step and analyze each puzzle carefully before responding.
7. If you're unsure about a puzzle, try to break it down into smaller parts.

Your goal is to solve as many puzzles as possible on hackmerlin.io. Start by navigating to the website and begin solving puzzles."""

async def main():
    """Main function to run the hackmerlin.io solver."""
    
    # Check if OpenAI API key is set
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please set your OpenAI API key in the .env file.")
        return
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Initialize browser
    browser = Browser()
    
    # Initialize agent with system prompt
    agent = Agent(
        browser=browser,
        planner=client.chat.completions,
        model="gpt-4o-mini",
        system_prompt=SYSTEM_PROMPT
    )
    
    try:
        # Start by navigating to hackmerlin.io
        print("🚀 Starting hackmerlin.io puzzle solver...")
        print("📱 Opening https://hackmerlin.io...")
        
        # Navigate to the website
        await agent.run("Navigate to https://hackmerlin.io and start solving puzzles")
        
        # Main solving loop
        print("\n🎯 Beginning puzzle solving...")
        print("=" * 50)
        
        # Run the agent and print each step
        async for step in agent.run_iter("Solve the current puzzle and continue to the next one"):
            print(f"\n📝 Step: {step.action}")
            if step.observation:
                print(f"👁️  Observation: {step.observation[:200]}...")
            print("-" * 30)
            
    except KeyboardInterrupt:
        print("\n⏹️  Stopping solver...")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        await browser.close()
        print("🔚 Browser closed.")

if __name__ == "__main__":
    asyncio.run(main())
