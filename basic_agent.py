
import asyncio
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
from datetime import datetime
import time


class MyBehaviour(PeriodicBehaviour):
    """
    A simple periodic behaviour that runs every 5 seconds.
    This demonstrates basic agent activity and autonomous behavior.
    """
    
    async def run(self):
        """
        This method is called every 5 seconds (as defined by the period).
        It prints a status message showing the agent is active.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"MyBehaviour running - Current time: {current_time}")
        print(f"Agent is active and monitoring...")


class BasicAgent(Agent):
    """
    BasicAgent: A simple SPADE agent for LAB 1
    
    This agent:
    - Connects to an XMPP server
    - Runs a periodic behavior every 5 seconds
    - Demonstrates basic agent functionality
    """
    
    async def setup(self):
        """
        Setup method called when the agent starts.
        Here we initialize the agent's behaviors.
        """
        print(f"Agent {self.jid} is starting...")
        
        behaviour = MyBehaviour(period=5)
        
        self.add_behaviour(behaviour)
        
        print(f"Agent {self.jid} is running")


async def main():
    
    XMPP_SERVER = "xmpp.jp"
    AGENT_JID = "joeboy77@xmpp.jp"  
    AGENT_PASSWORD = "Joseph66715"    
    
    print("=" * 50)
    print("LAB 1: Basic SPADE Agent")
    print("=" * 50)
    print(f"Connecting to: {XMPP_SERVER}")
    print(f"Agent JID: {AGENT_JID}")
    print("=" * 50)
    
    agent = BasicAgent(AGENT_JID, AGENT_PASSWORD)
    
    await agent.start()
    
    print("Agent started successfully!")
    print("Press Ctrl+C to stop the agent...")
    print("=" * 50)
    

    try:
        while agent.is_alive():
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("\n" + "=" * 50)
        print("Stopping agent...")
        print("=" * 50)
    
    # Stop the agent
    await agent.stop()
    print("Agent stopped successfully!")


if __name__ == "__main__":
    """
    Entry point of the program.
    Runs the main coroutine using asyncio.
    """
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Please check your credentials and internet connection.")