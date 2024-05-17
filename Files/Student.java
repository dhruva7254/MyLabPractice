package com.bank;

public class Student 
{
	private int rollno;
	private String name,city;
	private static int rollCounter ;
	static
	{	
		rollCounter=100;	
	}
	public Student()
	{
		rollCounter=rollCounter+1;//1
		rollno=rollCounter;
		name="sham";
		city="pune";
	}
	public Student(String name, String city) 
	{	
		rollCounter=rollCounter+1;//2
		rollno=rollCounter;
		this.name = name;
		this.city = city;
	}
	public void show()
	{
		System.out.println(rollno+"   "+name+"    "+city);
	}
}
