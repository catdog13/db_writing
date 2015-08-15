# Metadata For Movies

#### writing_to_db
Main Program

#### exporter
Exports db as json, csv, and tabson files

#### updater
Batch updates metadata for movies

#### single_update
updates a single movie's metadata

#### modules
Backbone for whole operation
each part of the metadata gets is own function
add the column and call the function in the updater and writer functions

#### Requires
[requests](https://pypi.python.org/pypi/requests)
[dataset](https://pypi.python.org/pypi/dataset)