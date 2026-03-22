from crewai import Crew, Process
from engine.agents import VerityAgents
from engine.tasks import VerityTasks
import os
from dotenv import load_dotenv

load_dotenv()

def run_verity_swarm(topic):
    # Initialize Agents
    agents = VerityAgents()
    lead = agents.lead_investigator()
    analyst = agents.cross_reference_analyst()
    auditor = agents.bias_auditor()
    synthesizer = agents.contextual_synthesizer()

    # Initialize Tasks
    tasks = VerityTasks()
    t1 = tasks.identification_task(lead, topic)
    t2 = tasks.validation_task(analyst, [t1])
    t3 = tasks.audit_task(auditor, [t2])
    t4 = tasks.synthesis_task(synthesizer, [t1, t2, t3])

    # Form the Crew
    verity_crew = Crew(
        agents=[lead, analyst, auditor, synthesizer],
        tasks=[t1, t2, t3, t4],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = verity_crew.kickoff()
    return result

if __name__ == "__main__":
    print("--- VerityFlow-AI: Starting Swarm ---")
    topic = "The impact of synthetic media on democratic elections in 2026"
    report = run_verity_swarm(topic)
    print("\n\n--- FINAL VERITY REPORT ---")
    print(report)
