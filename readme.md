# setsy 

This adds the cartesian operation and a powerset operation to the inherited set class.

It attempts to preserve the order of the input iterable when outputting with the _str_ method.

It's too setsy for its shirt.

## Future plans

- [x] Power set

## Important disclaimer

The code here does not yet represent work I'd submit for production code-review.  Standards differ, and I have worked within many different sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:

- [x] Apply this checklist to all new projects as step one
- [ ] A complete regression test suite.
- [ ] Meaningful exceptions and exception-handling coverage.
- [ ] Thoughtful, self-documenting, variable, method, and function names.
- [ ] Adequate output to permit users to understand the results, assisting in the self-documenting nature of the code.
  - [ ] Specifically, would this benefit from comprehensive logging?
  - [ ] Would it benefit from a results page with stats to demonstrate accurate and complete results?
  - [ ] How do I want to manage output to stdout, stderr, file, etc?
  - [ ] How do comments and outputs help and assist one another without being redundant?
- [ ] Actual docstring comments at all levels of the code.
- [x] Linting the code for PEP 8 standardization Or Applying a PEP formatter to the code.
- [ ] Requirements documents, user-facing documents and presentations, and other documents consistent with Agile User Stories to add value.
- [ ] Commit statements which facilitate an understanding of code history.
- [ ] Readme.md pages with more interesting usage of markdown which tell a code narrative. 
- [ ] Make good decisions relating to
  - [ ] Exceptions versus return values
  - [ ] Using idiomatic Python versus clarity of code
  - [ ] Extend this list


### Getting Started

This project provides an enhanced Python set class, `setsy`, with additional functionality for set operations, including power sets, cartesian products, and improved subset/superset checks with explanations. You can explore its features through the included demo script.

To quickly try out the capabilities, run the demo script or use the provided Docker setup for an isolated environment.

---

### Prerequisites

- Python 3.8 or higher
- (Optional) Docker, for containerized usage

---

### Installing

**Clone the repository:**
```bash
git clone https://github.com/ErikPohl444/setsy.git
cd setsy
```

**Install dependencies:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

**Alternatively, run with Docker:**
```bash
docker build -t setsy .
docker run --rm setsy
```

## Running the tests

I will explain how to test the system here using the automated tests.

## Contributing

For now, I'd be excited to receive pull requests.  I don't have rules for contributing right now.

## Authors

* **Erik Pohl** - *Initial work* - 

Also see the list of github contributors.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to everyone who has motivated me to learn more.
