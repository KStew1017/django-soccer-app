# Soccer Match Application

This Django python application keeps track of soccer matches in the 2022-2023 Champions League, including information on when and where it will be played, and who will be playing.

Along with specific match information, there will be an option to view teams individual pages and see their rosters.

The postgres database used for this application has been seeded with data from [ESPN's hidden API endpoints](https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b), found courtesy of [Akshay Easwaran](https://github.com/akeaswaran).

---

The Django configuration files and main application files can be found under app/main/.

Each entity in the database can be found in its own respective folder in app/.