def acessarSite(url: str):
    import requests
    try:
        url = url.replace(' ', '')
        resp = ''
        while ('http' or 'https') not in resp:
            resp = input('This site is "http" or "https"? ')
        url = f'{resp.strip(" ")}://{url}'
        requests.get(url)
    except:
        print(f'\n\033[1;31mO site {url} não está acessível no momento.\033[m')
    else:
        print(f'\n\033[1;32mConsegui acessar o site {url} com sucesso!\033[m')
