win_susp_etw_trace_evasion_grammar = {
    "<start>": [
        "<wevtutil_attack>",
        "<logman_attack>",
        "<powershell_attack>"
    ],
    "<wevtutil_attack>": [
        "<wevtutil_exe> <wevtutil_clear_cmd>",
        "<wevtutil_exe> <wevtutil_disable_cmd>"
    ],
    "<wevtutil_exe>": [
        "wevtutil.exe",
        "%windir%\\system32\\wevtutil.exe",
        "wevtutil"
    ],
    "<wevtutil_clear_cmd>": [
        "<clear_verb> <log_name> /Trace"
    ],
    "<clear_verb>": [
        "cl",
        "'cl'",
        "c^l",
        "clear-log"
    ],
    "<wevtutil_disable_cmd>": [
        "<disable_verb> <log_name> <disable_switch>"
    ],
    "<disable_verb>": [
        "sl",
        "\"sl\"",
        "s^l",
        "set-log"
    ],
    "<disable_switch>": [
        "/e:false",
        "/E:FALSE"
    ],
    "<log_name>": [
        "Microsoft-Windows-Sysmon/Operational",
        "\"Windows PowerShell\""
    ],
    "<logman_attack>": [
        "<logman_exe> <logman_params_reordered>"
    ],
    "<logman_exe>": [
        "logman.exe",
        "LOGMAN",
        "%SystemRoot%\\System32\\logman.exe"
    ],
    "<logman_params_reordered>": [
        "<update_verb> <trace_name> <provider_param> <ets_switch>",
        "<update_verb> <trace_name> <ets_switch> <provider_param>"
    ],
    "<update_verb>": [
        "update",
        "upd^ate",
        "\"update\""
    ],
    "<trace_name>": [
        "trace EventLog-System",
        "trace \"Circular Kernel Context Logger\""
    ],
    "<provider_param>": [
        "--p \"Microsoft-Windows-Kernel-Process\"",
        "-p {0819b1d9-6c39-4ea3-8ca4-685f00251728}"
    ],
    "<ets_switch>": [
        "-ets",
        "'-ets'"
    ],
    "<powershell_attack>": [
        "<powershell_exe> -Command <ps_obfuscated_cmd>",
        "<powershell_exe> -EncodedCommand <encoded_ps_command>"
    ],
    "<powershell_exe>": [
        "powershell.exe",
        "pwsh.exe"
    ],
    "<ps_obfuscated_cmd>": [
        "&('Rem' + 'ove-EtwTraceProvider') -Guid '{d62b96e2-b13d-4235-8698-1e245f3a2e06}'",
        "Set-EtwTraceProvider -Guid '{d62b96e2-b13d-4235-8698-1e245f3a2e06}' -Mode ('0x1' + '1')"
    ],
    "<encoded_ps_command>": [
        "UgBlAG0AbwB2AGUALQBF AHQAdwBUAHIAYQBjAGUAUAByAG8AdgBpAGQAZQByACAALQBHAHUAaQBkACAAJwB7AGQANgAyAGIAOQA2AGUAMgAtAGIAMQAzAGQALQA0ADIANwM1ADMALQA4ADYAOQA4AC0AMQBlADIANAA1AGYAMwBhADIAZQAwADYAfQAnAA==",
        "UwBlAHQA LQBFAHQAdwBUAHIAYQBjAGUAUAByAG8AdgBpAGQAZQByACAALQBHAHUAaQBkACAAJwB7AGQANgAyAGIAOQA2AGUAMgAtAGIAMQAzAGQALQA0ADIANwM1ADMALQA4ADYAOQA4AC0AMQBlADIANAA1AGYAMwBhADIAZQAwADYAfQAnACAALQBNAG8AZABlACAAMAB4ADEAMQA="
    ]
}