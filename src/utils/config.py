from decouple import config


HF_BASE_URL = config("HF_BASE_URL")
HF_API_KEY = config("HF_API_KEY")

fits_model = str(config("YODA_FITS_MODEL"))
ner_model = str(config("YODA_NER_MODEL"))
