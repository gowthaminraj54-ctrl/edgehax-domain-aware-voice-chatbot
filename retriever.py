def load_knowledge(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    chunks = text.split("\n\n")
    return chunks


def retrieve(query, chunks):
    query = query.lower()
    results = []

    for chunk in chunks:
        if any(word in chunk.lower() for word in query.split()):
            results.append(chunk)

    return results[:2] if results else []
