```mermaid
sequenceDiagram
    participant 학생 as Student
    participant 학년/반 관리
    participant 학생 관리 시스템
    participant 학생 데이터베이스

    학생->>학년/반 관리: 입학 신청
    학년/반 관리->>학생 관리 시스템: 학생 정보 전달
    학생 관리 시스템->>학생 데이터베이스: 학생 정보 저장
    학생 데이터베이스-->>학생 관리 시스템: 저장 완료
    학생 관리 시스템-->>학년/반 관리: 학생 등록 완료
    학년/반 관리-->>학생: 입학 완료
```