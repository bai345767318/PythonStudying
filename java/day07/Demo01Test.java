package day07;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/*
TDD测试驱动开发:Test-Driven Devlopment 开发功能代码之前，先编写测试用例。
JUnit单元测试框架，测试代码最小单元，也就是方法。python可能就是某语句。
JUnit：简单方便的组织测试代码，随时运行。生成测试报告，测试报告包含代码覆盖率。

 */

class Demo01Test {
    /*
    语句覆盖(覆盖度最低)：程序中每个语句至少执行一次。
    判定覆盖(分支覆盖)：(k<0||k>=str.length())，每个判定的true/false至少覆盖一次。
    条件覆盖：k<0是一个条件，一个判定点包含一个或多个条件，每个条件的true/false至少覆盖一次。
    路径覆盖(覆盖度最高)：基于流程图，把可能的路径全都覆盖。
    判定条件覆盖：每个判定true/false至少覆盖一次。每个判定中的每个条件的true/false至少覆盖一次。
    组合覆盖：上面集中覆盖方法组合使用
    一般条件下，判定覆盖少于条件覆盖
    @org.junit.jupiter.api.Test
     */
    @Test
    void z01() {
        Demo01 d = new Demo01();
        //调用要测试的方法，进行断言，前面是预期结果，后面是实际结果
        assertEquals(3,Demo01.z01("ashdjasdhkjas",'a'));
        assertEquals(0,Demo01.z01("ashdjasdhkjas",'b'));
    }

    @Test
    void jieQu() {
        assertEquals("ERROR:索引错误",Demo01.jieQu("",0));
        assertEquals("aass",Demo01.jieQu("aassddffgg",4));
        assertEquals("ERROR:索引错误",Demo01.jieQu("zxcv",5));
        assertEquals("ERROR:索引错误",Demo01.jieQu("",2));
        assertEquals("ERROR:空值",Demo01.jieQu(null,1));
    }

    @Test
    void nixu() {
        assertEquals("you love i",Demo01.nixu("i love you"));
        assertEquals("i",Demo01.nixu("i"));
        assertEquals("ERROR:空值",Demo01.nixu(null));
    }

    @Test
    void isTrangle(){
        //判定覆盖 if(a == b || b == c || a==c)
        assertEquals("等腰三角形",Demo01.isTriangle(2,2,3));
        assertEquals("一般三角形",Demo01.isTriangle(2,3,4));
        //条件覆盖：分支中每个条件的true/false取一次
        assertEquals("等腰三角形",Demo01.isTriangle(2,2,3));
        assertEquals("等腰三角形",Demo01.isTriangle(2,3,2));
        assertEquals("等腰三角形",Demo01.isTriangle(3,2,2));
        //a==b && a==c
        assertEquals("等边三角形",Demo01.isTriangle(2,2,2));
        assertEquals("Error:参数错误",Demo01.isTriangle(0,0,0));
        //!(a+b>c && a+c>b && b+c>a)
        assertEquals("不是三角形",Demo01.isTriangle(1,1,3));
        assertEquals("不是三角形",Demo01.isTriangle(2,6,2));
        assertEquals("不是三角形",Demo01.isTriangle(5,1,3));

    }

}