from google.cloud.language import enums, types


def process_text_to_analyze(sentences: list):
    documents = []
    for sentence in sentences:
        document = types.Document(
            content=sentence,
            type=enums.Document.Type.PLAIN_TEXT
        )
        documents.append(document)
    return documents
