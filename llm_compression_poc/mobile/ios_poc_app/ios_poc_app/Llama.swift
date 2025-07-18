
import Foundation
import LlamaFramework

class LlamaState: ObservableObject {
    @Published var responseText = ""
    private var llama: Llama?

    init() {
        // Don't load the model in SwiftUI previews
        if ProcessInfo.processInfo.environment["XCODE_RUNNING_FOR_PREVIEWS"] == "1" {
            self.responseText = "Model response appears here."
            return
        }

        // Hard-coded model filename for now
        let modelName = "Llama-3.2-1B-Instruct-Q4_K_M"
        guard let modelPath = Bundle.main.path(forResource: modelName, ofType: "gguf") else {
            print("Error: Model file not found")
            self.responseText = "Error: Model file not found. Make sure you've added it to the 'Copy Bundle Resources' build phase."
            return
        }

        do {
            self.llama = try Llama(modelPath: modelPath)
        } catch {
            print("Error initializing Llama: \(error)")
            self.responseText = "Error initializing Llama: \(error)"
        }
    }

    @MainActor
    func runInference(prompt: String) async {
        guard let llama = llama else {
            self.responseText = "Llama model is not available."
            return
        }
        do {
            let response = try await llama.start(for: prompt)
            self.responseText = response
        } catch {
            self.responseText = "Error: \(error)"
        }
    }
}