# Dipendenza PyMuPDF non disponibile

PyMuPDF/fitz non e installato in questo ambiente. Lo script ha usato il fallback locale macOS CUPS (`cupsfilter` + `rastertotiff`) con Pillow per generare PNG a 300 DPI.

Per usare il renderer preferito in futuro, installare localmente:

```bash
python3 -m pip install PyMuPDF
```
