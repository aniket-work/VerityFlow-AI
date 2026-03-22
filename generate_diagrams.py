import base64
import requests
import os

# Ensure images directory exists
os.makedirs("images", exist_ok=True)

diagrams = {
    "title_diagram": """
graph TB
    subgraph "VerityFlow-AI Swarm"
        L[Lead Investigator]
        A[Cross-Reference Analyst]
        B[Bias Auditor]
        S[Contextual Synthesizer]
    end
    News[Trending News Story] --> L
    L -->|Investigative Priorities| A
    A -->|Verified Facts| B
    B -->|Neutrality Audit| S
    S -->|Verity Report| Output[Deep-Context Narrative]
    style L fill:#4A90E2,stroke:#333,stroke-width:2px
    style A fill:#50E3C2,stroke:#333,stroke-width:2px
    style B fill:#F5A623,stroke:#333,stroke-width:2px
    style S fill:#BD10E0,stroke:#333,stroke-width:2px
""",
    "architecture_diagram": """
graph LR
    User[Topic Input] --> Main[main.py: Swarm Controller]
    Main --> Agents[engine/agents.py: VerityAgents]
    Main --> Tasks[engine/tasks.py: VerityTasks]
    Agents --> Gemini[Gemini 1.5 Flash Model]
    Tasks --> Crew[CrewAI Orchestrator]
    Crew --> Results[Multi-Format Output]
""",
    "sequence_diagram": """
sequenceDiagram
    participant User
    participant Lead as Lead Investigator
    participant Analyst as Cross-Ref Analyst
    participant Auditor as Bias Auditor
    participant Synth as Context Synth
    User->>Lead: Topic Input
    Lead->>Analyst: Investigative Priorities
    Analyst->>Auditor: Fact-Check Report
    Auditor->>Synth: Neutrality/Bias Audit
    Synth->>User: Comprehensive Verity Report
""",
    "flow_diagram": """
flowchart TD
    Start[New News Event] --> Identify[Identify Core Claims]
    Identify --> Verify[Verify against Global Archives]
    Verify --> Audit[Audit for Bias and Framing]
    Audit --> Synthesize[Synthesize Contextual Narrative]
    Synthesize --> Final[Final Professional Report]
"""
}

def generate_diagrams():
    print("--- Generating Technical Mermaid Diagrams ---")
    for name, code in diagrams.items():
        try:
            # Fix: Ensure no extra whitespace and base64 encode
            clean_code = code.strip()
            encoded = base64.b64encode(clean_code.encode()).decode()
            url = f"https://mermaid.ink/img/{encoded}"
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"images/{name}.png", 'wb') as f:
                    f.write(response.content)
                print(f"Successfully generated: images/{name}.png")
            else:
                print(f"Failed to generate {name}: HTTP {response.status_code}")
        except Exception as e:
            print(f"Error generating {name}: {str(e)}")

if __name__ == "__main__":
    generate_diagrams()
