from es_yoda_ner import load

Entity = tuple[str, str, int, int]
Entities = list[Entity]

ner = load()


def get_ents(text: str) -> Entities:
    doc = ner(text)

    ents: Entities = []

    for token in doc:
        print(token.morph)

    for ent in doc.ents:
        first_word = ent.text
        is_size_tag_and_not_number = ent.label_ == "size" and not first_word.isdigit()
        if is_size_tag_and_not_number:
            continue
        ents.append((ent.label_, first_word, ent.start_char, ent.end_char))

    return ents
