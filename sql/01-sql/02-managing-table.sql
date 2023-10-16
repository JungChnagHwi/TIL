-- Table 구조 확인
PRAGMA table_info('examples');

-- `cid`
-- cid는 "Column ID"를 의미하는 컬럼
-- 각 컬럼의 고유한 식별자를 나타내는 정수 값
-- 일반적으로 cid 컬럼은 사용자가 직접 사용하지 않으며, 
-- PRAGMA table_info() 명령과 같은 메타데이터 조회 작업에서 컬럼의 정보를 식별하는 데 사용

-- 1. Create a table
CREATE TABLE examples (
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL, -- 문자열 데이터 50자까지 null은 안됨
  FirstName VARCHAR(50) NOT NULL  -- 필드명, 데이터타입, 제약조건 순
                                  -- AUTOINCREMENT 자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성,
                                  -- 필드의 자동증가, 항상 새로운 레코드에 대해 이전 최대 값보다 큰 값 할당, 삭제된 값 무시
);

-- 2. Modifying table fields
-- 2.1 ADD COLUMN
ALTER TABLE 
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL;
 
-- sqlite는 단일 문을 사용하여 한번에 여러 열을 추가하는 것을 지원하지 않음
ALTER TABLE examples
ADD COLUMN Age INTEGER NOT NULL; -- 필드 추가

ALTER TABLE examples
ADD COLUMN Address VARCHAR(100) NOT NULL;

-- 2.2 RENAME COLUMN
ALTER TABLE examples
RENAME COLUMN Address TO PostCode; -- 필드 이름 변경

-- 2.3 DROP COLUMN
ALTER TABLE examples
DROP COLUMN PostCode; -- 필드 삭제,, 삭제하는 필드가 다른 부분에서 참조되지 않고 기본키가 아니며  UNIQE 제약 조건이 없는 경우에만 작동

-- 2.4 RENAME TO
ALTER TABLE examples
RENAME TO new_examples; -- 테이블 이름 변경

-- 3. Delete a table
DROP TABLE new_examples; -- 테이블 삭제
DROP TABLE examples; -- 

-- sqlite는 컬럼 수정 불가
-- 대신 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용
