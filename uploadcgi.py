print("content-type: text/html")
print()

import cgi, os
import cgitb
cgitb.enable()

#try: # Windows needs stdio set for binary mode.
#    import msvcrt
#    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
#    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
#except ImportError:
#    pass

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['filename']

print("--------")
print("filename", fileitem.filename)
print("file", fileitem.file)
print("--------")


# Test if the file was uploaded
if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)

    open(fn, 'wb').write(fileitem.file.read(250000))
    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'No file was uploaded'

print("""
        <html><body>
        <p>%s</p>
        </body></html>
        """ % (message,))
