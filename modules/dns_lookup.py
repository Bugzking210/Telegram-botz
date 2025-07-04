import dns.resolver

def lookup(domain):
    res = dns.resolver.Resolver()
    out = []
    for t in ['A','MX','NS','TXT']:
        try:
            answers = res.resolve(domain, t)
            out.append(f"{t}: {[r.to_text() for r in answers]}")
        except Exception as e:
            out.append(f"{t}: Error {e}")
    return "\n".join(out)
