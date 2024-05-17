package com.bank;
public class Employee 
{
	private int empid;
	private String name;
	private int age;
	private static int count;
	public Employee()
	{
		empid=1;
		name="xyz";
		age=30;
		count++;	
	}
	public Employee(int empid, String name, int age) 
	{
		super();
		this.empid = empid;
		this.name = name;
		this.age = age;
		count++;
	}
	public static void showCount()
	{
		System.out.println("Count:"+count);
	}
	public void show()
	{
		System.out.println("EmpId="+empid+"   Name   "+name+"   "+age+"    Count:"+count);
	}
}
