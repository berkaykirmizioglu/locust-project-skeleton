import strgen


def generate_email() -> str:
    """Generates a random mail address starts with 'locustn11tester'"""
    email = "locustn11tester" + strgen.StringGenerator("[a-z]{5}[0-9]{5}").render() + "@mailinator.com"
    return email
