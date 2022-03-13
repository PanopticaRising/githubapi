# PAC: 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
import requests
from src.orgs import OrgAPI
from src.repos import RepoAPI
from src.users import UsersAPI


class GitHubAPI:

    def __init__(self, username, PAC):
        """
        This instantiates the Github API with a Personal-Access Token.
        This will be passed to all requests for authentication.
        """
        self._username = username
        self._PAC = PAC
        self.users = UsersAPI(self)
        self.repos = RepoAPI(self)
        self.orgs = OrgAPI(self)

    # TODO: It'd be cool if we made a HEAD request to every endpoint to show API status.
    def _repr_html_(self):
        return f"<h1>Github API instance</h1><p>To access data, refer to <code>users</code>, <code>repos</code>, or <code>orgs</code> properties.</p>"

    def make_request(self, method, url_fragment, **kwargs):
        return requests.request(
            method, f"https://api.github.com/{url_fragment}", auth=(self._username, self._PAC), **kwargs)
