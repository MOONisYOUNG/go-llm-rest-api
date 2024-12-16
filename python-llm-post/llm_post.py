import requests
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv
from typing import List, Dict
import os

# OpenAI API Key 불러오기
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# LLM 정의하기 (창의력 극대화가 필요하므로 temperature은 1.0으로 설정)
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=1.0)

# 템플릿 정의하기
template = """
        재밌지만 무례하지 않은 롤 닉네임을 추천해 주세요. \
        닉네임 5개를 쉼표로 구분된 목록으로 생성합니다. \
        오직 쉼표로 구분된 목록만 반환하고 그 이상은 반환하지 마세요. \
        띄어쓰기 또는 영어를 포함해도 좋습니다.
        
        예시 : 라인전눈감고도함, 바론은내꺼야, 펭귄구르기
        """

human_template = "{text}"

# 프롬프트 정의하기
prompt = ChatPromptTemplate.from_messages([
    ("system", template),
])

# OutputParser 정의하기 (쉼표 기준으로 parsing 작업 수행)
class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str):
        return text.strip().split(", ")

# Chain 정의하기
chain = prompt | llm | CommaSeparatedListOutputParser()


# user 이름 생성 함수
def generate_user_name() -> List[Dict]:
    # 유저 정보 저장할 리스트 정의하기
    users = []
    
    # 유저 정보 생성하기
    results = chain.invoke({"text" : " "})

    for name in results:
        # Create user dictionary
        user = {
            "Name": name,
        }
        users.append(user)
    
    return users

# go 서버에 user 이름 POST 요청 보내는 함수
def post_users_to_go_server(users):
    base_url = "http://localhost:3000/users"
    
    for user in users:
        try:
            response = requests.post(base_url, json=user)
            if response.status_code == 201:
                print(f"Successfully posted user: {user['Name']}")
            else:
                print(f"Failed to post user {user['Name']}. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error posting user {user['Name']}: {e}")

def main():
    print("생성 작업을 마친 후, 3000번 포트에 POST 요청을 보냅니다.")
    users = generate_user_name()
    post_users_to_go_server(users)

if __name__ == "__main__":
    main()