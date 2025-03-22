Adding an Event Server Repository to sort code functions with proper syntax.

For copy paste and function signature ID tagging purposes.

Best to keep it flexible to help in long term maintainability.
Got the structure right for me so that it gives guidance.

- It is not serverless, but does follow good practices.

- Testing was mandatory in previous versions, it is optional now, only because the chicken and egg problem of testing wastes time.

- Testing is useful for certain purposes, not everything. 

- Certain tests will be added to help in long term feature testing, for when code is recompiled on different newer, older systems, cross platform uses.

- Keep static files in a newer version of Documentation.

- Keep projects built in it's own repository.

- Bootstrappers go in their own repository.

- Boilerplate is useful, goes in own repository.

- Extract configuration goes in own repository.

- devops goes in it's own repository.

- ideas, feature priority and text, json, csv, models, data go in their own repository.

- fix the version details so that can test deprecation or revert version.

