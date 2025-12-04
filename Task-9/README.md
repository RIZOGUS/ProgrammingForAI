# NLP Demo: Stemming and Lemmatization

A Python demonstration of **Stemming** and **Lemmatization** using NLTK (Natural Language Toolkit).

## 📚 What is Stemming and Lemmatization?

### Stemming

Stemming is a crude heuristic process that chops off the ends of words to reduce them to a common base form. It doesn't consider the context or grammatical rules.

**Example**:

- "Running" → "Run"
- "Studies" → "Studi"

### Lemmatization

Lemmatization uses vocabulary and morphological analysis to return the base or dictionary form of a word (called a **lemma**). It considers the context and part of speech.

**Example**:

- "Running" (verb) → "run"
- "Studies" (noun) → "study"
- "Better" (adjective) → "good"

## 🛠️ Setup & Installation

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Demo**:

   ```bash
   python nlp_demo.py
   ```

The script will automatically download required NLTK data (`wordnet`, `omw-1.4`, `punkt`) on first run.

## 📊 Sample Output

```
Original        | Stemming (Porter)    | Lemmatization (WordNet)
-----------------------------------------------------------------
Running         | run                  | run
Studies         | studi                | study
Better          | better               | good
Cacti           | cacti                | cactus
Am              | am                   | be
Mice            | mice                 | mouse
```

## 🔍 Key Differences

| Feature | Stemming | Lemmatization |
|---------|----------|---------------|
| Accuracy | Less accurate | More accurate |
| Speed | Faster | Slower |
| Output | May not be real words | Always real words |
| Context | Ignores context | Uses context/POS |

## 💡 Use Cases

- **Stemming**: Search engines, information retrieval (where speed matters)
- **Lemmatization**: Text analysis, sentiment analysis, NLP pipelines (where accuracy matters)
