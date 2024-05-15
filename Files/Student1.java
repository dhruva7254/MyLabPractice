package day3practice1;
public class Student1 
{
	private int rollno;
	private String name;
	private int marks;
//	public Student1(int rollno, String name, int marks) {
//		super();
//		this.rollno = rollno;
//		this.name = name;
//		this.marks = marks;
//	}
	public void assignStudent(int r, String n, int m)
	{
		rollno=r;
		name=n;
		marks=m;
	}
	public void showStudent()
	{
		System.out.println("Roll No.: "+rollno);
		System.out.println("Name: "+name);
		System.out.println("Marks: "+marks);
	}
}
