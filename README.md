# 🎮 go-py-llm-rest-api <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=Go&logoColor=white"/> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Anaconda-44A8338?style=flat-square&logo=Anaconda&logoColor=white"/> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=LangChain&logoColor=white"/> <img src="https://github.com/user-attachments/assets/dbdacdea-4baa-4c0c-9925-f2cbb03cedc9" width=70> 
## 👉 Go/Python언어, REST API, LLM을 조합하여 만든 '게임 LoL 닉네임 AI 제너레이터'
### ✅ 프로젝트 소개
LLM을 통해 생성한 'LoL 게임 닉네임'을 Fiber 프레임워크 기반으로 제작한 REST API에 전송하는 기능을 코드로 구현했습니다.  
  
생성 내역 중복 검사가 필요 없는 도메인 영역을 선정하는 과정에서 꽤 많은 고민거리가 파생되었습니다.  
고민 끝에 게임 'League of Legends(약칭: LoL 또는 롤)'은 중복 닉네임을 허용한다는 것이 기억나서 해당 테마를 주제로 고르게 되었습니다.  
  
LLM 특유의 '할루시네이션'을 창의적인 요소를 부각시킬 수 있는 특징이라고 재해석하여 코드 작업에 임했습니다.  
할루시네이션 정도를 제어할 수 있는 temperature 변수 값을 1.0으로 설정함으로써 다채로운 닉네임을 생성할 수 있게끔 했습니다.  
+) 관련 논문 : [A Survey on Large Language Model Hallucination via a Creativity Perspective](https://arxiv.org/html/2402.06647v1)

또한 LLM 프롬프트에 '재밌지만 무례하지 않은 롤 닉네임을 추천해 주세요.' 내용을 포함시킴으로써 유저 간의 불쾌함을 최소화시킬 수 있도록 설정했습니다.

### 🔴 코드 동작 전에 해야 하는 작업
1. 'go-server' 폴더 위치에서 'go build' 명령어를 입력합니다.
2. 아나콘다 파이썬 가상환경을 설정하는 명령어 'conda create -n [가상환경 이름] python=3.10'를 입력합니다. 사용자 정의 값은 반드시 바꾸셔야 합니다.
3. 가상환경을 활성화하는 명령어 'conda activate [가상환경 이름]'을 입력합니다.
4. 'python-server' 폴더 위치에서 파이썬 라이브러리 환경을 설정하는 명령어'pip install -r requirements.txt'를 입력합니다.
5. '.env' 파일에서 발급받은 OpenAI API key 값을 입력합니다.

### 🟠 코드 동작 방법 (Linux 기준 작성)
1. 'go-server' 폴더 위치에서 './go-server' 명령어를 입력하여 go server를 활성화시킵니다.
2. 'python-llm-post' 폴더 위치에서 'python llm_post.py' 명령어를 입력합니다.
3. 웹 브라우저 또는 Postman에서 'http://
localhost:3000/users'가 성공적으로 잘 동작하는지 확인합니다.

### 🟢 코드 실행 결과
![image](https://github.com/user-attachments/assets/82bf88f8-d706-452e-a916-4e42ef6b6327)
  
![image](https://github.com/user-attachments/assets/bd5e2a17-0981-4d15-9cf2-a229497f5c98)
