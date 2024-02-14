import PyPDF2
import sys

# WATERMARK PROJECT

template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]

    page.merge_page(watermark.pages[0])
    output.add_page(page)
    print(f'Page {i + 1} of {len(template.pages)} complete...')

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)

print("Merger Complete")

# SELECT FILE WITH WATERMARK, SET TO A VARIABLE(WATERMARK)
# CREATE READ VARIABLE FOR EACH PAGE
# CREATE A NEW FILE WITH THE WATERMARK DOCUMENT AS BASE, AND ADD READ TO THE FILE
# CREATE LOOP TO START AT UNMARKED.PAGE[0] UNTIL UNMARKED.PAGE[LEN[UNMARKED]
# GATHER SEPERATE PAGES IN NEW FOLDER AND MERGE

# #COMBINING PDFS INTO ONE FILE WITH CUSTOM NAME USING CLI(PYTHON3 + "CURRENT FILE NAME" + "FILES TO COMBINE"
# inputs = sys.argv[1:]
#
#
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
#
#
# pdf_combiner(inputs)

# ROTATE PDF CODE
# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     # print(len(reader.pages)) #TO FIND LENGTH
#     # print(reader.pages[0]) #TO FIND SPECIFIC PAGE
#     page = reader.pages[0]
#     page.rotate(90)
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)
