import spacy
import neuralcoref

nlp = spacy.load("en_core_web_sm")
neuralcoref.add_to_pipe(nlp)

text = "John went to the store. He bought milk."
doc = nlp(text)

print("Original Text:")
print(text)

print("\nResolved Text:")
print(doc._.coref_resolved)
