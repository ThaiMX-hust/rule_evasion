win_bcdedit_boot_conf_tamper_grammar = {
    "<start>": [
        "<executable> <params>"
    ],
    "<executable>": [
        "bcdedit.exe",
        "bcdedit",
        "%windir%\\system32\\bcdedit.exe",
        "C:\\Windows\\SysNative\\bcdedit.exe"
    ],
    "<params>": [
        "<set_cmd> <option1>",
        "<set_cmd> <option2>"
    ],
    "<set_cmd>": [
        "set",
        "s^et",
        "\"set\"",
        "'set'"
    ],
    "<option1>": [
        "<identifier> <bsp_policy> <bsp_value>"
    ],
    "<option2>": [
        "<identifier> <re_policy> <re_value>"
    ],
    "<identifier>": [
        "{current}",
        "{default}",
        ""
    ],
    "<bsp_policy>": [
        "bootstatuspolicy",
        "'bootstatuspolicy'"
    ],
    "<bsp_value>": [
        "ignoreallfailures",
        "ignore^all^failures"
    ],
    "<re_policy>": [
        "recoveryenabled",
        "\"recoveryenabled\""
    ],
    "<re_value>": [
        "no",
        "n^o",
        "NO"
    ]
}