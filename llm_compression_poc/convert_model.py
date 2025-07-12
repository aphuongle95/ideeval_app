
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import coremltools as ct
from dotenv import load_dotenv
import os

def main():
    """
    Downloads a model from Hugging Face, converts it to Core ML, and applies quantization.
    """
    load_dotenv()
    hf_token = os.getenv("HUGGING_FACE_HUB_TOKEN")
    
    model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
    
    # Download model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=hf_token)
    model = AutoModelForCausalLM.from_pretrained(model_name, token=hf_token)
    
    # Create dummy input
    dummy_input = tokenizer("Hello, my name is", return_tensors="pt")
    
    # Trace the model
    traced_model = torch.jit.trace(model, (dummy_input['input_ids'], dummy_input['attention_mask']))
    
    # Convert to Core ML
    mlmodel = ct.convert(
        traced_model,
        convert_to="mlprogram",
        inputs=[
            ct.TensorType(name="input_ids", shape=(1, ct.Range(1, 2048)), dtype=torch.int32),
            ct.TensorType(name="attention_mask", shape=(1, ct.Range(1, 2048)), dtype=torch.int32),
        ],
        compute_units=ct.ComputeUnit.CPU_AND_GPU,
    )
    
    # Quantize the model
    op_config = ct.optimize.coreml.OpPalettizerConfig(
        mode="uniform", nbits=4, weight_threshold=512
    )
    config = ct.optimize.coreml.OptimizationConfig(global_config=op_config)
    quantized_model = ct.optimize.coreml.palettize_weights(mlmodel, config=config)
    
    # Save the model
    quantized_model.save("Llama3.mlpackage")

if __name__ == "__main__":
    main()
