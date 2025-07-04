import whois

def whois_query(domain):
    try:
        info = whois.whois(domain)
        return str(info)
    except Exception as e:
        return f"Error fetching WHOIS: {e}"
