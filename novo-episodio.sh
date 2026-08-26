#!/usr/bin/env bash
# Baixa a legenda automática em pt de um vídeo do YouTube e converte em texto limpo.
#
#   ./novo-episodio.sh https://youtu.be/XXXXXXXX
#
# Depois de rodar, peça ao Claude para ler a transcrição e atualizar o skill.

set -euo pipefail

if [ $# -eq 0 ]; then
  echo "uso: ./novo-episodio.sh <url-do-youtube> [<url> ...]"
  exit 1
fi

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAW="$REPO/transcricoes/raw"
TEXTO="$REPO/transcricoes/texto"
mkdir -p "$RAW" "$TEXTO"

for URL in "$@"; do
  echo "==> $URL"

  # metadados
  META=$(yt-dlp --no-update "$URL" --skip-download \
           --print "%(id)s|%(title)s|%(channel)s|%(duration)s|%(upload_date)s" 2>/dev/null)
  ID=${META%%|*}
  echo "    $META"

  # legenda automática em português (pt-orig = ASR original, não tradução)
  yt-dlp --no-update "$URL" --skip-download \
         --write-auto-sub --sub-lang "pt-orig" --sub-format json3 \
         -o "$RAW/%(id)s.%(ext)s" 2>&1 | grep -Ei "writing|error" || true

  if [ ! -f "$RAW/$ID.pt-orig.json3" ]; then
    echo "    !! sem legenda automática em pt — precisa de Whisper para este"
    continue
  fi

  # próximo número da sequência
  N=$(printf "%02d" $(( $(ls "$TEXTO" | grep -cE '^[0-9]{2}-') + 1 )))

  # slug do canal
  SLUG=$(echo "$META" | cut -d'|' -f3 \
          | iconv -f utf-8 -t ascii//TRANSLIT 2>/dev/null \
          | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' \
          | sed 's/^-//;s/-$//' | cut -c1-30)

  python3 "$RAW/conv.py" "$ID"
  mv "$TEXTO/$ID.txt" "$TEXTO/$N-$SLUG.txt"

  # registra no urls.txt para histórico
  echo "$URL # $META" >> "$RAW/urls.txt"

  echo "    -> transcricoes/texto/$N-$SLUG.txt"
done

echo
echo "Pronto. Agora peça ao Claude:"
echo "  \"lê a transcrição nova e atualiza o skill\""
