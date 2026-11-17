
from services.config.workout_config import PROMPT
import groq


class LLMCoach:
    def __init__(self, groq_client):
        self.client = groq_client
        self.history = []
        self.system_prompt = PROMPT

    def give_feedback(self, event, issue):
        prompt = f"Event: {event}"

        if issue:
            prompt += f" Form Issue: {issue}"

        messages = [
            {"role": "system", "content": self.system_prompt},
            *self.history[-10:],
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=messages,
                temperature=0.4,
                max_completion_tokens=500,
            )

            text = response.choices[0].message.content.strip()

            self.history.append({
                "role": "assistant",
                "content": text
            })

            return text

        except groq.APIError as e:
            print(f"Groq API Error: {e}")
            return "I'm temporarily unable to generate AI feedback. Please continue your workout."
