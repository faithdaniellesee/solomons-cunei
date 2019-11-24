from pylatex import Document, Figure


doc = Document(documentclass="article")
with doc.create(Figure(position='p')) as fig:
    fig.add_image('doggo.jpeg')

doc.generate_pdf('test', compiler='latexmk', compiler_args=["-pdf", "-pdflatex=pdflatex"], clean_tex=True)

