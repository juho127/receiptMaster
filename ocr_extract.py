import os
import sys

try:
    from pdf2image import convert_from_path
    import pytesseract
    from PIL import Image
except ImportError:
    print("Error: Missing dependencies. Please install them using:")
    print("pip install pdf2image pytesseract Pillow")
    print("\nNote: You also need 'poppler' and 'tesseract' installed on your system.")
    sys.exit(1)

def process_pdf(pdf_path, output_folder="extracted_images"):
    """
    1. Converts PDF pages to images.
    2. (Optional) Performs OCR on each image.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: File not found -> {pdf_path}")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")

    print(f"Converting PDF: {pdf_path} ...")
    
    try:
        # Convert PDF to list of PIL Image objects
        pages = convert_from_path(pdf_path)
        
        for i, page in enumerate(pages):
            image_path = os.path.join(output_folder, f"page_{i+1}.png")
            page.save(image_path, "PNG")
            print(f"Saved: {image_path}")
            
            # Optional: Perform OCR
            # print(f"Performing OCR on page {i+1}...")
            # text = pytesseract.image_to_string(page, lang='kor+eng')
            # print(f"--- Page {i+1} Text ---\n{text}\n")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        print("\nTip: Ensure 'poppler' is installed and in your PATH.")

if __name__ == "__main__":
    target_pdf = "receipt.pdf" # Default filename
    if len(sys.argv) > 1:
        target_pdf = sys.argv[1]
        
    process_pdf(target_pdf)
