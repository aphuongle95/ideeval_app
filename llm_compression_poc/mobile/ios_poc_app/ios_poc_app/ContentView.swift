import SwiftUI
import SwiftLlama

struct ContentView: View {
    @State private var result = ""
    let modelPath = Bundle.main.path(forResource: "your_model", ofType: "gguf")!

    var body: some View {
        VStack {
            Button("Run Llama") {
                Task {
                    do {
                        let llama = try SwiftLlama(modelPath: modelPath)
                        let response = try await llama.start(for: "Hello, Llama!")
                        result = response
                    } catch {
                        result = "Error: \(error)"
                    }
                }
            }
            Text(result)
                .padding()
        }
    }
}
