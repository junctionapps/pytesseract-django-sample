import tempfile
from PIL import Image
from django.shortcuts import render
from pytesseract import pytesseract
from ocr_sample.forms import UploadFileForm


def ocr_index(request):
    context = dict()

    # Windows users need to add something like:
    # pytesseract.pytesseract.tesseract.cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            image = Image.open(request.FILES['file_upload'])
            image_text = pytesseract.image_to_string(image)

            # If you were handling larger files, perhaps something like this would be better
            # with tempfile.TemporaryFile() as temp_file:
            #     for chunk in request.FILES['file_upload'].chunks():
            #         temp_file.write(chunk)
            #     image = Image.open(temp_file)
            #     image_text = pytesseract.image_to_string(image)

            context.update({'image_text': image_text, })
            # reset the form: typically we'd redirect elsewhere to prevent multiple
            # submissions of data, but there is no database interaction here - only
            # sending the text back
            form = UploadFileForm()
    else:
        form = UploadFileForm()

    context.update({'form': form, })

    return render(request, "ocr_sample/ocr_index.html", context)