
win_cmd_assoc_execution_grammar = {
    "<start>": [
        "<executable> <command>"
    ],
    "<executable>": [
        "cmd.exe",
        "cmd",
        "%COMSPEC%",
        "%windir%\\system32\\cmd.exe"
    ],
    "<command>": [
        "/c <fuzzed_assoc> <params>",
        "/C <fuzzed_assoc> <params>"
    ],
    "<fuzzed_assoc>": [
        "assoc",
        "ASSOC",
        "a^s^soc",
        "as''oc"
    ],
    "<params>": [
        ".xyz=evil.exe",
        "'.txt'=txtfile",
        ".pdf=\"C:\\temp\\payload.com\"",
        ".html"
    ]
}