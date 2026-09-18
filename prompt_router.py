"""Deterministic prompt routing for small AI automations."""

from dataclasses import dataclass
import re
import sys


@dataclass(frozen=True)
class Route:
    task: str
    system_prompt: str
    confidence: float


RULES = (
    ("support", re.compile(r"\b(refund|return|order|delivery|shipment|invoice)\b", re.I),
     "You are a concise customer support agent. Use only verified order data."),
    ("extract", re.compile(r"\b(extract|parse|fields|json|structured)\b", re.I),
     "Extract the requested fields. Return valid JSON and no commentary."),
    ("summarize", re.compile(r"\b(summarize|summary|tldr|shorten)\b", re.I),
     "Summarize the input faithfully in clear, compact bullet points."),
)


def route(text: str) -> Route:
    """Choose a prompt strategy without calling a model."""
    if not text or not text.strip():
        raise ValueError("text must not be empty")
    for task, pattern, prompt in RULES:
        if pattern.search(text):
            return Route(task, prompt, 0.9)
    return Route("general", "Answer helpfully, state uncertainty, and ask for missing context.", 0.4)


if __name__ == "__main__":
    decision = route(" ".join(sys.argv[1:]))
    print(f"task={decision.task}\nconfidence={decision.confidence}\nsystem={decision.system_prompt}")
