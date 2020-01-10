# 1/10 - variable / control flow function
- ### variable
  - #### create variable
    + ##### SET @variable_name;
      ```mysql
      SET @a = 1;
      SET @b = 'MySQL';
      ```
   - #### variable type conversion
     + CAST ( ... AS variable type)
        ```mysql
        -- 실수 => 정수
        SELECT
            CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 갯수'
        FROM buyTbl;
        ```
     + CONVERT ( ... , variable type)
       ```mysql
       -- 숫자가 포함된 문자열
       SELECT CONVERT('2nd', SIGNED INTEGER); -- 2
       SELECT CONVERT('2nd123', SIGNED INTEGER); -- 2
       ```
       
- ### 제어 흐름 함수 (control flow function)
   - #### IF / IFNULL / NULLIF
     + ##### IF(수식, True 값1, False 값2)
       ```mysql
       SELECT IF(100 < 200, '크다', '작다'); -- 크다
       SELECT IF(100 > 200, '크다', '작다'); -- 작다
       ```
     + ##### IFNULL(수식1, 수식2) : 수식1이 NULL이 아니면 수식1 반환, NULL 이면 수식2 반환
       ```mysql
       SELECT IFNULL(NULL, 'NULL값이다'); -- NULL값이다
       SELECT IFNULL(100 + 300, 'NULL값이다.'); -- 400
       ```
     + ##### NULLIF(수식1, 수식2) : 수식1과 수식2가 같으면 NULL, 다르면 수식1 반환
       ```mysql
       SELECT NULLIF(50 + 50, 40 + 60); -- NULL
       SELECT NULLIF(50 + 50, 40 + 40); -- 100
       ```
   - #### CASE    
     + ##### CASE 값1 WHEN 값2 THEN 결과값1 ... ELSE 결과값2 END
       ```mysql
       SET @age = 5;
       SELECT 
          CASE @age
              WHEN 0 THEN '영'
              WHEN 5 THEN '오'
              WHEN 10 THEN '십'
              ELSE '지정된 숫자가 아니다'
          END AS '결과';
       ```
- ### 문자열 함수 (string function)
   - #### IF / IFNULL / NULLIF
     + ##### IF(수식, True 값1, False 값2)

- ### 날짜 및 시간 함수 (date and time function)
- ### 제어 흐름 함수 (control flow function)
- ### 제어 흐름 함수 (control flow function)
