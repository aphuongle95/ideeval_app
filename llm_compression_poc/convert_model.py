import torch
import coremltools as ct
from transformers import AutoModelForCausalLM, AutoTokenizer

def main():
    """Downloads a model, converts it to Core ML, and saves it."""
    
    model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    
    print(f"Starting download of {model_name}...")
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    print("Model and tokenizer downloaded successfully.")

    # --- Prepare for Conversion ---
    # 1. Set model to evaluation mode
    model.eval()
    
    # 2. Create example input
    # The tokenizer returns a dictionary, and we need the `input_ids` tensor.
    example_input = tokenizer("hello world", return_tensors="pt")
    
    # 3. Trace the model with the example input to get a ScriptModule
    print("Tracing model...")
    traced_model = torch.jit.trace(model, (example_input['input_ids'],))
    print("Model traced successfully.")

    # --- Set up Quantization ---
    # Use 4-bit palletization for significant compression
    quantization_config = ct.optimize.coreml.OpPalettizerConfig(
        mode="kmeans", nbits=4
    )
    
    # --- Convert to Core ML ---
    print("Starting Core ML conversion with quantization...")
    mlmodel = ct.convert(
        traced_model,
        convert_to="mlprogram",
        inputs=[ct.TensorType(shape=example_input['input_ids'].shape)],
        compute_units=ct.ComputeUnit.CPU_AND_NE, # Target CPU and Neural Engine
        optimization_config=ct.optimize.coreml.OptimizationConfig(global_config=quantization_config)
    )
    print("Model converted to Core ML successfully.")

    # --- Save the Model ---
    output_path = "TinyLlama-1.1B-Chat-v1.0-4bit.mlpackage"
    mlmodel.save(output_path)
    print(f"Model saved to {output_path}")

if __name__ == "__main__":
    main()
