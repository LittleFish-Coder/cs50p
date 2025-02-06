doc = input("File name: ").strip().lower()

if doc.endswith("jpg") or doc.endswith("jpeg"):
    print("image/jpeg")
elif doc.endswith("png"):
    print("image/png")
elif doc.endswith("gif") :
    print("image/gif")
elif doc.endswith("pdf"):
    print("application/pdf")
elif doc.endswith("txt"):
    print("text/plain")
elif doc.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")
