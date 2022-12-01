This repo is a fork of https://github.com/iannuttall/binlist-data

The BIN data in the repo is exposed as a RESTful API using a simple Flask frontend. 

A docker image can be created by running the command

docker build --tag binlookup . 

To run the docker image, you can run the command below (to expose the lookup service on a port different from 5000, (say 8000), change the -p option to 8000:5000

docker run --name binlookup -d -p 5000:5000 binlookup


The service can be used to do BIN lookups by sending a GET request to /lookup/&lt;credit-card-number&gt; (its enough to send just the first 6 digits)

ex: http://localhost:5000/lookup/377420

You are free to use this list for any purpose, including private or commercial use. This is just a test project, so use at your own risk.  I would also like to thank the binlist-data team for the meticulous work in compiling the BIN data and providing it to the community


The README.md file from the original project is appended below for your reference. 

# Repo closed

I no longer have the time or desire to continue updating and moderating this repository, and it is now read-only. You can fork this and continue your own database.

# Open-source BIN list

This repository is an open-source list of Issuer Identification Numbers (IIN), which are more commonly known as a Bank Identification Number (BIN).

The leading 6-8 numbers of a credit or debit card are used to identify the issuing bank or financial institution. This repo has been compiled by scraping, organising and compiled data from many different sources and is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Using the list

You are free to use this list for any purpose, including private or commercial use.

**This data is not an official IIN register.** I scraped and compiled this data to help with learning Python, and although it is a fairly comprehensive and accurate BIN list, it's not perfect. Use at your own risk!


## Contributing

The easiest way is to fork this repository on GitHub, modify existing lines, or add your own, and then submit a [pull request](https://help.github.com/en/articles/about-pull-requests). If you could quote a source link or text with your commit message, it'll help me to verify the data and include your submission in the list.

