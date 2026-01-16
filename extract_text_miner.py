from pdfminer.high_level import extract_text

try:
    text = extract_text("resume.pdf")
    print("--- TEXT START ---")
    print(text)
    print("--- TEXT END ---")
except Exception as e:
    print(f"Error: {e}")
