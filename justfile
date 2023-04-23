# Servir los contenidos en un web server local
serve:
    cd {{invocation_directory()}} && mkdocs serve -a localhost:3456

# Generar PDF con la documentación
pdf:
    cd {{invocation_directory()}} && ENABLE_PDF_EXPORT=1 mkdocs build
