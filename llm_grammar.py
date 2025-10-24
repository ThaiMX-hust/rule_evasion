import os
#import yaml
import openai # Hoặc thư viện LLM khác
import ast # Để chuyển đổi chuỗi output của LLM thành dictionary
from fuzzingbook.GrammarFuzzer import GrammarFuzzer

# Cấu hình API key của bạn
# openai.api_key = "YOUR_API_KEY"

def get_grammar_from_llm(rule_content: str) -> dict:
    # Xây dựng prompt ở đây
    prompt = f"""
    Bạn là một chuyên gia an ninh mạng...
    ...
    BÂY GIỜ, HÃY XỬ LÝ QUY TẮC SAU ĐÂY:
    ---
    {rule_content}
    ---
    """
    
    # Gọi API của LLM (đây là pseudo-code)
    # response = openai.Completion.create(engine="text-davinci-003", prompt=prompt)
    # grammar_string = response.choices[0].text.strip()
    
    # Giả lập output của LLM để test
    grammar_string = """
{
    "<start>": ["<executable> <params_reordered>"],
    "<executable>": ["schtasks.exe", "%windir%\\system32\\schtasks.exe"],
    "<params_reordered>": ["<create_verb> <tn_param>", "<tn_param> <create_verb>"],
    "<create_verb>": ["/create", "/cr", "'/create'"],
    "<tn_param>": ["/tn \\"MyTask\\"", "/TN \\"MyTask\\""]
}
    """

    # Chuyển đổi chuỗi thành dictionary một cách an toàn
    try:
        return ast.literal_eval(grammar_string)
    except Exception as e:
        print(f"Lỗi khi xử lý output từ LLM: {e}")
        return None

def main():
    rule_path = "rules/proc_creation_win_schtasks_creation.yml"
    with open(rule_path, 'r') as f:
        rule_content = f.read()

    # Giai đoạn 1: LLM tạo grammar
    print("Đang gửi rule cho LLM để tạo grammar...")
    grammar = get_grammar_from_llm(rule_content)
    
    if grammar:
        print("LLM đã tạo grammar thành công!")
        
        # Giai đoạn 2: Fuzzer tạo test case
        fuzzer = GrammarFuzzer(grammar)
        output_file = "commands_generated_by_llm.txt"
        
        print(f"Đang tạo test case bằng fuzzer...")
        with open(output_file, "w") as f:
            for _ in range(1000):
                f.write(fuzzer.fuzz() + "\n")
        print(f"Hoàn tất! Kết quả được lưu tại {output_file}")

if __name__ == "__main__":
    main()