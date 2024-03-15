from setuptools import setup, Extension
import setuptools_scm  # noqa  Ensure it’s installed

extensions = [
    Extension("cutadapt2._align", sources=["src/cutadapt2/_align.pyx"]),
    Extension("cutadapt2.qualtrim", sources=["src/cutadapt2/qualtrim.pyx"]),
    Extension("cutadapt2.info", sources=["src/cutadapt2/info.pyx"]),
    Extension("cutadapt2._kmer_finder", sources=["src/cutadapt2/_kmer_finder.pyx"]),
]

setup(ext_modules=extensions)
