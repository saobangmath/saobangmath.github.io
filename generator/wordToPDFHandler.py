import json
import os
import subprocess
import comtypes.client


pdfFormat = 17

with open("./config.json") as f:
    config = json.load(f)
    try:
        doc_path = config["doc_path"]
        pdf_paths = config["pdf_paths"]
        assert(os.path.exists(doc_path))
        in_file = os.path.abspath(doc_path)
        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(in_file)
        for pdf_path in pdf_paths:
            print(pdf_path)
            out_file = os.path.abspath(pdf_path)
            # create word client
            doc.SaveAs(out_file, FileFormat = pdfFormat)
            # verify the format of generate pdf
            subprocess.Popen(out_file , shell = True)
        print("Open!")
        doc.Close()
        word.quit()
    except:
        print("Error in opening file")