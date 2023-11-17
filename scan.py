import docx2pdf
from PIL import Image
from io import BytesIO
import pytesseract
from database import Database
import pythoncom
import shutil
import fitz
import os

path_parts = [os.getcwd(), 'tesseract', 'tesseract.exe']
path = os.path.join(*path_parts)
raw_path = r'' + path
pytesseract.pytesseract.tesseract_cmd = raw_path

class Scan:
	def __init__(self, path, email):
		self.num_pages = 1
		self.path = path
		self.email = email
		self.database = Database("database.db")
		self.text = ""
	
	def scan(self):
		text = self.scan_file(self.path)
		unkown = True
		if text != "":
			text = text.strip()
			text = " ".join(text.split())
			templates = self.database.get_templates()
			for i in templates:
				if i[0].lower() in text.lower():
					unkown = False
					name = self.database.get_name_on_template(i[0])
					self.sorting(name)
					break

		if unkown == True:
			name = "Не распознано"
			self.sorting(name)

	def scan_file(self, path):
		print(path)
		text = ""
		if path.endswith(".pdf"):
			text = self.scan_pdf(path)
		elif path.endswith(".docx"):
			text = self.scan_docx(path, os.path.splitext(path)[0] + ".pdf")
		elif path.endswith(".jpg") or path.endswith(".jpeg") or path.endswith(".png") or path.endswith(".tif") or path.endswith(".tiff"):
			text = self.scan_image(path)
			print(text)
		return text

	def scan_image(self, path_image):
		image = Image.open(path_image)
		text = pytesseract.image_to_string(image, lang="rus")
		return text

	def scan_docx(self, path_docx, path_pdf):
		pythoncom.CoInitialize()
		docx2pdf.convert(path_docx, path_pdf)

		doc = fitz.open(path_pdf)

		if doc.page_count >= 2:
			self.num_pages = 2

		image_xrefs = {}
		for i in range(self.num_pages):
			page = doc[i]
			self.text += page.get_text()
			for image in page.get_images():
				image_xrefs.setdefault(image[0], [])			

		for index, xref in enumerate(image_xrefs):
			img = doc.extract_image(xref)
			self.text += pytesseract.image_to_string(Image.open(BytesIO(img["image"])), lang="rus")

		doc.close()
		os.remove(path_pdf)

		return self.text

	def scan_pdf(self, path_pdf):
		doc = fitz.open(path_pdf)

		if doc.page_count >= 2:
			self.num_pages = 2

		image_xrefs = {}
		for i in range(self.num_pages):
			page = doc[i]
			self.text += page.get_text()
			for image in page.get_images():
				image_xrefs.setdefault(image[0], [])

		for index, xref in enumerate(image_xrefs):
			img = doc.extract_image(xref)
			self.text += pytesseract.image_to_string(Image.open(BytesIO(img["image"])), lang="rus")
			
		return self.text
	
	def sorting(self, folder_name):
		print(folder_name)
		try:
			if not os.path.exists(f"Messages/{self.email}/{folder_name}"):
				os.makedirs(f"Messages/{self.email}/{folder_name}")
			filename = os.path.basename(self.path)
			new_filename = filename
			if os.path.exists(os.path.join(f"Messages/{self.email}/{folder_name}", filename)):
				i = 0
				while os.path.exists(os.path.join(f"Messages/{self.email}/{folder_name}", new_filename)):
					i+=1
					new_filename = f"{os.path.splitext(filename)[0]}_{i}{os.path.splitext(filename)[1]}"
			shutil.copy2(self.path, os.path.join(f"Messages/{self.email}/{folder_name}", new_filename))
			os.remove(self.path)
		except Exception as e:
			print(e)