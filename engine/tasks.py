from crewai import Task

class VerityTasks:
    def identification_task(self, agent, topic):
        return Task(
            description=f"Identify the core claims and potential misinformation triggers in the trending news regarding: {topic}. Provide a concise list of points that need verification.",
            expected_output="A list of specific claims and investigative priorities for the validation team.",
            agent=agent
        )

    def validation_task(self, agent, context):
        return Task(
            description="Using the investigative priorities identified, cross-reference each claim against global news archives and official datasets. Confirm or debunk each claim with evidence.",
            expected_output="An evidence-based validation report for each flagged claim, cited with sources.",
            agent=agent,
            context=context
        )

    def audit_task(self, agent, context):
        return Task(
            description="Evaluate the primary sources of the news story for bias, emotional manipulation, and framing. Identify whose interests are served by the narrative.",
            expected_output="A detailed bias and sentiment audit report, highlighting cognitive biases and manipulation tactics.",
            agent=agent,
            context=context
        )

    def synthesis_task(self, agent, context):
        return Task(
            description="Synthesize the investigative findings, validations, and bias audits into a final 'Verity Report'. Ensure the tone is professional, objective, and provides historical context for the event.",
            expected_output="A comprehensive 2000-word 'Verity Report' that serves as the definitive source of truth for the topic.",
            agent=agent,
            context=context
        )
