import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
import pytesseract

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# OCR function
def extract_text():

    # Open image chooser
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
    )

    # If user cancels
    if not file_path:
        return

    # Read image
    image = cv2.imread(file_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract text
    text = pytesseract.image_to_string(gray)

    # Clear previous text
    output_text.delete(1.0, tk.END)

    # Show extracted text
    output_text.insert(tk.END, text)

    # Success popup
    messagebox.showinfo("Success", "Text Extracted Successfully")


# Main window
root = tk.Tk()

root.title("AI OCR Text Recognition")
root.geometry("700x500")

# Heading
heading = tk.Label(
    root,
    text="Artificial Intelligence OCR Project",
    font=("Arial", 18, "bold")
)

heading.pack(pady=20)

# Upload button
upload_btn = tk.Button(
    root,
    text="Upload Image",
    font=("Arial", 14),
    command=extract_text
)

upload_btn.pack(pady=10)

# Output label
output_label = tk.Label(
    root,
    text="Detected Text:",
    font=("Arial", 14)
)

output_label.pack()

# Text area
output_text = tk.Text(
    root,
    height=15,
    width=80
)

output_text.pack(pady=10)

# Run application
root.mainloop()