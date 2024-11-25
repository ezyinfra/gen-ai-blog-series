# Run LLM models locally

This demo app shows how to run LLM models locally and interact with them.

This is a Python / Poetry / FastAPI based app that uses the `openai` library to interact with the LLM models. You can run it locally or in the cloud using the env variable `RUN_IN_CLOUD=true`.

Actual logic to interact with the LLM model is in the `local_llm_model/model_serving.py` file.

## Installation

1. Install Poetry 

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies

```bash
poetry install
```

3. Set the environment variables

```bash
# Update the .env file with your OpenAI API key and model name
cp .env.template .env
vi .env
```

## For local development

```bash
# .env file should be,

RUN_IN_CLOUD=false
OPENAI_API_KEY=dummy-api-key
MODEL_NAME=llama3.2
```

## Deploying to cloud

```bash
# .env file should be,

RUN_IN_CLOUD=true
OPENAI_API_KEY=<your-openai-api-key>
MODEL_NAME=gpt-4o-mini
```

4. Run the app

```bash
poetry run ./run.sh
```
