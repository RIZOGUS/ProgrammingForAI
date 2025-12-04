import nltk
from nltk.stem import PorterStemmer
import spacy

# Download necessary NLTK data for stemming
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("Downloading punkt...")
    nltk.download('punkt')

# Load spaCy model for better lemmatization
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("\nspaCy model not found. Installing...")
    print("Please run: python -m spacy download en_core_web_sm")
    print("Then restart this script.\n")
    exit(1)

def process_word_interactive():
    """Interactive mode where users can input words and get stemmed/lemmatized results."""
    stemmer = PorterStemmer()
    
    print("\n" + "="*70)
    print(" NLP Word Processor - Convert Words to Base Form")
    print("="*70)
    print("\nEnter any English word (including verb forms) to see its base form.")
    print("Examples: running, studied, ran, went, better, mice")
    print("Type 'quit' or 'exit' to stop.\n")
    
    while True:
        user_input = input("Enter a word: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!")
            break
        
        if not user_input:
            print("Please enter a valid word.\n")
            continue
        
        word_lower = user_input.lower()
        
        # Stemming (crude)
        stemmed = stemmer.stem(word_lower)
        
        # Lemmatization with spaCy (accurate, handles irregular verbs)
        doc = nlp(word_lower)
        lemmatized = doc[0].lemma_ if len(doc) > 0 else word_lower
        pos_tag = doc[0].pos_ if len(doc) > 0 else "UNKNOWN"
        
        # Check if word is likely invalid (if lemma is same and POS is generic/unknown)
        is_likely_invalid = (lemmatized == word_lower and pos_tag in ["X", "SYM"])
        
        # Display results
        print(f"\n  Original Word:     {user_input}")
        print(f"  ──────────────────────────────")
        print(f"  Word Type:         {pos_tag}")
        
        if is_likely_invalid:
            print(f"  Status:            ⚠️  May not be a valid word")
        
        print(f"  ──────────────────────────────")
        print(f"  Stemmed (Porter):  {stemmed}")
        print(f"  Lemmatized (spaCy): {lemmatized}")
        print(f"  ──────────────────────────────")
        print(f"  ✓ Base Form:       {lemmatized}")
        print()

if __name__ == "__main__":
    process_word_interactive()
