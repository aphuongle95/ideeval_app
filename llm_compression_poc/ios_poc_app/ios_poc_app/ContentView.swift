import SwiftUI

struct ContentView: View {
    let entries = dummyEntries
    
    var body: some View {
        NavigationView {
            List(entries) { entry in
                VStack(alignment: .leading) {
                    Text(entry.title)
                        .font(.headline)
                    Text(entry.body)
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                }
            }
            .navigationTitle("Journal")
        }
    }
}

#Preview {
    ContentView()
}
