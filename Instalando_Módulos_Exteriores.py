import pydf

pdf = pydf.generate_pdf('<h1>Teste</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
"""
Não funciona pq é Windows.
"""