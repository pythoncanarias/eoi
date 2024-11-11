# Servir los contenidos en un web server local
serve:
    cd {{invocation_directory()}} && mkdocs serve -a localhost:3456

# Generar PDF con la documentación
pdf:
    cd {{invocation_directory()}} && ENABLE_PDF_EXPORT=1 mkdocs build


# Generar la documentación con Sphibx
docs: clean
     cd {{invocation_directory()}} &&  sphinx-build -W -c . -b html . ./html


# Borra todos los ficheros compilados python (*.pyc, *.pyo, __pycache__)
clean:
    sudo find . -type d -name "__pycache__" -exec rm -r "{}" +
    sudo find . -type d -name ".mypy_cache" -exec rm -r "{}" +
    sudo find . -type d -name ".pytest_cache" -exec rm -r "{}" +
    sudo find . -type d -name ".ipynb_checkpoints" -exec rm -r "{}" +
    sudo find . -type f -name "*.pyc" -delete
    sudo find . -type f -name "*.pyo" -delete
    if [ -e .ruff_cache ]; then rm -r .ruff_cache/; fi

# Cambiar el título de la terminal
[unix]
termtitle *args='Terminal':
    echo -en "\033]0;{{ args }}\007";

# Generar la documentación con Sphinx cuando cambien las fuentes
watchdocs:
    just termtitle Watch Docs
    watchmedo shell-command --patterns "*.rst;*.py" --recursive --command "just docs"

