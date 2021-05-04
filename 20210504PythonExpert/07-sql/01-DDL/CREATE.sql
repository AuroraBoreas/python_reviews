
CREATE TABLE employee(
    empId   INT NOT NULL,
    empName VARCHAR(255) NOT NULL,
    empDept INT NULL,
    CONSTRAINT empPk PRIMARY KEY (empId),
    CONSTRAINT empDeptFk FOREIGN KEY (empDept) REFERENCES department(deptId)
);


CREATE TABLE department(
    deptId    INT NOT NULL,
    deptName  VARCHAR(255) NOT NULL,
    CONSTRAINT deptPk PRIMARY KEY (deptId)
);