﻿-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "EMPLOYEES" (
    "EMP_NO" INTEGER   NOT NULL,
    "BIRTH_DATE" DATE   NOT NULL,
    "FIRST_NAME" VARCHAR(100)   NOT NULL,
    "LAST_NAME" VARCHAR(100)   NOT NULL,
    "GENDER" VARCHAR(1)   NOT NULL,
    "HIRE_DATE" DATE   NOT NULL,
    CONSTRAINT "pk_EMPLOYEES" PRIMARY KEY (
        "EMP_NO"
     )
);

CREATE TABLE "TITLES" (
    "EMP_NO" INTEGER   NOT NULL,
    "TITLES" VARCHAR(50)   NOT NULL,
    "FROM_DATE" DATE   NOT NULL,
    "TO_DATE" DATE   NOT NULL
);

CREATE TABLE "SALARIES" (
    "EMP_NO" INTEGER   NOT NULL,
    "SALARY" INTEGER   NOT NULL,
    "FROM_DATE" DATE   NOT NULL,
    "TO_DATE" DATE   NOT NULL
);

CREATE TABLE "DEPARTMENTS" (
    "DEPT_NO" VARCHAR(4)   NOT NULL,
    "DEPT_NAME" VARCHAR(30)   NOT NULL,
    CONSTRAINT "pk_DEPARTMENTS" PRIMARY KEY (
        "DEPT_NO"
     )
);

CREATE TABLE "DEPT_MANAGER" (
    "DEPT_NO" VARCHAR(4)   NOT NULL,
    "EMP_NO" INTEGER   NOT NULL,
    "FROM_DATE" DATE   NOT NULL,
    "TO_DATE" DATE   NOT NULL
);

CREATE TABLE "DEPT_EMP" (
    "EMP_NO" INTEGER   NOT NULL,
    "DEPT_NO" VARCHAR(4)   NOT NULL,
    "FROM_DATE" DATE   NOT NULL,
    "TO_DATE" DATE   NOT NULL
);

ALTER TABLE "TITLES" ADD CONSTRAINT "fk_TITLES_EMP_NO" FOREIGN KEY("EMP_NO")
REFERENCES "EMPLOYEES" ("EMP_NO");

ALTER TABLE "SALARIES" ADD CONSTRAINT "fk_SALARIES_EMP_NO" FOREIGN KEY("EMP_NO")
REFERENCES "EMPLOYEES" ("EMP_NO");

ALTER TABLE "DEPT_MANAGER" ADD CONSTRAINT "fk_DEPT_MANAGER_DEPT_NO" FOREIGN KEY("DEPT_NO")
REFERENCES "DEPARTMENTS" ("DEPT_NO");

ALTER TABLE "DEPT_MANAGER" ADD CONSTRAINT "fk_DEPT_MANAGER_EMP_NO" FOREIGN KEY("EMP_NO")
REFERENCES "EMPLOYEES" ("EMP_NO");

ALTER TABLE "DEPT_EMP" ADD CONSTRAINT "fk_DEPT_EMP_EMP_NO" FOREIGN KEY("EMP_NO")
REFERENCES "EMPLOYEES" ("EMP_NO");

ALTER TABLE "DEPT_EMP" ADD CONSTRAINT "fk_DEPT_EMP_DEPT_NO" FOREIGN KEY("DEPT_NO")
REFERENCES "DEPARTMENTS" ("DEPT_NO");

