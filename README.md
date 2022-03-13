# GitHub API Wrapper

This is a simple wrapper around GitHub's REST API.

## Usage

TODO: Update usage information to reflect an end-user pip installation.

The GitHubAPI class is the main entrypoint into the SDK. It is instantiated with
a Personal Access Token that has the following permissions:

- `repo` to access information about private and public repos on your account
- `read:org` to access information about your organizations
- `read:user` to access information about your user

```
from src.base import GitHubAPI

github = GitHubAPI("USERNAME", "TOKEN")

github.users.me() // Returns the authenticated user's information
```

The GitHubAPI class re-exports subcommands that can be used to access different
parts of the GitHub API. Currently implemented are Users, Organizations, and
Repositories.

For example, to find a repository specifically:

```
github.repos.get("panopticarising", "mathy-editor")
```

The objects returned from calls to the GitHubAPI provide their own instance
methods for easier access of information.

For example, to find a User's repository:

```
my_user = github.users.me()
my_user.get_repos()
```

## Rationale

This wrapper currently only exposes READ information from the GitHub API. The
intention is to provide easy-to-use abstractions to allow end-users to scrape
information that they have access to from GitHub.

## Roadmap

This SDK is still currently in development. The following are goals to improve
code quality and feature implementations:

- Add in additional checks for exceptions and explicitly mark the public-facing
  API with expected exceptions.
  - Currently, any exceptions from the request are propagated up, and might
    result in KeyErrors when instance objects are being constructed.
- Update existing API implementations to expose additional documented request
  parameters that are not currently exposed in the public-facing API.
  - Of the many additional parameters not included, we should try to implement
    paging in a developer-friendly way by supporting iterable/generator access
    under-the-hood. This should ideally be wrapped in a user-friendly error that
    clearly explains whether the API request failed (i.e. bad status code) or
    whether the resource was malformed (missing required keys)
- Ensure type-hinting is added to all public-facing API calls for a better
  developer experience
- Implement more dynamic HTML renderings for large data displayed in ipynb.
