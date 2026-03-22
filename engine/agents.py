from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

class VerityAgents:
    def lead_investigator(self):
        return Agent(
            role="Lead Investigative Journalist",
            goal="Identify trending news stories and flag potential misinformation or controversial claims for deep-dive investigation.",
            backstory="You are a veteran investigative journalist with a 'nose for news'. You excel at spotting patterns of misinformation and identifying which stories require urgent validation to protect public discourse.",
            llm=llm,
            allow_delegation=False,
            verbose=True
        )

    def cross_reference_analyst(self):
        return Agent(
            role="Cross-Reference Data Analyst",
            goal="Verify claims made in a news story by searching across diverse, reputable global databases and social media archives.",
            backstory="You are a data-driven analyst who believes only in hard evidence. You cross-reference claims against multiple independent sources to establish a ground truth.",
            llm=llm,
            allow_delegation=False,
            verbose=True
        )

    def bias_auditor(self):
        return Agent(
            role="Bias & Sentiment Auditor",
            goal="Analyze the tone, sentiment, and potential political or corporate bias of a news source or claim.",
            backstory="You are an expert in media linguistics and political science. You detect subtle biases and emotional triggers used to manipulate public opinion.",
            llm=llm,
            allow_delegation=False,
            verbose=True
        )

    def contextual_synthesizer(self):
        return Agent(
            role="Contextual Narrative Synthesizer",
            goal="Synthesize the findings from all agents into a professional, non-partisan, and deeply contextual report.",
            backstory="You are a master storyteller who values nuance and historical context. You turn raw data and fact-checks into a comprehensive narrative that informs rather than inflames.",
            llm=llm,
            allow_delegation=False,
            verbose=True
        )
