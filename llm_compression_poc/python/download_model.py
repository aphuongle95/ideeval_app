from huggingface_hub import hf_hub_download
import os
from dotenv import load_dotenv

def main():
    """
    Downloads a GGUF model from Hugging Face.
    """
    dotenv_path = "/Users/yenphuong/Code/AI_on_the_go/ideeval_app/llm_compression_poc/.env"
    load_dotenv(dotenv_path=dotenv_path)
    hf_token = os.getenv("HUGGING_FACE_HUB_TOKEN")

    if not hf_token:
        raise ValueError(f"HUGGING_FACE_HUB_TOKEN not found in {dotenv_path}")

    repo_id = "bartowski/Llama-3.2-1B-Instruct-GGUF"
    filename = "Llama-3.2-1B-Instruct-Q4_K_M.gguf"
    output_path = "/Users/yenphuong/Code/AI_on_the_go/ideeval_app/llm_compression_poc/models"
    
    hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        local_dir=output_path,
        local_dir_use_symlinks=False,
        token=hf_token
    )

if __name__ == "__main__":
    main()