# Grove Collaborative Coding Challenge: Store Locator

## Installation:

Download and unzip.

Use of a virtual environment it recommended

```bash
$ sudo pip3 install virtualenv
$ python3 -m virtualenv env
$ source env/bin/activate
```

In package root run the following command:

```bash
$ source install.sh
```

The command `find_store` is now available in your `env` virtual environment.

Run command `find_store` for usage.

## Notes

This solution uses docopt to access arguments passed to the module through the bash terminal. The module's main function drives the rest of the application, including an address model for address data entered by the user. 

Tests are done using the pytest module and are simple, aiming to cover the most critical functionality.

The find store command can be run from any location in the command line as long as module contents are not moved or changed. 

This module is designed to be self-explanatory and intuitive and should be possible to use simply by checking usage with the base command. The module will function with any input and return appropriate error responses when run from the command line.

I chose a standard JSON format for JSON output and a mailing address format for text output.

Tests can be run by calling pytest on the test directory. Dependencies were installed during package installation.

Example testing call from module root directory:

```bash
$ pytest find_store/test
```

## Notes about the code:

There are several things I would improve given another refactor:

- Abstract out the display functions into a class called Display with subclasses JSONDisplay and TextDisplay.
- Scrape the CSV one time, use it as a seed for a Mongo database.
  - Pro: faster!
  - Con: harder to update, could solve this with a seed script.
- During database seeding geocode each store location so it can be converted into the same address object as the user entered data. This would make the application less fragile and easier to understand.
- Handle the possibility that the CSV file is not formatted as expected and return a useful error message about formatting to the user.
- Extend testing. This is the first time I've written a command line application, and testing was challenging. I'd like to spend more time figuring out how to do this better.