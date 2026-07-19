#!/usr/bin/env python3
"""Cliente mínimo da API do Plane (self-hosted ou cloud).

Uso:
  plane.py list-projects
  plane.py create-project "Nome do Projeto" --identifier SLUG
  plane.py list-issues <projeto>
  plane.py create-issue <projeto> "Título da issue" [--desc "descrição"]

<projeto> aceita nome, identifier ou UUID.

Config: PLANE_BASE_URL e PLANE_WORKSPACE — env, .env do repo ou ~/.config/plane/config.
Token: ~/.config/plane/token, env PLANE_API_TOKEN ou PLANE_API_TOKEN= no .env.
Gerar token em: seu Plane → Workspace Settings → API tokens.
"""

import argparse
import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

try:  # o Python do python.org vem sem CA bundle; certifi cobre
    import certifi

    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

TOKEN_PATH = os.path.expanduser("~/.config/plane/token")


def _find_repo_env() -> str:
    """Procura um .env subindo do diretório atual (o script pode viver na pasta do plugin)."""
    d = os.getcwd()
    while True:
        candidate = os.path.join(d, ".env")
        if os.path.exists(candidate):
            return candidate
        parent = os.path.dirname(d)
        if parent == d:
            return os.path.join(os.getcwd(), ".env")  # não achou; usar cwd na mensagem de erro
        d = parent


REPO_ENV = _find_repo_env()


GLOBAL_CONFIG = os.path.expanduser("~/.config/plane/config")


def _env(name: str) -> str | None:
    """Ordem: ambiente → .env do repo → ~/.config/plane/config (multi-repo)."""
    if os.environ.get(name):
        return os.environ[name]
    for path in (REPO_ENV, GLOBAL_CONFIG):
        if os.path.exists(path):
            with open(path) as f:
                for line in f:
                    if line.startswith(f"{name}="):
                        return line.split("=", 1)[1].strip()
    return None


BASE_URL = (_env("PLANE_BASE_URL") or "").rstrip("/")
WORKSPACE = _env("PLANE_WORKSPACE") or ""


def require_config() -> None:
    if not BASE_URL or not WORKSPACE:
        sys.exit(
            "Configure seu Plane: defina PLANE_BASE_URL (ex.: https://plane.exemplo.com ou "
            "https://api.plane.so) e PLANE_WORKSPACE (slug do workspace) — no ambiente, "
            f"num .env do repo ({REPO_ENV}) ou em {GLOBAL_CONFIG}."
        )


def token() -> str:
    tok = os.environ.get("PLANE_API_TOKEN")
    if not tok and os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH) as f:
            tok = f.read().strip()
    if not tok:  # fallback: PLANE_API_TOKEN no .env da raiz do monorepo
        env_path = REPO_ENV
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    if line.startswith("PLANE_API_TOKEN="):
                        tok = line.split("=", 1)[1].strip()
                        break
    if not tok:
        sys.exit(
            f"Sem token do Plane. Gere em {BASE_URL} → Workspace Settings → "
            f"API tokens e salve em {TOKEN_PATH} (ou exporte PLANE_API_TOKEN)."
        )
    return tok


def request(method: str, path: str, body: dict | None = None) -> dict:
    require_config()
    url = f"{BASE_URL}/api/v1/workspaces/{WORKSPACE}/{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "X-API-Key": token(),
            "Content-Type": "application/json",
            # proxies como Cloudflare bloqueiam o UA padrão do urllib (erro 1010)
            "User-Agent": "oraculo-flow-plane-cli/1.0 (curl-compatible)",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} em {method} {url}: {e.read().decode(errors='replace')}")
    except urllib.error.URLError as e:
        sys.exit(f"Falha de rede em {url}: {e.reason}")


def paginated(path: str) -> list[dict]:
    results, cursor = [], None
    while True:
        sep = "&" if "?" in path else "?"
        page = request("GET", path + (f"{sep}cursor={cursor}" if cursor else ""))
        if isinstance(page, list):  # algumas versões devolvem lista direta
            return page
        results.extend(page.get("results", []))
        if not page.get("next_page_results"):
            return results
        cursor = page.get("next_cursor")


def find_project(ref: str) -> dict:
    projects = paginated("projects/")
    ref_low = ref.lower()
    for p in projects:
        if ref_low in (p.get("id", "").lower(), p.get("identifier", "").lower(), p.get("name", "").lower()):
            return p
    names = ", ".join(f"{p['name']} ({p['identifier']})" for p in projects) or "(nenhum)"
    sys.exit(f"Projeto '{ref}' não encontrado. Existentes: {names}")


def cmd_list_projects(_args) -> None:
    for p in paginated("projects/"):
        print(f"{p['identifier']:<12} {p['name']:<32} {p['id']}")


def cmd_create_project(args) -> None:
    identifier = (args.identifier or args.name[:5]).upper().replace(" ", "").replace("-", "")
    p = request("POST", "projects/", {"name": args.name, "identifier": identifier})
    print(f"Criado: {p['name']} ({p['identifier']}) id={p['id']}")
    print(f"URL: {BASE_URL}/{WORKSPACE}/projects/{p['id']}/issues/")


def cmd_list_issues(args) -> None:
    p = find_project(args.project)
    for i in paginated(f"projects/{p['id']}/issues/"):
        print(f"{p['identifier']}-{i.get('sequence_id', '?'):<5} {i.get('name', '')}")


def cmd_create_issue(args) -> None:
    p = find_project(args.project)
    body = {"name": args.title}
    if args.desc:
        body["description_html"] = f"<p>{args.desc}</p>"
    i = request("POST", f"projects/{p['id']}/issues/", body)
    print(f"Criada: {p['identifier']}-{i.get('sequence_id', '?')} — {i.get('name')}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list-projects").set_defaults(fn=cmd_list_projects)

    cp = sub.add_parser("create-project")
    cp.add_argument("name")
    cp.add_argument("--identifier", help="prefixo das issues (ex.: LUMA); default: 5 primeiras letras do nome")
    cp.set_defaults(fn=cmd_create_project)

    li = sub.add_parser("list-issues")
    li.add_argument("project")
    li.set_defaults(fn=cmd_list_issues)

    ci = sub.add_parser("create-issue")
    ci.add_argument("project")
    ci.add_argument("title")
    ci.add_argument("--desc", help="descrição em texto simples")
    ci.set_defaults(fn=cmd_create_issue)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
