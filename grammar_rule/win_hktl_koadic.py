win_hktl_koadic_grammar = {
    "<start>": [
        "<executable> <params_reordered>"
    ],
    "<executable>": [
        "cmd.exe",
        "cmd",
        "%COMSPEC%",
        "%windir%\\system32\\cmd.exe"
    ],
    "<params_reordered>": [
        "<q_switch> <c_switch> <command>",
        "<c_switch> <q_switch> <command>"
    ],
    "<q_switch>": [
        "/q",
        "''/q''"
    ],
    "<c_switch>": [
        "/c",
        "\"/c\""
    ],
    "<command>": [
        "<chcp_fuzzed> 65001 > nul & echo payload",
        "<chcp_env_var_obfuscation> & echo payload"
    ],
    "<chcp_fuzzed>": [
        "chcp",
        "c^hcp",
        "\"chcp\""
    ],
    "<chcp_env_var_obfuscation>": [
        "set a=chcp & call %a% 65001 > nul"
    ]
}
    