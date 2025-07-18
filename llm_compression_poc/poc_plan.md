# Sub-Plan: LLM Model Compression PoC

This document outlines the plan for the Proof of Concept (PoC) focused on compressing a large language model for on-device use.

### Objective

The goal is to convert a general-purpose, open-source language model into a compressed format that is highly optimized for Apple's Core ML framework.

### Plan

1.  **Choose a Base Model:**
    *   **Model:** `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
    *   **Rationale:** This model is small enough to be manageable for a PoC while being powerful enough to demonstrate a realistic conversion process.

2.  **Create a Conversion Script:**
    *   A Python script will be created to automate the conversion.
    *   **Libraries:** The script will use `transformers`, `torch`, and Apple's `coremltools`.
    *   **Process:**
        1.  Download the TinyLlama model from the Hugging Face Hub.
        2.  Convert the model into the Core ML format (`.mlpackage`).
        3.  Apply **4-bit quantization** during the conversion to significantly compress the model's size.

3.  **Deliverables:**
    *   **A runnable, minimal iOS application.**
    *   The app will load the compressed Core ML model.
    *   It will run a single inference on a pre-defined input.
    *   It will display the raw model output to confirm successful execution.
    *   This deliverable also includes the `convert_model.py` script and `requirements.txt` needed to generate the model asset.

This PoC will validate the end-to-end technical feasibility of converting, compressing, and executing a custom LLM on an iOS device.
