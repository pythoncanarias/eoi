# Servir los contenidos en un web server local
serve:
    mkdocs serve -a localhost:3456

pdf:
    ENABLE_PDF_EXPORT=1 mkdocs build
