win_cmdkey_recon_grammar = {
    "<start>": [
        "<executable> <list_param>"
    ],
    "<executable>": [
        "cmdkey.exe",
        "cmdkey",
        "%windir%\\system32\\cmdkey.exe",
        "C:\\Windows\\SysNative\\cmdkey.exe"
    ],
    "<list_param>": [
        "/list",
        "/LIST",
        "'/list'",
        "\"/list\"",
        "/li^st"
    ]
}