#!/bin/bash

_yt_completions() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # Liste des sous-commandes
    opts="start update uninstall"

    # Complétion des sous-commandes
    COMPREPLY=( $(compgen -W "${opts}" -- "${cur}") )
    return 0
}

complete -F _yt_completions yt
