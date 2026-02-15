# Receipt Management System (Template)

영수증(PDF)에서 추출한 결제 데이터를 체계적으로 관리하고 분석하기 위한 일반적인 템플릿 프로젝트입니다.

## 프로젝트 개요
이 시스템은 영수증 파일에서 데이터를 추출하여 JSON 형식으로 저장하고 관리하는 구조를 제공합니다. 개인의 결제 데이터를 깃(Git)과 같은 버전 관리 시스템에서 안전하게 관리할 수 있도록 설계되었습니다.

## 안티그래비티(AI)와 함께 사용하기

이 시스템은 안티그래비티(Antigravity) AI를 사용하여 영수증을 자동으로 읽고 데이터화할 때 가장 강력합니다.

### 사용 방법
1. **영수증 준비**: 네이버페이 등에서 내려받은 카드 영수증 PDF 파일을 이 폴더에 넣습니다.
2. **AI에게 요청**: 안티그래비티 채팅창에 영수증 파일을 첨부(@파일명)하고 다음과 같이 요청하세요:
   > "이 영수증 내용을 읽어서 `transactions.json` 형식에 맞춰 업데이트해줘."
3. **자동 판독 및 저장**: 안티그래비티가 시각적 분석(Visual Analysis)을 통해 이미지 기반의 PDF에서도 결제 정보를 정확히 추출하여 JSON 파일을 업데이트합니다.

## 프로젝트 구조

- `transactions.json`: 결제 데이터 저장소 (샘플 데이터 포함)
- `.gitignore`: 개인정보 및 불필요한 파일 제외 설정
- `README.md`: 프로젝트 안내 및 가이드

## 데이터 관리 가이드

1. **데이터 추가**
   `transactions.json` 파일에 본인이 추출한 결제 내역을 JSON 형식에 맞춰 추가하세요.
   
2. **보안 주의 사항**
   - 원본 PDF 파일명은 항상 `.gitignore`에 추가되어 있는지 확인하세요.
   - `transactions.json` 내의 승인번호나 카드정보는 필요한 경우 마스킹(예: `1234****`) 처리하는 것을 권장합니다.

## Git 연동 가이드

1. **로컬 저장소 초기화**
   ```bash
   git init
   ```

2. **개인정보 제외 확인**
   `.gitignore` 파일을 열어 `*.pdf` 또는 특정 영수증 파일명이 포함되어 있는지 확인합니다.

3. **파일 커밋 및 푸시**
   ```bash
   git add .
   git commit -m "Initialize generic receipt management template"
   git remote add origin <your-repository-url>
   git push -u origin main
   ```

## 라이선스
이 프로젝트는 교육 및 개인 관리용 템플릿으로 자유롭게 수정 및 배포가 가능합니다.
