import Foundation

struct JournalEntry: Identifiable {
    let id = UUID()
    let title: String
    let body: String
    let date: Date
}

let dummyEntries = [
    JournalEntry(title: "First Entry", body: "This is the body of the first journal entry.", date: Date()),
    JournalEntry(title: "Second Entry", body: "This is the body of the second journal entry.", date: Date().addingTimeInterval(-86400)),
    JournalEntry(title: "Third Entry", body: "This is the body of the third journal entry.", date: Date().addingTimeInterval(-172800))
]
