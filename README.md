# AI Prompt Router

Small, dependency-free Python router for sending requests to the right prompt strategy by task type. Useful as a first layer in AI agents and support automations.

## Usage

```bash
python -m prompt_router "Summarize this customer message"
python -m unittest -v
```

The router returns a structured decision containing the task, system prompt, and confidence. Add providers behind the decision without coupling business logic to a model vendor.

## Design

Rules are explicit, deterministic, and easy to replace with an LLM classifier when needed. The package uses only the Python standard library.

## License

MIT
