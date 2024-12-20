-- 학년 테이블
CREATE TABLE Grade (
    grade_id INT PRIMARY KEY,
    grade_name VARCHAR(50) NOT NULL
);

-- 반 테이블
CREATE TABLE Class (
    class_id INT PRIMARY KEY,
    grade_id INT,
    class_name VARCHAR(10) NOT NULL,
    teacher_id INT,
    FOREIGN KEY (grade_id) REFERENCES Grade(grade_id),
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);

-- 학생 테이블
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50) NOT NULL,
    class_id INT,
    FOREIGN KEY (class_id) REFERENCES Class(class_id)
);

-- 선생님 테이블
CREATE TABLE Teacher (
    teacher_id INT PRIMARY KEY,
    teacher_name VARCHAR(50) NOT NULL,
    subject_id INT,
    FOREIGN KEY (subject_id) REFERENCES Subject(subject_id)
);

-- 과목 테이블
CREATE TABLE Subject (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(50) NOT NULL
);

-- 데이터 삽입 예시
INSERT INTO Grade (grade_id, grade_name) VALUES (1, '1학년'), (2, '2학년'), (3, '3학년'), (4, '4학년'), (5, '5학년'), (6, '6학년');

INSERT INTO Subject (subject_id, subject_name) VALUES 
(1, '수학'), (2, '국어'), (3, '영어'), (4, '체육'), (5, '음악'), (6, '과학'), (7, '사회'), (8, '도덕');

INSERT INTO Teacher (teacher_id, teacher_name, subject_id) VALUES 
(1, '김철수', 1), 
(2, '이영희', 2), 
(3, '박민수', 3), 
(4, '최지우', 4), 
(5, '정해인', 5), 
(6, '한지민', 6);