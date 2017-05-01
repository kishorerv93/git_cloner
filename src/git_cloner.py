#!/usr/bin/python3


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser('Git web cloner')
    parser.add_argument('--type', type=str, nargs=1, help='service type: `bitbucket` or `github`')
    parser.add_argument('--login', type=str, nargs=1, default=[''], help='user login')
    parser.add_argument('--password', type=str, nargs=1, default=[''], help='user password')

    parser.add_argument('site', metavar='site', type=str, help='service address')

    args = parser.parse_args()

    service_type = None if args.type is None else args.type[0]
    site = args.site
    login = args.login[0]
    password = args.password[0]

    if service_type is None:
        if 'github' in site:
            service_type = 'github'
        elif 'bitbucket' in site or 'atlassian' in site:
            service_type = 'bitbucket'
        else:
            service_type = site

    if service_type == 'bitbucket':
        from git_cloner.bitbucket import BitbucketCloner
    elif service_type == 'github':
        from git_cloner.github import GithubCloner
        owner = ''
        GithubCloner(site, owner, login=login, password=password).clone()
    else:
        print('Unknown type "{}"!'.format(service_type))
        exit(1)

