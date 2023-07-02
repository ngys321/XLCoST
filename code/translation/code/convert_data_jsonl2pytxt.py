import json

# 입력 파일명과 출력 파일명 설정
input_file = "/home/ysnamgoong42/ws/XLCoST/nl2codesearch/dataset/program_level/Python/train.jsonl"
output_file = "/home/ysnamgoong42/ws/XLCoST/g4g/XLCoST_data/pair_data_tok_full_desc/Python-desc/train-Python-desc-tok.txt"

# .jsonl 파일 읽기
with open(input_file, "r") as file:
    lines = file.readlines()

# docstring_tokens 추출하여 텍스트 파일에 저장
with open(output_file, "w") as file:
    for line in lines:
        data = json.loads(line)
        docstring_tokens = data["docstring_tokens"]
        docstring_text = " ".join(docstring_tokens)
        file.write(docstring_text + "\n")

# 입력 파일명과 출력 파일명 설정
input_file = "/home/ysnamgoong42/ws/XLCoST/nl2codesearch/dataset/program_level/Python/train.jsonl"
output_file = "/home/ysnamgoong42/ws/XLCoST/g4g/XLCoST_data/pair_data_tok_full_desc/Python-desc/train-Python-desc-tok.py"

# .jsonl 파일 읽기
with open(input_file, "r") as file:
    lines = file.readlines()

# docstring_tokens 추출하여 텍스트 파일에 저장
with open(output_file, "w") as file:
    for line in lines:
        data = json.loads(line)
        code_tokens = data["code_tokens"]
        code_text = " ".join(code_tokens)
        file.write(code_text + "\n")









# 입력 파일명과 출력 파일명 설정
input_file = "/home/ysnamgoong42/ws/XLCoST/nl2codesearch/dataset/program_level/Python/valid.jsonl"
output_file = "/home/ysnamgoong42/ws/XLCoST/g4g/XLCoST_data/pair_data_tok_full_desc/Python-desc/val-Python-desc-tok.txt"

# .jsonl 파일 읽기
with open(input_file, "r") as file:
    lines = file.readlines()

# docstring_tokens 추출하여 텍스트 파일에 저장
with open(output_file, "w") as file:
    for line in lines:
        data = json.loads(line)
        docstring_tokens = data["docstring_tokens"]
        docstring_text = " ".join(docstring_tokens)
        file.write(docstring_text + "\n")

# 입력 파일명과 출력 파일명 설정
input_file = "/home/ysnamgoong42/ws/XLCoST/nl2codesearch/dataset/program_level/Python/valid.jsonl"
output_file = "/home/ysnamgoong42/ws/XLCoST/g4g/XLCoST_data/pair_data_tok_full_desc/Python-desc/val-Python-desc-tok.py"

# .jsonl 파일 읽기
with open(input_file, "r") as file:
    lines = file.readlines()

# docstring_tokens 추출하여 텍스트 파일에 저장
with open(output_file, "w") as file:
    for line in lines:
        data = json.loads(line)
        code_tokens = data["code_tokens"]
        code_text = " ".join(code_tokens)
        file.write(code_text + "\n")






# 입력 파일명과 출력 파일명 설정
input_file = "/home/ysnamgoong42/ws/XLCoST/nl2codesearch/dataset/program_level/Python/test.jsonl"
output_file = "/home/ysnamgoong42/ws/XLCoST/g4g/XLCoST_data/pair_data_tok_full_desc/Python-desc/test-Python-desc-tok.txt"

# .jsonl 파일 읽기
with open(input_file, "r") as file:
    lines = file.readlines()

# docstring_tokens 추출하여 텍스트 파일에 저장
with open(output_file, "w") as file:
    for line in lines:
        data = json.loads(line)
        docstring_tokens = data["docstring_tokens"]
        docstring_text = " ".join(docstring_tokens)
        file.write(docstring_text + "\n")

# 입력 파일명과 출력 파일명 설정
input_file = "/home/ysnamgoong42/ws/XLCoST/nl2codesearch/dataset/program_level/Python/test.jsonl"
output_file = "/home/ysnamgoong42/ws/XLCoST/g4g/XLCoST_data/pair_data_tok_full_desc/Python-desc/test-Python-desc-tok.py"

# .jsonl 파일 읽기
with open(input_file, "r") as file:
    lines = file.readlines()

# docstring_tokens 추출하여 텍스트 파일에 저장
with open(output_file, "w") as file:
    for line in lines:
        data = json.loads(line)
        code_tokens = data["code_tokens"]
        code_text = " ".join(code_tokens)
        file.write(code_text + "\n")
