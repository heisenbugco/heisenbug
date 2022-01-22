from distutils.core import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_descript = fh.read()
setup(
  name = "heisenbug",
  packages = ["heisenbug"],
  version = "0.0.1",
  license="",      
  description="Hello Quantum!",
  long_description=long_descript,
  long_description_content_type=" text/markdown",
  author="heisenbug.co",                 
  author_email="heisenbugco@gmail.com",
  url="https://github.com/heisenbugco/heisenbug",
  download_url="https://github.com/heisenbugco/heisenbug/archive/v_001.tar.gz", 
  keywords=["quantum", "machine", "learning"], 
  # install_requires=[],
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: Self Declared",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
  ],
)
