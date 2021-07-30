# Easter Distribution

This project shows how Easters within a century are distributed among months and dates,
and how Easter date swings back and forth, year after year.
It is in action [here](https://rayluo.github.io/easter/).

This project is also designed to be a sample of how to use
[brip](https://pypi.org/project/brip)
to pull in generic pure Python packages into your
[Brython](http://brython.info/)-powered project.


## How to develop a project like this?

We chose to implement the following features in this sample project,
to showcase how generic Python packages could be pulled into your project by `brip`.

* Calculate the Easter date of any given year.
  [Easter calculation is complicated](https://www.tondering.dk/claus/cal/easter.php),
  but it is made easy by this generic Python package
  [python-dateutil](https://dateutil.readthedocs.io/en/stable/easter.html).
* Show the distribution of Easters in charts,
  with the help of this generic Python package
  [charts.css.py](https://rayluo.github.io/charts.css.py/).

So, how to build a Brython project to utilize the above 2 generic Python packages?

1. Prerequisite:
   You do *NOT* need to install those 2 packages by the normal `pip`.
   Instead, you use `pip` to install `brip` into a virtual environment,
   once and for all:
   such an environment can be shared among all your Brython projects.

   Installation on Linux and macOS:

   ```
   python3 -m venv ~/venv_central
   source ~/venv_central/bin/activate
   pip install brip
   ```

   Installation on Windows:

   ```
   py -m venv $HOME\venv_central
   $HOME\venv_central\Scripts\activate
   pip install brip
   ```

2. Create an empty Brython project.
   You can choose to clone or download this
   [template Brython project](https://github.com/rayluo/brython-project-template).

3. Inside your Brython project's webroot directory
   (i.e. the directory containing your index.html),
   create a `brequirements.txt` file containing your dependencies.
   After you finish that, you will see this.

   ```
   cd ~/easter/website
   cat brequirements.txt
   ```

   You are expected to fill it with this content, optionally with their version ranges.

   ```
   python-dateutil<3
   charts.css.py>=0.4.0,<1
   ```

   For what it's worth, the `python-dateutil` package has its own dependency on `six`,
   but you don't have to know, `brip` will automatically pull in all dependencies for you.

4. Run `brip install -r brequirements.txt`.
   This will generate a `site-packages.brython.js` file,
   which contains the packages that you declared, as well as all their dependencies.

5. In your Brython project's `index.html`, include the `brython.js` as usual,
   and you would typically also need to include the `brython_stdlib.js`,
   lastly you include the `site-packages.brython.js` that we generated just now.

   That is all.
   Now you can use `import dateutil` and `import charts.css` in your Brython project.

6. Once you finish your project, you can deploy it with the generated
   `site-packages.brython.js`.

   Alternatively, this project chooses to
   [run step 4 on-the-fly via Github Actions](https://github.com/rayluo/easter/blob/main/.github/workflows/publish-to-github-pages.yml#L16-L19),
   and then [deploy the website to Github Pages](https://github.com/rayluo/easter/blob/main/.github/workflows/publish-to-github-pages.yml#L21-L24)
   (with the help from another tool named [Github Page Overwriter](https://github.com/rayluo/github-pages-overwriter)).
   The end result is you do not even need to hardcode a copy of `site-packages.brython.js`
   inside your project's code base.
   See how clean our [code base](https://github.com/rayluo/easter/tree/main/website) is.


## Caveat

The two external dependencies, `python-dateutil` and `charts.css.py`,
work smooth inside Brython.
But the reality is, not every PyPI packages would work fine.
Please refer to the [limitations of brip](https://github.com/rayluo/brip#limitations)
for more details.

