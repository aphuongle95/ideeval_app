# Python Best Practices

- Use virtual environments (e.g., `venv`, `conda`) for dependency isolation.
- List all dependencies in `requirements.txt` and keep it updated.
- Follow PEP8 for code style and formatting (use `black` or `flake8`).
- Write modular, reusable code and document all functions/classes.
- Never hardcode secrets, credentials, or environment-specific values—use configuration files or environment variables instead.
- Use logging instead of print statements for debug/info output.
- Store secrets and API keys in a `.env` file, never in code.
- Write unit tests and keep them in a `tests/` or `*_test.py` files.
- Clean up temporary files and caches after experiments.
- Document all experiments and findings in a `research/` or `logs/` folder.
