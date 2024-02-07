import pdfquery

if __name__ == '__main__':
    pdf = pdfquery.PDFQuery("./pdf/i-485.pdf")
    pdf.load()

    # Query Family first name
    label = pdf.pq('LTPage[page_index="0"] LTTextLineHorizontal:contains("1.a. Family Name")')
    print(label)
    left_corner = float(label.attr('x1'))
    top_corner = float(label.attr('y1'))
    first_name = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, top_corner-30, left_corner+70, top_corner)).text()
    print(f"Family name is: {first_name}") # John

    # Query Family given name
    # Case of multiple returns
    labels = pdf.pq('LTPage[page_index="0"] LTTextLineHorizontal:contains("Given Name")')
    print(labels)
    label = labels[0] # pick the first one
    left_corner = float(label.attrib['x1'])
    top_corner = float(label.attrib['y1'])
    given_name = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, top_corner-30, left_corner+30, top_corner)).text()
    print(f"Given name is: {given_name}") # Doe
