```mermaid
erDiagram
    GRADE {
        INT grade_id PK
        VARCHAR(50) grade_name
    }

    CLASS {
        INT class_id PK
        INT grade_id FK
        VARCHAR(10) class_name
        INT teacher_id FK
    }

    STUDENT {
        INT student_id PK
        VARCHAR(50) student_name
        INT class_id FK
    }

    TEACHER {
        INT teacher_id PK
        VARCHAR(50) teacher_name
        INT subject_id FK
    }

    SUBJECT {
        INT subject_id PK
        VARCHAR(50) subject_name
    }

    GRADE ||--o{ CLASS : "has"
    CLASS ||--o{ STUDENT : "has"
    CLASS }o--|| TEACHER : "has"
    TEACHER }o--|| SUBJECT : "teaches"

```